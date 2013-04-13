#!env python

from timeit import default_timer as timer

# String length, iterations
tests = (
#     (1, 100000),
#     (50, 10000),
#     (1000, 1000),
#     (100000, 100),
     (100000, 50),
     (10000000, 1),
     (10000000, 5),
     (10000000, 2),
)

results = {}
     
if 'xrange' not in locals():
     xrange = range

for strlen, count in tests:
     results[strlen, count] = []
     
     s1 = 'X'* strlen
     s2 = 'X'* strlen
     print("Simple concatenation: s1 = s1 + s2")
     start = timer()
     
     for i in xrange(count):
          s1 = s1 + s2

     time = timer() - start
     assert(len(s1) == strlen*(count+1))
     print('Time for {} concats of {} length strings = {:0.3f}'.format(count, strlen, time))
     results[strlen, count].append(time)


     s1 = 'X'* strlen
     s2 = 'X'* strlen
     print("Concatenate and assign: s1 += s2")
     start = timer()
     
     for i in xrange(count):
          s1 += s2

     time = timer() - start
     assert(len(s1) == strlen*(count+1))
     print('Time for {} concats of {} length strings = {:0.3f}'.format(count, strlen, time))
     results[strlen, count].append(time)


     s1 = 'X'* strlen
     s2 = 'X'* strlen
     print("Joining two strings: s1 = ''.join((s1, s2))")
     start = timer()
     
     for i in xrange(count):
          s1 = ''.join((s1, s2))

     time = timer() - start
     assert(len(s1) == strlen*(count+1))
     print('Time for {} concats of {} length strings = {:0.3f}'.format(count, strlen, time))
     results[strlen, count].append(time)


     s1 = 'X'* strlen
     s2 = 'X'* strlen
     print("Looking up the join function outside the loop: s1 = j((s1, s2))")
     start = timer()
     
     j = ''.join
     for i in xrange(count):
          s1 = j((s1, s2))

     time = timer() - start
     assert(len(s1) == strlen*(count+1))
     print('Time for {} concats of {} length strings = {:0.3f}'.format(count, strlen, time))
     results[strlen, count].append(time)


     s1 = 'X'* strlen
     s2 = 'X'* strlen
     print("Making a list of strings and joining after the loop: s1 = ''.join(l)")
     start = timer()
     
     l = [s1]
     for i in xrange(count):
          l.append(s2)
     s1 = ''.join(l)

     time = timer() - start
     assert(len(s1) == strlen*(count+1))
     print('Time for {} concats of {} length strings = {:0.3f}'.format(count, strlen, time))
     results[strlen, count].append(time)


     s1 = 'X'* strlen
     s2 = 'X'* strlen
     print("Old formatting: s1 = '%s%s' % (s1, s2)")
     start = timer()
     
     for i in xrange(count):
          s1 = '%s%s' % (s1, s2)
     
     time = timer() - start
     assert(len(s1) == strlen*(count+1))
     print('Time for {} concats of {} length strings = {:0.3f}'.format(count, strlen, time))
     results[strlen, count].append(time)


     s1 = 'X'* strlen
     s2 = 'X'* strlen
     print("New formatting: s1 = '{0}{1}'.format(s1, s2)")
     start = timer()
     
     for i in xrange(count):
          s1 = '{0}{1}'.format(s1, s2)
     
     time = timer() - start
     assert(len(s1) == strlen*(count+1))
     print('Time for {} concats of {} length strings = {:0.3f}'.format(count, strlen, time))
     results[strlen, count].append(time)

from pprint import pprint
pprint(results)