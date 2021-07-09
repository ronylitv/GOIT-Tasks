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

print(is_integer('+378s90'))