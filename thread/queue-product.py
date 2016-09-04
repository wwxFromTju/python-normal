#!/usr/bin/env python
# encoding=utf-8

import _thread as thread, queue, time

safe_print = thread.allocate_lock()
data_queue = queue.Queue()

num_consumers = 2
num_producers = 4
num_messages = 4


def producer(num):
    for msgnum in range(num_messages):
        time.sleep(num)
        data_queue.put('[producer id={}, count={}]'.format(num, msgnum))


def consumer(num):
    while True:
        time.sleep(0.1)
        try:
            data = data_queue.get(block=False)
        except queue.Empty:
            pass
        else:
            with safe_print:
                print('consumer', num, 'got=>', data)


if __name__ == "__main__":
    for i in range(num_consumers):
        thread.start_new_thread(consumer, (i,))

    for i in range(num_producers):
        thread.start_new_thread(producer, (i,))

    time.sleep(((num_producers - 1) * num_messages) + 1)

    print("main exit")