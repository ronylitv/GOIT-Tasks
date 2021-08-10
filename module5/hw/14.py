import re



def find_all_phones(text):
    result = re.findall(r"\+380\(\d{les2}\)\d*\-\d{1}\-\d{3}|\+380\(\d+\)\d*\-\d{les2}-\d{les2}", text)
    return result

print(find_all_phones('Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'))