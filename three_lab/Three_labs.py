import math
import random

import numpy as np

from three_lab import Message
from three_lab.Data import Data

random_list = []
type_list = []


def generate_data():
    for i in range(100):
        random_list.append(random.random())


def generate_type_message() -> list:
    result_list = []
    mu = 0.4
    sigma = math.sqrt(4.2)
    norma = [random.normalvariate(mu, sigma) for i in range(100)]
    for item in range(len(random_list)):
        message = Message.Message()

        if 0 <= random_list[item] <= 0.09:
            message.type = 1
            message.address = np.random.choice(range(1, 6), p=(0.52, 0.27, 0.09, 0.07, 0.05))
        elif 0.09 < random_list[item] <= 0.77:
            message.type = 2
            message.address = np.random.choice(range(1, 6), p=(0.34, 0.44, 0.07, 0.12, 0.03))
        elif 0.77 < random_list[item] <= 0.81:
            message.type = 3
            message.address = np.random.choice(range(1, 6), p=(0.63, 0.11, 0.08, 0.17, 0.01))
        elif 0.81 < random_list[item] <= 1:
            message.type = 4
            message.address = np.random.choice(range(1, 6), p=(0.51, 0.02, 0.23, 0.12, 0.12))

        message.len = random.randrange(22, 254)
        message.time = norma[item]
        result_list.append(message)

    return result_list


def task():
    generate_data()

    arr: list[Message] = generate_type_message()
    arr = sorted(arr, key=lambda message: message.time)

    arr = sorted(arr, key=lambda x: x.time)
    coun = [0, 0, 0, 0]
    for i in arr:
        coun[i.type - 1] += 1
    print("1) Сравнение вероятностей появления сообщений (заданная и полученная)")
    for i in coun:
        print(i, i / 100)
    print("2) Сравнение средней длины заявки")
    arrange = []
    for j in range(1, 5):
        arrange.append(np.mean([i.len for i in arr if i.type == j]))
    maxmin = [[0, 99], [0, 99], [0, 99], [0, 99]]
    for i in arr:
        if i.len < maxmin[i.type - 1][1]:
            maxmin[i.type - 1][1] = i.len
        if i.len > maxmin[i.type - 1][0]:
            maxmin[i.type - 1][0] = i.len
    for i in range(4):
        print(f"{arrange[i]:.04}", maxmin[i][0])
    print("3) Вычисление средней частоты вычисления заявок")
    coun = [0, 0, 0, 0, 0]
    for i in arr:
        coun[i.address - 1] += 1
    maxt = arr[99].time
    for i in coun:
        print(i, i / maxt)
    print("4) Данные о вероятности и числе заявок в потоке сведены в таблицу.")
    coun = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for i in arr:
        coun[i.type - 1][i.address - 1] += 1
    for i in coun:
        print(i)
        sumi = sum(i)
        for j in i:
            print(f"{j / sumi:.2}", end=" ")
        print()
    time = [[], [], [], []]
    for i in arr:
        time[i.type - 1].append(i.time)
    print("Числовые характеристики ")
    for i in range(4):
        temp = Data(time[i])
        print(i + 1, temp)
    for i in arr:
        print(i)


if __name__ == "__main__":
    task()
