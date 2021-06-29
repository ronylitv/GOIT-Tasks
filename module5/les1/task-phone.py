from myphone import is_valid_phone

registration = []

for phone in ['380682450080', '0000000000',
                 '0964046372', '3805033 87099', '0503734441',
                 '380002450080', '+380682460080', '+38 (050) 33 870 99']:
    if is_valid_phone(phone):
        registration.append(phone)

connected = []

for phone in ['380682450080', '0000000000',
              '0964046372', '380002450080', '+380682460080']:
    if is_valid_phone(phone):
        connected.append(phone)

print(registration)
print(connected)

result = list(set(registration) & set(connected))
print(result)