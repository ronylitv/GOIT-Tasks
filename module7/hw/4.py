# def is_integer(s: str):
#     s = (s.strip()
#          .removeprefix('+')
#          .removeprefix('-'))
#
#     if len(s) == 0:
#         return False
#     else:
#         count = 0
#         for i in s:
#             if i in '0123456789':
#                 count += 1
#         if len(s) == count:
#             return True




def is_integer(s: str):
    s = (s.strip()
         .removeprefix('+')
         .removeprefix('-'))
    if len(s) >= 1:
        for i in s:
            try:
                i = int(i)
            except:
                return False
        return True

print(is_integer('+380    993299  '))




