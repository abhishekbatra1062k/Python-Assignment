import time
import threading

class multiThreading(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(multiThreading, self).__init__(*args, **kwargs)
        self._stop_event=threading.Event()
        self.name=kwargs.get('name')

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        start=time.time()
        x=0
        while not self.stopped():
            print(f"{self.name} is running at {int(x)}\n")
            time.sleep(5)
            x=time.time()-start

t1=multiThreading(name='Thread 1', args=("task-1",))
t2=multiThreading(name='Thread 2', args=("task-2",))
t3=multiThreading(name='Thread 3', args=("task-3",))

t1.start()
t3.start()
time.sleep(20)
t1.stop()
t1.join()
t2.start()
time.sleep(18)
t3.stop()
t3.join()
t1 = multiThreading(name='Thread 1', args=("task-1",))
t1.start()