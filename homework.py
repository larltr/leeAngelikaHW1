import numpy as np

# задание 1 создание массива
numbers = np.arange(1, 11)
bro_numbers = np.arange(2, 11, 2) #с шагом 2
print(numbers, bro_numbers)
print("-----------------------------")

# задание 2 простые операции
a = np.array([5, 10, 15, 20])
b = np.array([2, 4, 6, 8])
sum_result = a + b
non = a * 2
mim = b - a
print(a, b)
print("Сумма:", sum_result)
print("Умножение а на 2:", non)
print("Вычитание b от а:", mim)
print("-----------------------------")

# задание 3 свойства массивов
scores = np.array([85, 90, 78, 92, 88])
print(scores)
print("Сумма всех оценок:", np.sum(scores))
print("Среднее значение:", np.mean(scores))
print("Максимальное число:", np.max(scores))
print("Минимальное число:", np.min(scores))
print("-----------------------------")

# задание 4 изменение массивов
data = np.array([1, 2, 3, 4, 5])
data[2] = 10
data = np.append(data, 6)
print(data)
print("-----------------------------")

# задание 5 выбор по условию
temps = np.array([23, 25, 21, 28, 20, 26])
high_temps = temps[temps > 23]  # сопоставляется логическое значение True или False
if high_temps.size > 0:
    print(high_temps)
else:
    print("<23")
print("-----------------------------")

# доп задание
myMatrica = np.array([[1, 2, 3],
                      [4, 5, 6]])
print("Матрица:", myMatrica)
slayy = myMatrica[1]
print("\nВторая строка:")
print(slayy)
