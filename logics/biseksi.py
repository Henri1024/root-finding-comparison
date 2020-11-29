from .base import Formula
import time

class Biseksi(Formula):
    def __init__(self):
        self._errors = []
        self._xrs = []

    def generate_xr(self, xi, xu):
        return (xi+xu)/2
    
    def compute(self, xi, xu, es):
        self.reset()
        start = time.time_ns()


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
                iter +=1
        self.set_total_iter(iter)
        self.set_exe_time(time.time_ns()-start)

