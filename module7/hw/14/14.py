# def to_indexed(start_file, end_file):
#     with open(start_file, 'r') as file_start:
#         lines = file_start.readlines()
#         count = 0
#         for item in lines:
#             item = str(count) + ': ' + item
#             with open(end_file, 'a') as f:
#                 f.write(item)
#             count +=1
def to_indexed(start_file, end_file):
    with open(start_file, 'r') as file_start:
        lines = file_start.readlines()
        count = 0
        text_for_add = ''
        for item in lines:
            item = str(count) + ': ' + item
            text_for_add += item
            count += 1
        with open(end_file, 'w') as f:
            f.write(text_for_add)





to_indexed('text.txt', 'new_file.txt')