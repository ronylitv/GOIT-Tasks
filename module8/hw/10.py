from collections import deque

MAX_LEN = 10

fifo = deque(maxlen=MAX_LEN)


def push(element):
    return fifo.append(element)


def pop():
    return fifo.popleft()
