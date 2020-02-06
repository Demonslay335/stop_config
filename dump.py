import os
import sys
import time
import winappdbg
import traceback


class MyEventHandler(winappdbg.EventHandler):

    last_alloc_memory = 0
    first_alloc_memory = 0
    address_of_alloc_memory = 0
    first_post = 0
    start_routine=0
    me=0
    catch_now=0

    virtualallocarea=[]
    memory_protection = {
        '0x01':'PAGE_NOACCESS',
        '0x02':'PAGE_READONLY',
        '0x04':'PAGE_READWRITE',
        '0x08':'PAGE_WRITECOPY',
        '0x10':'PAGE_EXECUTE',
        '0x20': 'PAGE_EXECUTE_READ',
        '0x40':'PAGE_EXECUTE_READWRITE',
        '0x80':'PAGE_EXECUTE_WRITECOPY'
        }

    openprocess_desiredaccess = {
        '0x01':'PROCESS_TERMINATE',
        '0x02':'PROCESS_CREATE_THREAD',
        '0x08':'PROCESS_VM_OPERATION',
        '0x10':'PROCESS_VM_READ',
        '0x20':'PROCESS_VM_WRITE',
        '0x40':'PROCESS_DUP_HANDLE',
        '0x80':'PROCESS_CREATE_PROCESS',
        '0x100':'PROCESS_SET_QUOTA',
        '0x200':'PROCESS_SET_INFORMATION',
        '0x400':'PROCESS_QUERY_INFORMATION',
        '0x800':'PROCESS_SUSPEND_RESUME',
        '0x1000':'PROCESS_QUERY_LIMITED_INFORMATION',
        '0x100000':'SYNCHRONIZE'
        }

    apiHooks = {
        "kernel32.dll":[
            ("VirtualAlloc",4),
            ("VirtualAllocEx",5),
            ("VirtualProtect",4),
        ]
    }


    def print_param(self,param):
        ind=0
        print(len(param))
        for par in param:
            print("Param {}: {}".format(ind,par))
            ind=ind+1

    def print_retval(self,retval):
        print("{}".format(retval))

    def pre_VirtualAlloc(self, event, *argv):
        print("------------------------------ VirtualAlloc {}----------------------------".format(hex(argv[0])))
        print("""
            _In_opt_ LPVOID lpAddress: {}
            _In_     SIZE_T dwSize: {}
            _In_     DWORD  flAllocationType: {}
            _In_     DWORD  flProtect:{}""".format(hex(argv[1]),argv[2],argv[3],argv[4]))
        self.virtualallocarea.append(argv[2])
        if argv[2] == 56832:
            print("Write  MEM {} ({})".format(argv[1],hex(argv[1])))
            self.mem = argv[1]
            self.catch_now=1

    def post_VirtualAlloc(self, event, *argv):
        print("\tReturn:{}".format(hex(argv[0])))
        self.virtualallocarea.append(argv[0])

        if self.catch_now == 1:
            self.mem = argv[0]
        self.catch_now=0


    def pre_VirtualProtect(self, event, *argv):
        if self.first_alloc_memory == 0:
            self.address_of_alloc_memory = argv[1]
            self.first_alloc_memory = 1
        else:
            self.last_alloc_memory = argv[1]#+argv[2]
        print("------------------------------ VirtualProtect ({})----------------------------".format(hex(argv[0])))
        print("""
            _In_  LPVOID lpAddress: {}
            _In_  SIZE_T dwSize: {}
            _In_  DWORD  flNewProtect: {}
            _Out_ PDWORD lpflOldProtect: {}""".format(hex(argv[1]),argv[2], self.memory_protection[("0x%.2x") %argv[3]],hex(argv[4])))
        self.print_param(argv)

    def post_VirtualProtect(self, event, *argv):
        p = event.get_process()
        z=self.virtualallocarea
        for i in range(0,len(z)):
            if i%2==0:
                try:
                    data = p.read(z[i+1],z[i])
                    if data[:2]=='MZ':
                        memfilename=str("dump-")+str(z[i+1])+".mem"
                        f=open(memfilename,'wb')
                        f.write(data)
                        f.close()
                        print("Success dump memory {} to file:{}".format(hex(z[i+1]),memfilename))
                        raise KeyboardInterrupt
                except KeyboardInterrupt:
                    raise
                except:
                    pass

    def pre_VirtualProtectEx(self, event, *argv):
        print("------------------------------ VirtualProtectEx ----------------------------")
        self.print_param(argv)

    def my_event_handler(event):
        pid= event.get_pid()

        System.request_debug_privileges()
        process = Process(pid)

def simple_debugger(filename):
  global logfile

  try:
    handler = MyEventHandler()
    with winappdbg.Debug(handler,bKillOnExit = True) as debug:
      abspath = os.path.abspath(filename)
      debug.execl(os.path.join(os.path.dirname(abspath), filename))
      debug.loop()
  except KeyboardInterrupt:
    print("Stopped")
  except:
    traceback.print_exc()

simple_debugger(sys.argv[1])
