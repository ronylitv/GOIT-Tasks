def caching_fibonacci():
    cache_dict = {0:0}
    def fibonacci(n):
        if n == 0:
            return 0

        if n <= 1:
            return 1
        elif n-1 in cache_dict.keys() or n-2 in cache_dict.keys():
            return cache_dict[n-1] + cache_dict[n-2]
        else:
            cache_dict[n-1] = fibonacci(n - 1)
            cache_dict[n-2] = fibonacci(n - 2)
            return fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci


p = caching_fibonacci()
print(p(0))
