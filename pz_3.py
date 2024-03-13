def first_half(array: list) -> list:
    # Определяем половину длины списка
    half_length = len(array) // 2
    # Получаем первую половину списка
    first_half = array[:half_length]

    # Возвращаем первую половину списка
    return list(first_half)


def second_half(array: list) -> list:
    # Определяем половину длины списка
    half_length = len(array) // 2
    # Получаем вторую половину списка
    second_half = array[half_length:]

    # Возвращаем вторую половину списка
    return list(second_half)


def sort_first_half(array: list) -> list:
    # Внешний цикл для прохода по всем элементам списка
    for i in range(len(array)):
        # Внутренний цикл for для сравнения и обмена соседних элементов, если необходимо
        for j in range(0, len(array) - 1):
            # Если текущий элемент array[j] больше следующего элемента array[j + 1]
            if array[j] > array[j + 1]:
                # Обмен элементов местами с помощью кортежей
                array[j], array[j + 1] = array[j + 1], array[j]

    # Возвращение отсортированного списка
    return list(array)


def sort_second_half(array: list) -> list:
    # Начинаем с индекса 1, чтобы не сравнивать с элементом, который находится перед первым
    for i in range(1, len(array)):
        # Если предыдущий элемент меньше текущего, меняем их местами
        if array[i - 1] < array[i]:
            array[i - 1], array[i] = array[i], array[i - 1]

    # Возвращаем отсортированный список
    return list(array)


array = [3, 2, 1, 4, 5, 8, 6, 3]
# Получаем первую и вторую половины списка
fh = first_half(array)
sh = second_half(array)
# Сортируем каждую половину и объединяем их в результат
result = list(sort_first_half(fh) + sort_second_half(sh))
print(result)