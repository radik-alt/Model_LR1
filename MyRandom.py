class MyRandom:

    current_value = 0.0

    def __init__(self, current_value):
        self.current_value = current_value

    def next(self) -> float:
        a = 214013
        b = 2531011
        m = 2**32

        self.current_value = (a * self.current_value + b) % m
        return self.current_value / m
