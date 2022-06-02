import threading

lock = threading.Lock()


def timer_callback():
    with lock:
        print('t')


while True:
    timer = threading.Timer(1, timer_callback)
    timer.start()
    timer.join()
