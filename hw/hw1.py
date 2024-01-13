# Задача 1
# Дан список целых чисел numbers. Необходиом написать в императивном стиле процедуру для сортировки
# числа в сприске в порядке убывания. Можно использовать любой алгоритм сортировки.
def sort_list_imperative(numbers):
    flag = True
    while flag:
        flag = False
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                flag = True
    return numbers


# Задача 2
# Написать точно такую же процедуру, но в декларативном стиле.
def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]
print(sort_list_imperative(nums1))
print(sort_list_declarative(nums2))
