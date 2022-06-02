import threading
import time
from queue import Queue

lock = threading.Lock()


class ClassThreading(threading.Thread):
    def __init__(self, value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = value

    def run(self) -> None:
        with lock:
            print('class start')
        time.sleep(2)
        with lock:
            print('class value', self.value)


threads = [ClassThreading(x) for x in range(10)]

for i in threads:
    i.start()

for i in threads:
    i.join()
