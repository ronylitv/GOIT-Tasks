def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as f:
        f.write(additional_info)

    with open(path, 'r') as f:
        f.seek(start_pos)
        line = f.read(count_chars)
    return line



print(file_operations('hw.txt', 'akfflkdsflsk', 8, 10))