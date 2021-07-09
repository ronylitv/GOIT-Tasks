def write_and_get_employees(employee_list, path):
    fh = open(path, 'w')
    for el in employee_list:
        for i in el:
            fh.write(i + '\n')

    fh.close()
    fh = open(path, 'r')
    lines = fh.readlines()
    return lines

print(write_and_get_employees([['Robert Stivenson,282', 'Alex Denver,30'],['Drake Mikelsson,19']], 'salary1.txt'))









