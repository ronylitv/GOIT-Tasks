def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for el in employee_list:
        for i in el:
            fh.write(i + '\n')

    fh.close()

write_employees_to_file([['Robert Stivenson,282', 'Alex Denver,30'],['Drake Mikelsson,19']], 'salary1.txt')









