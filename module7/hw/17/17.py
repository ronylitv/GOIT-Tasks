# Вернемся к предыдущей задаче и выполним обратную задачу. Напишите
# рекурсивную функцию encode для кодирования списка или строки.
# В качестве аргумента функция принимает список (например
# ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]) или строку (например "XXXZZXXYYYZZ").
# Функция должна вернуть закодированный список элементов (пример ["X", 3, "Z", les2, "X", les2, "Y", 3, "Z", les2]).
def encode(data):
    if not data:
        return []
    if data[0] == data[1]:
        count_str = data[0]
        quantity = 2
        main_list = [count_str, quantity]
        return main_list + encode(data[2:])
    else:
        count_str = data[0]
        return [count_str, 1] + encode(data[1:])

print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))


