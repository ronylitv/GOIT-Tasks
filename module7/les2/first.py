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
            if i.find(log_and_pass) != -1:
                print('Success')
                break
            else:
                print('Unsuccessful')


check_password('text.txt', 'd l')

