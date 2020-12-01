from .base import Formula
import time


def current_milli_time(): return int(round(time.time() * 1000))


class Secant(Formula):
    def __init__(self):
        self._errors = []
        self._xrs = []

    def generate_next(self, x0, x1):
        fx1 = self.f(x1)
        return x1 - (fx1 * (x1-x0)) / (fx1 - self.f(x0))

    def compute(self, xi, xu, es):
        self.reset()
        start = current_milli_time()

        iter = 1

        x0, x1 = xi, xu
        ea = 100
        while ea > es:
            xi = self.generate_next(x0, x1)

            if iter > 1:
                ea = self.generate_error(xi, x1)

            self.append_xrs(xi)
            self.append_errors(ea)

            x0, x1 = x1, xi
            iter += 1
        self.set_total_iter(iter)
        time_taken = current_milli_time()-start
        for i in range(5):
            self.set_exe_time(time_taken)
