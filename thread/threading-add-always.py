#!/usr/bin/env python
# encoding=utf-8

import threading, time

count = 0


def adder(addlock):
    global count
    for i in range(100):
        with addlock:
            count = count + 1
        time.sleep(0.001)


def rundom():
    threads = []
    addlock = threading.Lock()
    for i in range(100):
        thread = threading.Thread(target=adder, args=(addlock,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(count)


if __name__ == "__main__":
    rundom()