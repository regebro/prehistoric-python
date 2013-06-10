from proust.benchmark import Benchmark
from proust.suite import Suite

try:
    xrange = xrange
except NameError:
    xrange = range

strings = ['A' * x for x in xrange(1000)]

def simple_f():
    b = ''
    for x in range(999, -1, -1):
        b = b + strings[x]

simple_b = Benchmark(simple_f, description = "Simple concatenation: s1 = s1 + s2")
     

def join_f():
    l = []
    for x in range(999, -1, -1):
        l.append(strings[x])
    b = ''.join(l)

join_b = Benchmark(join_f, description = "Joining a list: s1 = ''.join(l)")


def extend_f():
    b = ''
    for x in range(999, -1, -1):
        b += strings[x]

extend_b = Benchmark(extend_f, description = "iadd: s1 += s2")

suite = Suite([simple_b, join_b, extend_b])