# class OpenFile:
#     def __init__(self, file_name, mode):
#         self.filename = file_name
#         self.mode = mode
#         self.file_handler = None
#
#     def __enter__(self):
#         self.file_handler = open(self.filename, self.mode)
#         return self.file_handler
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file_handler.close()
#
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         if a in [5, 8, 13]:
#             a, b = b, a + b
#             continue
#         yield a
#         a, b = b, a + b


class FibIterator:
    def __init__(self, count):
        self.count = count
        self.generated_numbers = 0

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.generated_numbers = 0
        return self

    def __next__(self):
        if self.generated_numbers <= self.count:
            self.a, self.b = self.b, self.a + self.b
            self.generated_numbers += 1
            return self.a
        else:
            raise StopIteration


if __name__ == '__main__':
    fib_iter = FibIterator(10)
    print(list(fib_iter.__iter__()))

