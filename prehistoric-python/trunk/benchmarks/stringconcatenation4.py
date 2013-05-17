from proust.benchmark import Benchmark
from proust.suite import Suite

try:
    xrange = xrange
except NameError:
    xrange = range

strings = ['A' * x for x in xrange(1000)]

def add_two_f():
    for x in range(999, -1, -1):
        b = strings[9] + strings[20]

add_two_b = Benchmark(add_two_f, description = "Adding 2")
     

def join_two_f():
    l = []
    for x in range(999, -1, -1):
        b = ''.join((strings[9], strings[20]))

join_two_b = Benchmark(join_two_f, description = "Joining 2")


def add_three_f():
    for x in range(999, -1, -1):
        b = strings[999] + strings[20] + strings[14]

add_three_b = Benchmark(add_three_f, description = "Adding 3")


def join_three_f():
    l = []
    for x in range(999, -1, -1):
        b = ''.join((strings[999], strings[20], strings[14]))

join_three_b = Benchmark(join_three_f, description = "Joining 3")



def add_four_f():
    for x in range(999, -1, -1):
        b = strings[999] + strings[20] + strings[14] + strings[200]

add_four_b = Benchmark(add_four_f, description = "Adding 4")


def join_four_f():
    l = []
    for x in range(999, -1, -1):
        b = ''.join((strings[999], strings[20], strings[14], strings[200]))

join_four_b = Benchmark(join_four_f, description = "Joining 4")


def add_ten_f():
    for x in range(999, -1, -1):
        b = strings[999] + strings[20] + strings[14] + strings[200] + strings[234] + strings[9] + strings[40] + strings[5] + strings[120] + strings[123]

add_ten_b = Benchmark(add_ten_f, description = "Adding 4")


def join_ten_f():
    l = []
    for x in range(999, -1, -1):
        b = ''.join((strings[999], strings[20], strings[14], strings[200], strings[234], strings[9], strings[40], strings[5], strings[120], strings[123]))

join_ten_b = Benchmark(join_ten_f, description = "Joining 4")


suite = Suite([add_two_b, join_two_b, add_three_b, join_three_b, add_four_b, join_four_b, add_ten_b, join_ten_b])