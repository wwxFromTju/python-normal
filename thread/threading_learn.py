#!/usr/bin/env python
# encoding=utf-8

import threading


class MyThread(threading.Thread):
    def __init__(self, my_id, count, mutex):
        self.my_id = my_id
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print('{} => {}'.format(self.my_id, i))


if __name__ == '__main__':
    stdout_mutex = threading.Lock()
    threads = []
    for i in range(10):
        thread = MyThread(i, 100, stdout_mutex)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("main exit")