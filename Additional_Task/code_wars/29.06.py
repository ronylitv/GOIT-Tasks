def sum_of_intervals(intervals):
    l = []
    for s, e in intervals:
        l += range(s, e)
    return len(set(l))


print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
