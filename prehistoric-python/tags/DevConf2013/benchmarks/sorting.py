from proust.benchmark import Benchmark
from proust.suite import Suite
import random

keys = list(range(10000))
listset = random.sample(keys, 2000)
setset = set(listset)
dictset = dict([(x, None) for x in setset])
checks = random.sample(keys, 2000)
dupset = listset + checks

def sort_f():
    l = list(setset)
    l.sort()
    return l
      
def sorted_f():
    return sorted(setset)

def sort_list_f():
    l = listset[:]
    l.sort()
    return l
      
def sorted_list_f():
    l = listset[:]
    return sorted(l)


sort_b = Benchmark(sort_f, description = "sort")
sorted_b = Benchmark(sorted_f, description = "sorted")

suite = Suite([sort_b, sorted_b])

sort_list_b = Benchmark(sort_list_f, description = "sort")
sorted_list_b = Benchmark(sorted_list_f, description = "sorted")

suite2 = Suite([sort_list_b, sorted_list_b])
