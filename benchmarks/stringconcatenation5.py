from proust.benchmark import Benchmark
from proust.suite import Suite

try:
    xrange = xrange
except NameError:
    xrange = range

uchar = u'A'
bchar = uchar.encode('ascii')
stringies = [uchar * x for x in xrange(1000)]
byties = [bchar * x for x in xrange(1000)]

def simple_b_f():
    s = u''.encode('ascii')
    for x in xrange(999, -1, -1):
        f = byties[x]
        s = s + f

simple_b_b = Benchmark(simple_b_f, description = "Simple byte concatenation: s1 = s1 + s2")


def simple_u_f():
    s = u''
    for x in xrange(999, -1, -1):
        f = stringies[x]
        s = s + f

simple_u_b = Benchmark(simple_u_f, description = "Simple unicode concatenation: s1 = s1 + s2")

def join_b_f():
    j = u''.encode('ascii')
    s = j.join(byties)

join_b_b = Benchmark(join_b_f, description = "Joining a byte list: s1 = ''.join(l)")

def join_u_f():
    j = u''
    s = j.join(stringies)

join_u_b = Benchmark(join_u_f, description = "Joining a byte list: s1 = ''.join(l)")

suite = Suite([simple_b_b, join_b_b, simple_u_b, join_u_b])
