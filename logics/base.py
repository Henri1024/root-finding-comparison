import numpy as np
import math

class Formula:
    def __init__(self):
        self._errors = []
        self._xrs = []

    def set_exe_time(self, time_taken):
        self._exe_time = time_taken

    def get_exe_time(self):
        return self._exe_time

    def get_errors(self):
        return self._errors

    def get_xrs(self):
        return self._xrs

    def append_errors(self, error):
        self._errors.append(error)

    def append_xrs(self, xr):
        self._xrs.append(xr)

    def set_function(self, f):
        self._f = f

    def f(self, val):
        exe = self.get_function()
        exe = exe.replace('x',str(val))
        
        return eval(exe)

    def get_function(self):
        return self._f

    def generate_error(self, val1, val2):
        return abs(((val1*1.0-val2*1.0)/val1*1.0) * 100.0)

    def reset(self):
        self._exe_time = 0
        self._xrs = []
        self._errors = []

    def set_total_iter(self, iter):
        self._iter = iter

    def get_total_iter(self):
        return self._iter

