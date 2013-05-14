from proust.benchmark import Benchmark
from proust.suite import Suite

simple_b = Benchmark('s = "aaaaaaaaaaaaaaaaa" + "bbbbbbbbbbbbbb"', description = "Simple concatenation: s = s1 + s2")

join_b = Benchmark('s = "".join(("aaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbb"))', description = "Joining two strings: s1 = ''.join((s1, s2))")

oldformat_b = Benchmark('s = "%s%s" % ("aaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbb")', description = "Old formatting: s1 = '%s%s' % (s1, s2)")

newformat_b = Benchmark('s = "{0}{1}".format("aaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbb")', description = "New formatting: s1 = '{0}{1}'.format(s1, s2)")

suite = Suite([simple_b, join_b, oldformat_b, newformat_b])