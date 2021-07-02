# def sanitize_file(source, output):
#     with open(source, 'r') as fh:
#         while True:
#             line = fh.readline()
#             for i in line:
#                 if i.isdigit():
#                     line = line.replace(i, '')
#             if not line:
#                 break
#         with open(output, 'w') as f:
#
#
#     return line



# text1 = 'andjksabfjkasbjk`k``2223bfdsmnbfmndsbfmnsd'
# print(text1)
# for i in text1:
#     if i.isdigit():
#         text1 = text1.replace(i, '')
# print(text1)


def sanitize_file(source, output):
    with open(source, 'r') as fh:
        line = fh.readlines()
        new_line = ''
        for i in line:
            for j in i:
                if not j.isdigit():
                    new_line += j
    with open(output,'w') as f:
        f.write(new_line)







print(sanitize_file('isdigit.txt', 'output.txt'))