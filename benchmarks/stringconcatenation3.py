from proust.benchmark import Benchmark
from proust.suite import Suite

try:
    xrange = xrange
except NameError:
    xrange = range

def setup_b():
    return {'null': u''.encode('ascii'),
            'char': u'A'.encode('ascii')}

def setup_u():
    return {'null': u'',
            'char': u'A',
            }


def add_two_f(char, null):
    result = null
    for x in xrange(1000):
        result = result + x * char

add_two_b_b = Benchmark(add_two_f, setup=setup_b,
                        description="Simple byte concatenation: s1 = s1 + s2")

add_two_u_b = Benchmark(add_two_f, setup=setup_u,
                        description="Simple unicode concatenation: s1 = s1 + s2")


def join_two_f(char, null):
    l = []
    for x in xrange(1000):
        l.append(x * char)

    result = null.join(l)

join_two_b_b = Benchmark(join_two_f, setup=setup_b,
                         description="Joining a byte list: s1 = ''.join(l)")

join_two_u_b = Benchmark(join_two_f, setup=setup_u,
                         description="Joining a unicode list: s1 = ''.join(l)")

suite = Suite([add_two_b_b, join_two_b_b, add_two_u_b, join_two_u_b])
