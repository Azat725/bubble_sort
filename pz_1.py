def bubble_sort(array: list):
    # Цикл for для перебора элементов массива с индексами i и i+1
    for i in range(len(array)):
        # Внутренний цикл for для сравнения и обмена соседних элементов, если необходимо
        for j in range(0, len(array) - 1):
            # Если текущий элемент array[j] больше следующего элемента array[j + 1]
            if array[j] > array[j + 1]:
                # Обмен элементов местами с помощью кортежей
                array[j], array[j + 1] = array[j + 1], array[j]
                
    # Возвращение отсортированного массива в виде списка
    return list(array)

array = [3, 2, 1, 4, 5, 8, 6]
print(bubble_sort(array))