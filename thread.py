import threading
import time

lock = threading.Lock()


def thread_target(a, b):
    #     with lock: - Это то же самое что и lock.acquire() ... lock.release()
    #         ...
    with lock:
        print('start')
    time.sleep(2)
    with lock:
        print(a, b)


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


t1 = threading.Thread(target=thread_target, args=(1, 2))
t1.start()

t2 = threading.Thread(target=thread_target, args=(3, 4))
t2.start()

t3 = ClassThreading(1)
t3.start()

t1.join()
t2.join()
t3.join()
