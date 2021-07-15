from collections import Counter


def get_count_visits_from_ip(ips):
    return dict(Counter(ips))


def get_frequent_visit_from_ip(ips):
    return Counter(ips).most_common(1)[0]


tup1 = [('66.50.38.43', 4), ('76.98.129.245', 3),
        ('85.157.172.253', 2), ('173.37.214.238', 2),
        ('143.231.49.229', 1), ('27.137.126.114', 1),
        ('248.95.93.236', 1)]

print(Counter(tup1).most_common(1)[0])
# print(get_count_visits_from_ip())
# print(get_frequent_visit_from_ip())
