#!/usr/bin/env python
# encoding=utf-8

import threading, time

count = 0


# 这里比较不一样
# 在2.7中会出现随机, 在3.5中不会
def adder():
    global count
    for i in range(100):
        count = count + 1
        time.sleep(0.001)


def rundom():
    threads = []
    for i in range(100):
        thread = threading.Thread(target=adder)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(count)


if __name__ == "__main__":
    rundom()