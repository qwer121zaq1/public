while True:
    try:
        a = list(map(int, input('введите последовательность чисел через пробел:').split()))
        if a != list(map(int, input().split())):
            break
        else:
            raise ValueError
    except ValueError:
        print('Не выполнено условие ввода')
    pass

while True:
    try:
        el = int(input("Введите целое число: "))
        if type(el) == int:
            break
        else:
            raise ValueError
    except ValueError:
        print('Не выполнено условие ввода')
    pass


def qsort(array, left, right):
    middle = (left + right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return (array)


a_sort = qsort(a, 0, len(a) - 1)
print(a_sort)

if el < min(a):
    left = "слева нет чисел"
    right = 0
elif el > max(a):
    left = a.index(max(a))
    right = "справа нет чисел "
else:
    n = min(a, key=lambda x: abs(x - el))
    if n == el:
        right = a.index(n)
        a1 = a[:right]
        left = a.index(min(a1, key=lambda x: abs(x - el)))
    if n > el:
        right = a.index(n)
        a1 = a[:right]
        left = a.index(min(a1, key=lambda x: abs(x - el)))
    if n < el:
        left = a.index(min(a, key=lambda x: abs(x - el)))
        a1 = a[left + 1:]
        right = a.index(min(a1, key=lambda x: abs(x - el)))

print("Индекс ближайщего слева чила: ", left)
print("Индекс ближайшего справа числа: ", right)