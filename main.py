import psutil
from random import randint

class ProcMus:
    def get_pids(self):
        return psutil.pids()
    def print_pids(self):
        print(self.pids)
    def get_pid_name(self, n=1, name=True):
        self.proc_name = psutil.Process(n)
        if name:
            return self.proc_name.name()
        else:
            return self.proc_name
    def get_proc_mem_size(self, proc):
        self.proc_name = self.get_pid_name(proc, False)
        self.proc_mem_size = self.proc_name.memory_info()
        self.rss = self.proc_mem_size[0]
        self.vms = self.proc_mem_size[1]
        return str(self.rss) + str(self.vms)
    def get_rand_pid(self):
        self.pids = self.get_pids()
        self.rand_pid = self.pids[randint(0,len(self.pids))]
        self.size = self.get_proc_mem_size(self.rand_pid)
        self.name = self.get_pid_name(self.rand_pid)
        if self.get_proc_mem_size(self.rand_pid) > 1:
            print self.rand_pid, self.name
            print self.size
            #print oct(self.size)
            #print bin(self.size)
        else:
            self.get_rand_pid()

if __name__ == '__main__':
    p = ProcMus()
    p.get_rand_pid()
    #print p.get_pid_name()
