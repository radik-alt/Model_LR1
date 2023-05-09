import random
import numpy as np
import math


class CountMath:
    def __init__(self, list_0, gl):
        self.req_list = gl
        self.gen_list = list_0
        self.n_type = [0, 0, 0, 0]

    def count_average(self):
        len_average = [0, 0, 0, 0]
        print("1 Item:")
        print("Средняя длина сообщений")
        for i in range(4):
            for j in self.gen_list:
                if j.type == i + 1:
                    self.n_type[i] += 1
                    len_average[i] += j.length
            len_average[i] /= self.n_type[i]
            print(f"{i + 1} {len_average[i]:.4}")
        print("\nВероятность поступления сообщения")
        [print(f"{i + 1} {self.n_type[i] / 100:4}") for i in range(4)]
        print()

    def count_queue_stats(self):
        lam = 0  # интенсивность поступления заявок
        wi = [0, 0, 0, 0]  # среднее время пребывания заявки i-го типа в очереди
        ti = [0, 0, 0, 0]  # средний промежуток времени между поступлением заявок i-го типа
        ui = [0, 0, 0, 0]  # среднее время пребывания заявки в системе
        temp_list = []
        lambda_i = [1, 1, 1, 1]  # интенсивность поступления заявок i-го типа
        li = [0, 0, 0, 0]  # средняя длина очереди заявок i-го типа
        pi_i = [0, 0, 0, 0]  # коэффициент загрузки оборудования заявками i-го типа
        pi = [0, 0, 0, 0]  # вероятность поступления заявки i-го типа
        mi = [1, 1, 1, 1]  # интенсивность обслуживания
        ni = [0, 0, 0, 0]  # коэффициент простоя
        w = 0  # среднее время пребывания заявки в очереди
        u = 0  # среднее время пребывания заявки в системе
        l = 0  # среднее число заявок в системе
        r = 0  # коэффициент загрузки
        print("2 Item:")
        print("Средняя длина очереди: ")
        for i in range(4):
            for j in self.req_list:
                if j.type == i + 1:
                    wi[i] += j.t_out
                    ui[i] += j.spent
            wi[i] /= self.n_type[i]
            ui[i] /= self.n_type[i]
            temp_list.clear()
            temp_list = [j.t_in for j in self.req_list if j.type - 1 == i]
            for j in range(1, self.n_type[i]):
                ti[i] += temp_list[j] - temp_list[j - 1]
            ti[i] /= self.n_type[i]
            lambda_i[i] /= ti[i]
            li[i] = wi[i] * lambda_i[i]
            print(f"{i + 1} {li[i]:.04}")
            print(f"w[i] {wi[i]} * lambda[i] {lambda_i[i]}")
            lam += self.n_type[i] * (i + 1) / 100
            mi[i] /= ui[i]
            pi_i[i] = self.n_type[i] * (i + 1) / mi[i] / 100
            r += pi_i[i]
            ni[i] = abs(1 - pi_i[i])
            pi[i] = lambda_i[i] / lam
            w += pi[i] * wi[i]
            u += pi[i] * ui[i]
            l += self.n_type[i] * (i + 1) * ui[i]
        print(f"W = {w}\nU = {u}\nL = {l}")
        print()
        vi = ui  # среднее время обслуживания заявки i-го типа, второй начальный момент времени обслуживания

        print()
        print("3 Item:")
        print("Среднее число заявок в системе")
        [print(f"{j + 1}. {self.n_type[j] * (j + 1) / 100}") for j in range(4)]
        print("Коэффициент загрузки оборудования заявками")
        [print(f"{j + 1}. {pi_i[j]:.5}") for j in range(4)]
        print("Коэффициент простоя")
        [print(f"{j + 1}. {ni[j]:.05}") for j in range(4)]
        print("Среднее время пребывания в системе")
        [print(f"{j + 1}. {ui[j]:.04}") for j in range(4)]
        print("Интенсивность обслуживания")
        [print(f"{j + 1}. {mi[j]:.04}") for j in range(4)]
        print(f"Коэффициент загрузки: \nR={r:.05}")


class Queue:
    def __init__(self, id, type, length):
        self.id = id
        self.type = type
        self.t_in = 0
        self.start = 0
        self.end = 0
        self.t_out = 0  # время простоя
        self.spent = math.ceil(length / 10)

    def __repr__(self):
        return f"Тпи: {self.type} Момент появления в канале: {self.t_in:5}; Начало обслуживания: {self.start:5} " \
               f"Конец обсулживания: {self.end:5} Время ожидания: {self.t_out:5} Время пребывания в канале {self.spent:5}"


class InputQueue:
    def __init__(self, arr):
        self.arr = arr

    def process_req(self):
        req_list = []
        t0 = math.ceil(self.arr[0].time * 60)
        for id, val in enumerate(self.arr):
            temp = Queue(id + 1, val.type, val.length)
            temp.t_in = t0
            temp.start = t0 + random.randint(0, 5)
            temp.end = temp.start + temp.spent
            temp.t_out = temp.start - temp.t_in
            t0 = temp.end + 1
            req_list.append(temp)

        return req_list


class Data():
    def __init__(self):
        self.type = 0
        self.address = 0
        self.length = 0
        self.time = 0

    def __repr__(self):
        return f"Тип: {self.type} Адресс: {self.address} Длинна: {self.length} Время: {self.time:.4}"


def create_req():
    """
    Генерация заявок
    :return: лист заявок
    """
    arr = []
    for i in range(100):
        example = Data()
        temp = random.random()
        example.length = random.randint(22, 254)
        example.time = abs(np.random.normal(0.4, math.sqrt(4.2)))

        if 0 <= temp <= 0.09:
            example.type = 1
            example.address = np.random.choice(range(1, 6), p=(0.52, 0.27, 0.09, 0.07, 0.05))
        elif 0.09 < temp <= 0.77:
            example.type = 2
            example.address = np.random.choice(range(1, 6), p=(0.34, 0.44, 0.07, 0.12, 0.03))
        elif 0.77 < temp <= 0.81:
            example.type = 3
            example.address = np.random.choice(range(1, 6), p=(0.63, 0.11, 0.08, 0.17, 0.01))
        elif 0.81 < temp <= 1:
            example.type = 4
            example.address = np.random.choice(range(1, 6), p=(0.51, 0.02, 0.23, 0.12, 0.12))

        arr.append(example)

    arr = sorted(arr, key=lambda x: x.time)
    return arr


if __name__ == '__main__':
    arr = create_req()
    input_queue = InputQueue(arr)
    list_input = input_queue.process_req()
    [print(i) for i in list_input]
    cm = CountMath(arr, list_input)
    cm.count_average()
    cm.count_queue_stats()
