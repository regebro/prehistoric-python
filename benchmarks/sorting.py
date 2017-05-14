from proust.benchmark import Benchmark
from proust.suite import Suite
import random

keys = list(range(100000))
listset = random.sample(keys, 40000)
setset = set(listset)
dictset = dict([(x, None) for x in setset])
checks = random.sample(keys, 200)
dupset = listset + checks

def sort_f():
    l = list(setset)
    l.sort()
    return l

def sorted_f():
    return sorted(setset)

def thesetup():
    return {'l': listset[:]}

def sort_list_f(l):
    l.sort()
    return l

def sorted_list_f(l):
    return sorted(l)

cl = lambda a, b: -cmp(a*2, b*2)
kl = lambda a: a*2

def sort_cmp(l):
    l.sort(cmp=cl)

def sort_key(l):
    l.sort(key=kl)

sort_b = Benchmark(sort_f, description = "sort")
sorted_b = Benchmark(sorted_f, description = "sorted")

suite = Suite([sort_b, sorted_b])

sort_list_b = Benchmark(sort_list_f, description = "sort")
sorted_list_b = Benchmark(sorted_list_f, description = "sorted")

suite2 = Suite([sort_list_b, sorted_list_b])


cmp_b = Benchmark(sort_cmp, description = "cmp", setup=thesetup)
key_b = Benchmark(sort_key, description = "key", setup=thesetup)

suite3 = Suite([cmp_b, key_b])
