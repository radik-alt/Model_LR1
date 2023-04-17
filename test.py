from math import factorial


def calculate_li(beta_i, K_i, pi_0i):
    first_term = (beta_i ** K_i) / (factorial(K_i) * K_i * ((1 - beta_i / K_i) ** 2))
    li = first_term * pi_0i
    return li


def pi_0i(b, k, p0):
    result = 0
    for m in range(k):
        result += (b ** m) / factorial(m)
    result += (b ** k) / (factorial(k) * (1 - (b / k)))
    return (1 - p0) * result + 1


def calc_mid_sum(li, bi):
    return li + bi


def calc_time_await_mid(li, yi):
    return li / yi


def calc_time_into_mid(mi, yi):
    return mi / yi


if __name__ == "__main__":
    listli = [0.0261, 0.236, 0.239, 1.093, 0.062]
    listbi = [0.189, 0.191, 0.193, 0.178, 0.152]
    listyi = [0.945, 0.958, 0.967, 1.07, 0.76]
    listmi = []
    listwi = []
    listui = []
    n = len(listyi)

    for i in range(n):
        listmi.append(calc_mid_sum(listli[i], listbi[i]))

    for i in range(n):
        listwi.append(calc_time_await_mid(listli[i], listyi[i]))

    for i in range(n):
        listui.append(calc_time_into_mid(listmi[i], listyi[i]))

    print("Среднее число заявок, пребывающих в каждой из систем сети.")
    print(listmi)

    print("Среднее время ожидания заявки в очереди системы.")
    print(listwi)

    print("Среднее время пребывания заявок в системах.")
    print(listui)

    print("Среднее число заявок, ожидающих обслуживания в СМО:")
    print(sum(listli))

    print("Среднее число заявок, пребывающих в сети")
    print(sum(listmi))

    print("Среднее время ожидания заявки в сети")
    print(sum(listwi))

    print("Среднее время пребывания заявок в сети:")
    print(sum(listui))
