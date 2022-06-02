import multiprocessing
import time


def clock(interval):
    print(interval)
    time.sleep(1)
    print('end')


class ClockProcess(multiprocessing.Process):
    def __init__(self, interval: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.interval = interval

    def run(self) -> None:
        print('class', self.interval)
        time.sleep(1)
        print('end')


if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(1, ))
    p.start()
    p.join()

    c = ClockProcess(2)
    c.start()
    c.join()
