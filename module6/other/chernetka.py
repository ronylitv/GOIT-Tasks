fh = open('test.txt', 'w+')
fh.write('hello!')
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'he'

fh.close()

byte_str = 'some text'.encode()
print(byte_str)

byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')

print(byte_array) # bytearray(b'Bill Kill')