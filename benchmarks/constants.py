from proust.benchmark import Benchmark
from proust.suite import Suite
import random

try:
    xrange = xrange
except NameError:
    xrange = range

var = 3.5

def real_constant_outside_f():
    const = 5 * 3.5
    f = 0
    for x in xrange(10000):
        f += const

def real_constant_inside_f():
    f = 0
    for x in xrange(10000):
        f += 5 * 3.5

def real_constant_division_outside_f():
    const = 5 / 3.5
    f = 0
    for x in xrange(10000):
        f += const

def real_constant_division_inside_f():
    f = 0
    for x in xrange(10000):
        f += 5 / 3.5

def pseudo_constant_outside_f():
    const = 5 * var
    f = 0
    for x in xrange(10000):
        f += x * const

def pseudo_constant_inside_f():
    f = 0
    for x in xrange(10000):
        f += x * (5 * var)

def pseudo_constant_power_outside_f():
    const = 5 ** var
    f = 0
    for x in xrange(10000):
        f += x * const

def pseudo_constant_power_inside_f():
    f = 0
    for x in xrange(10000):
        f += x * (5 ** var)

def variation_f():
    f = len(xrange(10000)) * 17.5

real_constant_outside_b = Benchmark(real_constant_outside_f, description = "multiplication outside loop")
real_constant_inside_b = Benchmark(real_constant_inside_f, description = "multiplication inside loop")
real_constant_division_outside_b = Benchmark(real_constant_division_outside_f, description = "division outside loop")
real_constant_division_inside_b = Benchmark(real_constant_division_inside_f, description = "division inside loop")
pseudo_constant_outside_b = Benchmark(pseudo_constant_outside_f, description = "var multiplication outside loop")
pseudo_constant_inside_b = Benchmark(pseudo_constant_inside_f, description = "var multiplication inside loop")
pseudo_constant_power_outside_b = Benchmark(pseudo_constant_power_outside_f, description = "var power outside loop")
pseudo_constant_power_inside_b = Benchmark(pseudo_constant_power_inside_f, description = "var power inside loop")
variation_b = Benchmark(variation_f, description='non-stupid')

suite = Suite([
#    real_constant_outside_b,
#    real_constant_inside_b,
#    real_constant_division_outside_b,
    real_constant_division_inside_b,
    pseudo_constant_outside_b,
    pseudo_constant_inside_b,
    pseudo_constant_power_outside_b,
    pseudo_constant_power_inside_b,
#    variation_b,
])
