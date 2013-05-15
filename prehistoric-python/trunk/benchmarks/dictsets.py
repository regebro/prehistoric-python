from proust.benchmark import Benchmark
from proust.suite import Suite
import random

keys = list(range(1000))
listset = random.sample(keys, 200)
setset = set(listset)
dictset = dict([(x, None) for x in setset])
checks = random.sample(keys, 200)

def dictset_f():
    for x in checks:
        x in dictset
      
def setset_f():
    for x in checks:
        x in setset

def listset_f():
    for x in checks:
        x in listset

dictset_b = Benchmark(dictset_f, description = "dictionary as set")
setset_b = Benchmark(setset_f, description = "set")
listset_b = Benchmark(listset_f, description = "list")

suite = Suite([dictset_b, setset_b, listset_b])