import time


class MyRandom:

    def __init__(self, seed=None, a=1103515245, c=12345, m=2**31 - 1):
        self.a = a
        self.c = c
        self.m = m
        self.x = seed or int(time.time())

    def rand(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x / self.m

    def randrange(self, start, stop):
        r = self.rand() / self.m
        return start + int(r * (stop - start))
