import time

class timeclass(object):
    times=0.0
    def __init__(self):
        self.times=0.0
    def r(self):
        self.times=time.time()
    def g(self,strx):
        print(strx+" 耗时="+str(round(time.time()-self.times,2)))