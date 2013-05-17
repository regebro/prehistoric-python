from proust.benchmark import Benchmark
from proust.suite import Suite

try:
    xrange = xrange
except NameError:
    xrange = range

a = "aaaaaaaaaaaaaaaaa"

def simple_f():
    b = ''
    for x in range(10000):
        b = b + a

simple_b = Benchmark(simple_f, description = "Simple concatenation: s = s1 + s2")
     

def join_f():
    l = []
    for x in range(10000):
        l.append(a)
    b = ''.join(a)

join_b = Benchmark(join_f, description = "Joining two strings: s1 = ''.join((s1, s2))")

suite = Suite([simple_b, join_b])