import random
import math


def generate_bernoulli_sample(n, p):

    values = [0, 1]  # множество значений (0 и 1)
    weights = [1 - p, p]  # вероятности соответствующих значений
    sample = random.choices(values, weights, k=n)  # генерация выборки
    return sample


def calculate_mean(sample):
    mean = sum(sample) / len(sample)
    return mean


def calculate_variance(sample, mean):

    variance = sum((x - mean) ** 2 for x in sample) / len(sample)
    return variance


def calculate_standard_deviation(variance):

    standard_deviation = math.sqrt(variance)
    return standard_deviation

def get_count(_list:list):
    count = 0
    for i in _list:
        if i == 1:
            count += i

    return count

if __name__ == "__main__":
    # Пример использования функций
    n = 100  # размер выборки
    p = 0.3  # вероятность успеха
    sample = generate_bernoulli_sample(n, p)
    print(sample)

    for i in range(0, 100, 10):
        print(get_count(sample[i:i+10]))

    mean = calculate_mean(sample)
    variance = calculate_variance(sample, mean)
    standard_deviation = calculate_standard_deviation(variance)

    print("Математическое ожидание: {:.2f}".format(mean))
    print("Дисперсия: {:.2f}".format(variance))
    print("Среднеквадратичное отклонение: {:.2f}".format(standard_deviation))
