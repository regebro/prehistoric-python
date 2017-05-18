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
unull = u''
bnull = unull.encode('ascii')


def simple_b_f():
    thelist = byties
    s = bnull
    for x in xrange(999, -1, -1):
        f = thelist[x]
        s = s + f

simple_b_b = Benchmark(simple_b_f, description = "Simple byte concatenation: s1 = s1 + s2")


def simple_u_f():
    thelist = stringies
    s = unull
    for x in xrange(999, -1, -1):
        f = thelist[x]
        s = s + f

simple_u_b = Benchmark(simple_u_f, description = "Simple unicode concatenation: s1 = s1 + s2")

def join_b_f():
    thelist = byties
    s = bnull
    s = s.join(thelist)

join_b_b = Benchmark(join_b_f, description = "Joining a byte list: s1 = b''.join(l)")


def join_u_f():
    thelist = stringies
    s = unull
    s = s.join(thelist)

join_u_b = Benchmark(join_u_f, description = "Joining a unicode list: s1 = u''.join(l)")

suite = Suite([simple_b_b, join_b_b, simple_u_b, join_u_b])
