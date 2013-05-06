from __future__ import with_statement
import sys
from timeit import default_timer as timer

try:
    implementation = sys.implementation.name
except AttributeError:
    implementation = sys.subversion[0]
    
platform = '%s %s' % (implementation, '.'.join(str(x) for x in sys.version_info[:3]))

# String length, iterations

variations = (
     #(10, 10000),
     #(100, 1000),
     #(1000, 100),
     #(10000, 10),
     (100000, 1),
)

results = {}
     
if 'xrange' not in locals():
    xrange = range

from zatapathique import Benchmark

class SimpleConcat(Benchmark):
    description = "Simple concatenation: s1 = s1 + s2"
     
    def test(self, count, strlen):
        s1 = 'X'* strlen
        s2 = 'X'* strlen
        for i in xrange(count):
            s1 = s1 + s2

class ConcateAndAssign(Benchmark):
    description = "Concatenate and assign: s1 += s2"
     
    def test(self, count, strlen):
        s1 = 'X'* strlen
        s2 = 'X'* strlen
        for i in xrange(count):
            s1 += s2

class Join(Benchmark):
    description = "Joining two strings: s1 = ''.join((s1, s2))"
     
    def test(self, count, strlen):
        s1 = 'X'* strlen
        s2 = 'X'* strlen
        for i in xrange(count):
            s1 = ''.join((s1, s2))

class OutsideJoin(Benchmark):
    description = "Looking up join first: s1 = j((s1, s2))"
     
    def test(self, count, strlen):
        s1 = 'X'* strlen
        s2 = 'X'* strlen
        j = ''.join
        for i in xrange(count):
            s1 = j((s1, s2))

class JoinAfter(Benchmark):
    description = "Making a list of strings and joining after the loop: s1 = ''.join(l)"
     
    def test(self, count, strlen):
        s1 = 'X'* strlen
        s2 = 'X'* strlen
        l = [s1]
        for i in xrange(count):
            l.append(s2)
        s1 = ''.join(l)

class OldFormat(Benchmark):
    description = "Old formatting: s1 = '%s%s' % (s1, s2)"
     
    def test(self, count, strlen):
        s1 = 'X'* strlen
        s2 = 'X'* strlen
        for i in xrange(count):
            s1 = '%s%s' % (s1, s2)

class NewFormat(Benchmark):
    description = "New formatting: s1 = '{0}{1}'.format(s1, s2)"
     
    def test(self, count, strlen):
        s1 = 'X'* strlen
        s2 = 'X'* strlen
        for i in xrange(count):
            s1 = '{0}{1}'.format(s1, s2)
            
tests = [SimpleConcat(), ConcateAndAssign(), Join(), OutsideJoin(), JoinAfter(), OldFormat()]
if sys.version >= '2.6':
    tests.append(NewFormat())

for strlen, count in variations:
    for test in tests:
        print("Running test %s %s times with string length %s" % (test.description, count, strlen) )
        test.warmup()
        test.run(count=count, strlen=strlen)
    
    
with open('results.csv', 'at') as outfile:
    for test in tests:
        print(test)
        test.save(outfile)
    