#
# seconds = 250
# minute = 0
# if seconds >= 60:
#     minute = seconds // 60
#     seconds %= 60
# if minute >= 60:
#     hh = minute // 60
#     minute %= 60
# else:
#     hh = 0
# hh = str(hh)
# minute = str(minute)
# seconds = str(seconds)
# if len(hh) == 1:
#     hh = '0' + hh
# if len(minute) == 1:
#     minute = '0' + minute
# if len(seconds) == 1:
#     seconds = '0' + seconds
#
#
# result = str(hh) + ':' + str(minute) + ':' + str(seconds)
#




# def make_readable(seconds):
#     minute = 0
#     if seconds >= 60:
#         minute = seconds // 60
#         seconds %= 60
#     if minute >= 60:
#         hh = minute // 60
#         minute %= 60
#     else:
#         hh = 0
#     hh = str(hh)
#     minute = str(minute)
#     seconds = str(seconds)
#     if len(hh) == 1:
#         hh = '0' + hh
#     if len(minute) == 1:
#         minute = '0' + minute
#     if len(seconds) == 1:
#         seconds = '0' + seconds
#
#     result = str(hh) + ':' + str(minute) + ':' + str(seconds)
#     return result
#
# print(make_readable(345))

# def make_readable(s):
#     return '{:02}:{:02}:{:02}'.format(s // 3600, s // 60 % 60, s % 60)
#
#
# print(make_readable(345))
def primeFactors(n):
    ret = ''
    for i in xrange(2, n + 1):
        num = 0
        while(n % i == 0):
            num += 1
            n /= i
        if num > 0:
            ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
        if n == 1:
            return ret

def primeFactors(n):
    i, j, p = 2, 0, []
    while n > 1:
        while n % i == 0: n, j = n / i, j + 1
        if j > 0: p.append([i,j])
        i, j = i + 1, 0
    return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in p)