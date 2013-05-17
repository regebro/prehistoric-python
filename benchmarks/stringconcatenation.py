from proust.benchmark import Benchmark
from proust.suite import Suite

try:
    xrange = xrange
except NameError:
    xrange = range

strings = ['A' * x for x in xrange(1000)]

def simple_f():
    for x in range(1000):
        s = strings[x] + strings[-x-1]

simple_b = Benchmark(simple_f, description = "Simple concatenation: s = s1 + s2")

def join_f():
    for x in range(1000):
        s = "".join((strings[x], strings[-x-1]))

join_b = Benchmark(join_f, description = "Joining two strings: s1 = ''.join((s1, s2))")

def oldformat_f():
    for x in range(1000):
        s = "%s%s" % (strings[x], strings[-x-1])
    
oldformat_b = Benchmark(oldformat_f, description = "Old formatting: s1 = '%s%s' % (s1, s2)")
     
def newformat_f():
    for x in range(1000):
        s = "{0}{1}".format(strings[x], strings[-x-1])

newformat_b = Benchmark(newformat_f, description = "New formatting: s1 = '{0}{1}'.format(s1, s2)")

suite = Suite([simple_b, join_b, oldformat_b, newformat_b])