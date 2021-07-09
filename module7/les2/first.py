# with open('text.txt', 'r') as f:
#     # lines = f.readlines()
#     # print(lines[0])
#     # line = f.readline()
#     # print(line)
#     print(f.readline())

def check_password(file, log_and_pass):
    with open(file, 'r') as f:
        lines = f.readlines()
        for i in lines:
            i.rstrip()
            if log_and_pass in i:
                print('Success')
                break
            else:
                continue


check_password('text.txt', 'a b')

