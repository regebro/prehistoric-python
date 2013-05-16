from proust.benchmark import Benchmark
from proust.suite import Suite
import random

keys = list(range(10000))
listset = random.sample(keys, 2000)
setset = set(listset)
dictset = dict([(x, None) for x in setset])
checks = random.sample(keys, 2000)
dupset = listset + checks

def dictset_f():
    for x in checks:
        x in dictset
      
def setset_f():
    for x in checks:
        x in setset

def listset_f():
    for x in checks:
        x in listset

def inserting_set_f():
    s = set()
    for x in dupset:
        s.add(x)

def inserting_dict_f():
    s = list()
    for x in dupset:
        s.append(x)

def inserting_dict_and_making_set_f():
    s = list()
    for x in dupset:
        s.append(x)
    s = set(s)


dictset_b = Benchmark(dictset_f, description = "dictionary as set")
setset_b = Benchmark(setset_f, description = "set")
listset_b = Benchmark(listset_f, description = "list")
inserting_set_b = Benchmark(inserting_set_f, description = "inserting into set")
inserting_dict_b = Benchmark(inserting_dict_f, description = "appending into list")
inserting_dict_and_making_set_b = Benchmark(inserting_dict_and_making_set_f, description = "set(list)")

suite = Suite([dictset_b, setset_b, listset_b])
suite2 = Suite([inserting_set_b, inserting_dict_b, inserting_dict_and_making_set_b])