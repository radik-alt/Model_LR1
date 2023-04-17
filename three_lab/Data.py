import numpy as np

class Data:

    def __init__(self, arr):
        self.arr = arr
        self.mean = np.mean(self.arr)
        self.dis = np.var(self.arr)
        self.otkl = np.std(self.arr)

    def __repr__(self):
        return f"Мат ожидание:{self.mean}, Дисперсия:{self.dis}, Ср кв отклонение:{self.otkl}, Интенсивность:{1 / self.mean}"
