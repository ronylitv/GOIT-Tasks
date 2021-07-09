# def all_sub_lists(data):
#     worked_data = data.copy()
#     main_list = [[]]
#     for i in worked_data:
#         main_list.append([i])
#     for i in range(len(worked_data)):
#         main_list.append(worked_data[:2])
#         worked_data = worked_data[1:]
#         if len(worked_data) == 1:
#             break
#     return main_list + [data]




def all_sub_lists(data: list):
    worked_data = data.copy()
    main_list = [[]]
    if len(data)>1:
        for i in data:
            main_list.append([i])

        if len(data) == 3:
            for i in range(len(data) - 1):
                main_list.append(worked_data[:2])
                worked_data = worked_data[1:]
        if len(data) == 4:
            for i in range(len(data) - 1):
                main_list.append(worked_data[:2])
                worked_data = worked_data[1:]
            worked_data = data.copy()
            for i in range(len(data) - 2):
                main_list.append(worked_data[:3])
                worked_data = worked_data[1:]
        return main_list + [data]
    else:
        return main_list

b = [4, 6, 1, 3]
a = [1, 2, 3]
print(all_sub_lists(b))

