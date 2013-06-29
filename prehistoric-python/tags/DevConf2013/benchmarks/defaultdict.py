from proust.benchmark import Benchmark
from proust.suite import Suite
from collections import defaultdict
import random

keys = list(range(1000))
dupes = random.sample(keys, 500)

def defaultdict_f():
    d = defaultdict(set)
    for k in keys:
        d[k].add(0)
    for k in dupes:
        d[k].add(0)
      
      
def add_to_dict(data, key, value):
    if key in data:
        data[key].add(value)
    else:
        data[key] = set([value])

def normaldict_f():
    d = {}
    for k in keys:
        add_to_dict(d, k, 0)
    for k in dupes:
        add_to_dict(d, k, 0)

defaultdict_b = Benchmark(defaultdict_f, description = "defaultdict")
normaldict_b = Benchmark(normaldict_f, description = "dict")

suite = Suite([defaultdict_b, normaldict_b])