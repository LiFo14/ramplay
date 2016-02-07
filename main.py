import psutil
from random import randint
from playdis import PlayDis

class RamPlay:
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
        try:
            self.proc_name = self.get_pid_name(proc, False)
            self.proc_mem_size = self.proc_name.memory_info()
        except psutil.ZombieProcess:
            self.get_proc_mem_size(self.get_rand_pid())
        self.rss = self.proc_mem_size[0]
        self.vms = self.proc_mem_size[1]
        if self.rss == 0 or self.vms == 0:
            self.get_proc_mem_size(self.get_rand_pid())
        return str(self.rss) + str(self.vms)

    def get_rand_pid(self):
        self.pids = self.get_pids()
        return self.pids[randint(0,len(self.get_pids())-1)]

    def get_rand_pid_info(self):
        self.size = self.get_proc_mem_size(self.get_rand_pid())
        self.name = self.get_pid_name(self.get_rand_pid())
        print self.size
        return self.size

if __name__ == '__main__':
    rp = RamPlay()
    play = PlayDis(rp.get_pid_name(rp.get_rand_pid()))
    play.initSeq(rp.get_rand_pid_info())
