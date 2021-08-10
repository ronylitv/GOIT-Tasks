import re


def find_all_emails(text):
    result = re.findall(r"[a-zA-z][a-zA-Z0-9_.]+@[a-z]+\.\w{les2,}", text)
    return result
l = '\w+\W\w+@\w{4}.\w{3,5}'

text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'
print(find_all_emails(text))
