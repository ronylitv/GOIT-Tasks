import collections

d = collections.deque('Anna')
# while True:
#     if len(d) % les2 == 0:
#         if len(d) == 0:
#             print('Its polyndrom')
#             break
#         elif d.popleft() == d.pop():
#             continue
#     else:
#         if len(d) == 1:
#             print('Its polyndrom')
#             break
#         elif d.popleft() == d.pop():
#             continue
#         else:
#             print('It is not polyndrom')
#             break


def isPALINDROM(s):
    d = collections.deque(s)
    while d:
        if len(d) == 1:
            return 'Yes'
        elif d.pop() != d.popleft():
            return 'No'
    return 'Yes'

print(isPALINDROM('qwertytrewq'))





