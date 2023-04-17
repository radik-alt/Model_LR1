import math
import random
import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt

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


        my_list_random = my_generator(_n=n)
        my_expected_value = get_expected_value(my_list_random)
        my_dispersion = get_dispersion(my_list_random, my_expected_value)
        my_deviation = get_deviation(my_dispersion)
        print(f"MyRandom{n}: "
              f"Мат.ожидание: {my_expected_value},"
              f" Дисперсия: {my_dispersion}, "
              f"Сред.квадра.отклонение: {my_deviation}")

        print(f"MyRandom{n}: "
              f"Тест частотности: {particularity(list_default_random)}, \n"
              f"Тест равномерности: {uniform(list_default_random)}")

        print("------------------------------------------------")


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
    generate_list = []
    for i in range(_n):
        if i == 0:
            generate_list.append(MyRandom(0).next())
        else:
            generate_list.append(MyRandom(generate_list[i - 1]).next())

    return generate_list


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
