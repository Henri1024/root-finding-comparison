from .base import Formula
import time


def current_milli_time(): return int(round(time.time() * 1000))


class Biseksi(Formula):
    def __init__(self):
        self._errors = []
        self._xrs = []

    def generate_xr(self, xi, xu):
        return (xi+xu)/2

    def compute(self, xi, xu, es):
        self.reset()
        start = current_milli_time()

        ea = 100.0
        iter = 1
        xr_last = 100

        if self.f(xi) * self.f(xu) >= 0:
            raise NameError("Nilai f(xi) * f(xu) tidak negatif")
        else:
            while ea > es:
                xr = self.generate_xr(xi, xu)
                fxr = self.f(xr)

                if self.f(xi)*fxr < 0:
                    xu = xr
                elif self.f(xi)*fxr > 0:
                    xi = xr

                if iter > 1:
                    ea = self.generate_error(xr, xr_last)
                self.append_errors(ea)
                self.append_xrs(xr)

                xr_last = xr
                iter += 1
        self.set_total_iter(iter)

        time_taken = current_milli_time()-start
        for i in range(5):
            self.set_exe_time(time_taken)
