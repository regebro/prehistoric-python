from proust.benchmark import Benchmark
from proust.suite import Suite

import string
import sys

try:
    xrange = xrange
except NameError:
    xrange = range

strings = ['A' * x for x in xrange(1000)]

def setup_u():
    return {'instr1': string.ascii_lowercase.decode(),
            'instr2': string.ascii_uppercase.decode()}

def simple_u_f(instr1, instr2):
    for x in xrange(10000):
        leftover = instr1 + instr2

simple_u_b = Benchmark(simple_u_f, setup=setup_u,
                       description="Simple concatenation: s = s1 + s2")

def join_u_f(instr1, instr2):
    for x in xrange(10000):
        leftover = u''.join((instr1, instr2))

join_u_b = Benchmark(join_u_f, setup=setup_u,
                     description="Joining two strings: s1=''.join((s1, s2))")

def oldformat_u_f(instr1, instr2):
    for x in xrange(10000):
        leftover = u"%s%s" %  (instr1, instr2)

oldformat_u_b = Benchmark(oldformat_u_f, setup=setup_u,
                          description="Old formatting: s1 = '%s%s' % (s1, s2)")

def newformat_u_f(instr1, instr2):
    for x in xrange(10000):
        leftover = u"{0}{1}".format(instr1, instr2)

newformat_u_b = Benchmark(newformat_u_f, setup=setup_u,
                          description="New formatting: s1 = '{0}{1}'.format(s1, s2)")

suite_u = Suite([oldformat_u_b, simple_u_b, join_u_b])


def setup_b():
    return {'instr1': string.ascii_lowercase.encode(),
            'instr2': string.ascii_uppercase.encode(),}

def simple_b_f(instr1, instr2):
    for x in xrange(10000):
        leftover = instr1 + instr2

simple_b_b = Benchmark(simple_b_f, setup=setup_b,
                       description="Simple concatenation: s = s1 + s2")

def join_b_f(instr1, instr2):
    for x in xrange(10000):
        leftover = ''.join((instr1, instr2))

join_b_b = Benchmark(join_b_f, setup=setup_b,
                     description="Joining two strings: s1=''.join((s1, s2))")

def oldformat_b_f(instr1, instr2):
    for x in xrange(10000):
        leftover = "%s%s" %  (instr1, instr2)

oldformat_b_b = Benchmark(oldformat_b_f, setup=setup_b,
                          description="Old formatting: s1 = '%s%s' % (s1, s2)")

suite_b = Suite([oldformat_b_b, simple_b_b, join_b_b,])

