def format_phone_number(func):
    def inner(x: str):
        number = func(x)
        if number.startswith('380'):
            number = '+' + number
        elif not number.startswith('+380'):
            number = '+38' + number
        return number
    return inner


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone


print(sanitize_phone_number('+38(050)123-32-34'))
print(sanitize_phone_number(' 0503451234'))
