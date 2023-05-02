import math
import random

import numpy as np
from matplotlib import pyplot as plt

from MyRandom import MyRandom

list_default_random_100 = []
list_default_random_1000 = []
list_default_random_10000 = []

my_list_random_100 = []
my_list_random_1000 = []
my_list_random_10000 = []

N = [100, 1000, 10000]


def main():
    for n in N:
        list_default_random = default_generator(_n=n)
        expected_value = get_expected_value(list_default_random)
        dispersion = get_dispersion(list_default_random, expected_value)
        deviation = get_deviation(dispersion)
        print(f"Random{n}: "
              f"Мат.ожидание: {expected_value},"
              f" Дисперсия: {dispersion}, "
              f"Сред.квадра.отклонение: {deviation}")

        print(f"Random{n}: "
              f"Тест частотности: {particularity(list_default_random)}, \n"
              f"Тест равномерности: {uniform(list_default_random)} \n")
        # evaluate_uniformity(list_default_random)


        intervals = [i * 0.1 for i in range(11)]
        hist, _ = np.histogram(list_default_random, intervals)
        frequencies = hist / n

        plt.bar(intervals[:-1], frequencies, width=0.1)
        plt.xlabel(f'Значение случайной величины {n}')
        plt.ylabel('Частотность')
        plt.title('График функции P() для оценки частотности генератора')
        plt.show()

        my_list_random = my_generator(_n=n)
        my_expected_value = get_expected_value(my_list_random)
        my_dispersion = get_dispersion(my_list_random, my_expected_value)
        my_deviation = get_deviation(my_dispersion)
        print(f"MyRandom{n}: "
              f"Мат.ожидание: {my_expected_value},"
              f" Дисперсия: {my_dispersion}, "
              f"Сред.квадра.отклонение: {my_deviation}")
        # evaluate_uniformity(my_list_random)

        print(f"MyRandom{n}: "
              f"Тест частотности: {particularity(list_default_random)}, \n"
              f"Тест равномерности: {uniform(list_default_random)}")

        intervals = [i * 0.1 for i in range(11)]
        hist, _ = np.histogram(my_list_random, intervals)
        frequencies = hist / n

        plt.bar(intervals[:-1], frequencies, width=0.1)
        plt.xlabel(f'Значение случайной величины {n}')
        plt.ylabel('Частотность')
        plt.title('График функции P() для оценки частотности генератора')
        plt.show()

        print("------------------------------------------------")


def evaluate_uniformity(data):
    # Вычисляем теоретическое математическое ожидание
    a = np.min(data)
    b = np.max(data)
    theoretical_mean = (a + b) / 2

    # Вычисляем математическое ожидание для каждой последовательности
    sequence_lengths = np.arange(1, 11) * 1000
    means_fixed_length = []
    means_variable_length = []

    for length in sequence_lengths:
        sequence = data[:length]
        mean = np.mean(sequence)
        means_fixed_length.append(mean)

    for i, length in enumerate(sequence_lengths):
        sequence = data[:length]
        mean = np.mean(sequence)
        means_variable_length.append(mean)
        # Строим графики для первых 5 последовательностей переменной длины
        plt.plot(np.arange(i + 1), theoretical_mean - np.array(means_variable_length[:i + 1]), 'ro-')

    # Строим график для фиксированной длины последовательности
    plt.plot(sequence_lengths, theoretical_mean - np.array(means_fixed_length), 'bo-')

    plt.title('Evaluation of uniformity')
    plt.xlabel('Sequence number')
    plt.ylabel('Difference (M - Mi)')
    plt.legend(['Variable length sequences', 'Fixed length sequence'])
    plt.show()

def uniform(data: list) -> list:
    result = []
    mat = get_expected_value(data)
    res = mat - 0.5
    result.append(mat)
    result.append(res)

    return result


def particularity(data: list):
    step = 1.0 / 50
    result = [0] * 50
    counter = 0
    i = 0.02
    while i < 50:
        for j in range(len(data)):
            if i >= data[j] > (i - 0.02):
                result[counter] += 1

        i += step
        counter += 1
    return result


def my_generator(_n: int) -> list:
    myRandom = MyRandom()
    list_my_random = []
    for i in range(_n):
        list_my_random.append(myRandom.rand())
    return list_my_random

def default_generator(_n: int) -> list:
    generate_list = []
    for i in range(_n):
        generate_list.append(random.uniform(0, 1))

    return generate_list


def get_expected_value(arr: list):
    return sum(arr) / len(arr)


def get_dispersion(arr: list, expected_value):
    value_sum = 0
    for i in arr:
        value_sum += i * i
    return value_sum / len(arr) - math.pow(expected_value, 2)


def get_deviation(dispersion):
    return math.sqrt(dispersion)


if __name__ == "__main__":
    main()
