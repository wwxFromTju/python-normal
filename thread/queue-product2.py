#!/usr/bin/env python
# encoding=utf-8

import threading, queue, time

safe_print = threading.Lock()
data_queue = queue.Queue()

num_consumers = 2
num_producers = 4
num_messages = 4


def producer(num, queue_var):
    for msgnum in range(num_messages):
        time.sleep(num)
        queue_var.put('[producer id={}, count={}]'.format(num, msgnum))


def consumer(num, queue_var):
    while True:
        time.sleep(0.1)
        try:
            data = queue_var.get(block=False)
        except queue.Empty:
            pass
        else:
            print('consumer', num, 'got=>', data)


if __name__ == "__main__":
    for i in range(num_consumers):
        thread = threading.Thread(target=consumer, args=(i, data_queue))
        thread.daemon = True
        thread.start()

    waitfor = []

    for i in range(num_producers):
        thread = threading.Thread(target=producer, args=(i, data_queue))
        waitfor.append(thread)
        thread.start()

    for thread in waitfor:
        thread.join()

    print("main end")