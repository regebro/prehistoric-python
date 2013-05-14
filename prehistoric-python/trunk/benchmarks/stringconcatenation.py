from proust.benchmark import Benchmark
from proust.suite import Suite

strlen = 10000

s1 = 'X'* strlen
s2 = 'Y'* strlen

def simple_f():
    s = s1 + s2
    #s = 'X'* strlen + 'Y'* strlen

simple_b = Benchmark(simple_f, description = "Simple concatenation: s = s1 + s2")
     

def join_f():
    s = ''.join((s1, s2))

join_b = Benchmark(join_f, description = "Joining two strings: s1 = ''.join((s1, s2))")
     

def oldformat_f():
    s = '%s%s' % (s1, s2)

oldformat_b = Benchmark(oldformat_f, description = "Old formatting: s1 = '%s%s' % (s1, s2)")
     
def newformat_f():
    s = '{0}{1}'.format(s1, s2)

newformat_b = Benchmark(newformat_f, description = "New formatting: s1 = '{0}{1}'.format(s1, s2)")

suite = Suite([simple_b, join_b, oldformat_b, newformat_b])