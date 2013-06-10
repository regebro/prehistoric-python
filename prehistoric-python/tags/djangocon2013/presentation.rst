:css: css/stylesheet.css
:skip-help: true
:title: Prehistoric Patterns in Python
:auto-console: true

----

:data-y: 0

.. class:: poster playfair bold pablo

PABLO FANQUE CIRCUS ROYAL,

.. class:: poster playfair warsaw

WARSAW, POLAND

.. class:: poster rye djangocon

DJANGOCON EU BONANZA

.. class:: poster chivo black positively

AND POSITIVELY THE

.. class:: poster playfair presentation

LAST PRESENTATION

.. class:: poster playfair counting

not counting the lightning talks

.. class:: poster chivo being bold

BEING FOR THE 

.. class:: poster chivo benefit bold

BENEFIT OF MR PONY

.. class:: poster diplomata prehistoric

PREHISTORIC

.. class:: poster diplomata  patterns

PATTERNS 

.. class:: poster diplomata python

IN PYTHON

.. class:: poster holtwood lennart

LENNART REGEBRO, ESQ.

.. class:: poster playfair celebrated

THE CELEBRATED PYTHON HUGGER!

.. class:: poster playfair plone black

PLONE DANCER, VAULTER, RIDER ETC.

.. class:: poster rye grandest

Grandest Night of the Season!

.. class:: poster playfair afternoon

On Afternoon 16:05, Friday 17th of May, 2013

.. note::

    Meine damen unt herren, mesdames et messieurs, ladies and gentlemen!
    Willkommen, bienvenue, welcome, to the positively last talk of DjangoCon
    Circus.
    
    And this is going to be about old code patterns, both real and mythical!
    
----

:data-x: 1200

DEFAULTDICT
===========

.. code:: python

    from collections import defaultdict

    data = defaultdict(set)
    
    data[key].add(value)

.. note::

   I'll start off with a patterns about dictionaries, and this one is a
   fairly common pattern.
   
   When you have many values per key, so that every value in your dictionary should
   be a list or a set or a tuple or another dictionary, or in fact anything mutable,
   you use a defaultdict.
   
   Essentially, if you access a key that doesn't exist, it creates the key!

----

:data-x: r-85
:data-y: r62
:data-scale: 0.5
:class: highlight defaultdict1

.. note::

    We create a defaultdict with in this case a set as the type of the
    values.

----

:data-x: r-21
:data-y: r67
:data-scale: 0.5
:class: highlight defaultdict2

.. note::

    And we can now rely on that any key we use exists, because if it
    doesn't, then the defaultdict will create a new set for that key.
    
    So we can just add to that key.
    
    But defaultdict only landed in Python in 2.5, so how did you do before this?  

----

:data-x: r1306
:data-y: 0
:data-scale: 1

DICTS OF MUTABLES
=================

.. code:: python

    if key in data:
        data[key].add(value)
    else:
        data[key] = set([value])

.. note::

    Well, you did your check manually.
   
----

:data-x: r-93
:data-y: r11
:data-scale: 0.5
:class: highlight mutable1

.. note::

  Does the key exist in the dictionary?
  
----

:data-x: r92
:data-y: r34
:data-scale: 0.5
:class: highlight mutable2

.. note::

  And if it does, add the value to the existing set.

----

:data-x: r28
:data-y: r68
:data-scale: 0.5
:class: highlight mutable3

.. note::

  But if it doesn't, it adds the key with a set as a value.

  Now, why do you need to know and recognize this pattern? It's outdated.
  You won't use it. It only exists in old unmaintained code, right?

  Well, I found this example here:
  
----

:data-x: r-27
:data-y: r65
:data-scale: 0.5
:class: reveal

``Django-1.5.1: django/db/models/sql/query.py``
-----------------------------------------------


.. note::

    Yeah, Django 1.5.1.
    
    Why? Because the code once supported Python 2.4. It doesn't anymore
    but nobody has changed it. It works...
    
    And I know what you think now, because I thought it! You think, maybe the
    clever core developers aren't using defaultdict because it's slow!
    
----

:data-x: r1200
:data-y: 0
:data-scale: 1

``defaultdict`` vs ``add_to_dict()``
====================================

+---------+------+
| CPython | 1.6x |
+---------+------+
| PyPy    | 1.2x |
+---------+------+
| Jython  | 0.3x |
+---------+------+

.. note::

    And it isn't. Except on Jython.

    Using a defaultdict is 1.6 times faster on CPython, 1.2 times on PyPy,
    and for some reason less three times as slow on Jython!
    
    I guess the Jython defaultdict implementation is very unoptimized.
    Using defaultdict is less code = less bugs and faster!

    OK, enough about dictionaries, now sets!

----

:data-x: r1200
:data-y: 0
:data-scale: 1

SETS
====

Unique values

Unordered

Fast lookup

.. note::

    Sets are useful, the values in a set must be unique, lookup in sets 
    are fast, although they aren't ordered.
    
    Sets first appeared as a standard library module in Python 2.3, and 
    as a built in type in Python 2.4.
    
    So what did you do before? What else do we have that has Unique values,
    fast lookup and no ordering?

----

SETS BEFORE SETS
================

.. code:: python

    d = {}
    for each in list_of_things:
        d[each] = None
        
    list_of_things = d.keys()

.. note::

    Yes! Dictionary keys! So in fact I lied, this pattern isn't about sets,
    it's about dictionaries too!
    
    This code example makes a list unique by putting it into a dictionary
    as keys with a value of None, and then getting a list of keys back.

    I could not, to my dissapointment find any examples of this in Django. :-)
    
    Another usage of dictionary keys like this is when you wanted to do very
    fast lookups. Checking if a value exists in a dictionary is way faster
    than checking if it exists in a list.

----

``dicts`` vs ``lists``
======================

+------------+------+
| Python 2.7 | 40x  |
+------------+------+
| Python 3.3 | 50x  |
+------------+------+
| PyPy 1.9   | 200x |
+------------+------+

.. note::

    This is simply looking if a value exists in a dictionary vs a list.
    Data is random integers.
    
    And as you see, dictionaries are *way* faster than lists. So it
    used to be a pattern that if you needed to do that a lot, you used
    a dictionary.
    
----

``sets`` vs ``dicts``
=====================

+------------+-------+
| Python 2.7 | 1.1x  |
+------------+-------+
| Python 3.3 | 1.05x |
+------------+-------+
| PyPy 1.9   | 1.06x |
+------------+-------+

.. note::

    However, sets are a little bit faster than dictionaries.
    
----

SORTING
=======

**Prehistoric code:**

.. code:: python

    retval = []
    for tn in template_names:
        retval.extend(search_python(python_code, tn))
    retval = list(set(retval))
    retval.sort()
    return retval


.. class:: ref

Django 1.5.1: extras/csrf_migration_helper.py

.. note::

    OK, enough with dictionaries for real now. Now lets talk about sorting.
    This code is also from Django 1.5.1.
    
----

:data-x: r-266
:data-y: r-5
:data-scale: 0.5
:class: highlight sort1

.. note::

    First it creates a list to return.
    
----

:data-x: r293
:data-y: r68
:data-scale: 0.7
:class: highlight sort2

.. note::

    The it fills that list with values.

----

:data-x: r-127
:data-y: r33
:data-scale: 0.5
:class: highlight sort3

.. note::

    And makes the list of values unique by converting it into a set, and
    then back into a list.
    
----

:data-x: r-152
:data-y: r52
:data-scale: 0.5
:class: highlight sort4

.. note::

    And lastly it sorts the list before returning it.
    
----

:data-x: r1452
:data-y: 0
:data-scale: 1

SORTING
=======

.. code:: python

    retval = set()
    for tn in template_names:
        retval.update(search_python(python_code, tn))
    retval = list(retval)
    retval.sort()
    return retval

.. note::

    Now of course, the first mistake in this code is to use a list in
    the first place. That's not a prehistoric pattern, I think it's just
    a mistake in the code in this case, likely the list(set()) call was
    added later than the main loop.
    
    Sure, updating lists are faster than updating sets, but first
    creating a long list and then making it a set is not faster than
    using a set from the start.
    
----

:data-x: r1200
:data-y: 0
:data-scale: 1

SORTING
=======

.. code:: python

    retval = set()
    for tn in template_names:
        retval.update(search_python(python_code, tn))
    return sorted(retval)

.. note::

    But the point here is this change. Instead of creating a list
    and then sorting it, you can now use sorted().

----

:data-x: r-149
:data-y: r114
:data-scale: 0.5
:class: highlight sort5

.. note::

    Because less lines means less bugs.
    
    Now in the earlier case we know that the variable was a list, because we
    just made the set into a list. But in other cases you don't know it.
    And sorted() takes any iterable. It can be a list, or set or a generator.
    This makes the code more robust.
    
    Calling sort() on an existing list is a little bit faster than calling
    sorted on the list, as it ends up creating a new list. But the difference
    is very small.
    
    
----

:data-x: r1349
:data-y: 0
:data-scale: 1

SORTING WITH CMP
================

.. code:: python

    sorted = catalog_sequence[:]
    sorted.sort(lambda x, y: cmp(x.modified(), y.modified()))
    return sorted
    
.. class:: ref

    Plone 4.0: Products/CMFPlone/skins/plone_scripts/sort_modified_ascending.py
    
.. note::

    The next old sorting pattern *is* all about speed. And this is nothing
    you will find in Django 1.5, because this doesn't even work under Python 3.
    
    So this example is from Plone, and in fact an old version of Plone, Plone 4.0.
    
----

:data-x: r-203
:data-y: r1
:data-scale: 0.5
:class: highlight cmp1

.. note::

    As you see here, this code first take a copy of the list, which is a good
    indication that this is old, this code is from the time when Plone still
    supported Python 2.3. Another indication is that it calls the copy "sorted".
    
    But I already covered sort() vs sorted(), for clarity I'll refactor this
    code to use sorted and also use a function instead of a lambda, because
    it's easier to read.
    
----

:data-x: r1403
:data-y: 0
:data-scale: 1

SORTING WITH CMP
================

.. code:: python

    def compare(x, y):
        return cmp(x.modified(), y.modified())
        
    return sorted(catalog_sequence, cmp=compare)

.. note::

    This is easier to read, but it has the same end-result.
    
----

:data-x: r27
:data-y: r45
:data-scale: 0.7
:class: highlight cmp2

.. note::

    And we see that the core of this is that it compares each object on the
    modification date.

    But since this uses a comparison method, it means it compares
    pairs of objects. And the longer the list is, the more pairs are possible!
    
----

:data-x: r1173
:data-y: 0
:data-scale: 1

AVERAGE # CALLS
===============

+--------+---------+----------+
| len(l) | # calls | Per item |
+--------+---------+----------+
| 4      | 6       | 1.5      |
+--------+---------+----------+
| 10     | 22      | 2.2      |
+--------+---------+----------+
| 100    | 528     | 5.28     |
+--------+---------+----------+
| 40,000 | 342,541 | 8.56     |
+--------+---------+----------+

.. class:: ref

    Reference: Jarret Hardie in Python Magazine

.. note::

    Reference: Jarret Hardie in Python Magazine

----

:data-x: r1200
:data-y: r0
:data-scale: 1

SORTING WITH KEY
================

.. code:: python

    def get_key(x):
        return x.modified()
        
    return sorted(key=get_key)

.. note::

    But also since Python 2.4 we can sort with a key function instead.

----

:data-x: r6
:data-y: r45
:data-scale: 0.5
:class: highlight cmp3

.. note::

    The function now got much simpler, and has only one call.
    But how does the statistics look for how many calls the function gets?
    
----

:data-x: r1194
:data-y: 0
:data-scale: 1

AVERAGE # CALLS
===============

+--------+---------+----------+
| len(l) | # calls | Per item |
+--------+---------+----------+
| 4      | 4       | 1        |
+--------+---------+----------+
| 10     | 10      | 1        |
+--------+---------+----------+
| 100    | 100     | 1        |
+--------+---------+----------+
| 40,000 | 40,000  | 1        |
+--------+---------+----------+

.. note::

    Yeah, you get exactly one call per item, always.
    With the earlier code, we get in average 680,000 calls to the
    modified() method when sorting 40.000 items. 
    
    Now we get 40,000 calls. That's 1/17th the amount of calls. Which
    essentially means that sorting 40,000 items takes just a tenth of the
    time.
    
----

:data-x: r1200

CONDITIONAL EXPRESSIONS
=======================

.. code:: python

    first_choice = include_blank and blank_choice or []
    

.. class:: ref

    Django-1.5.1: django/db/models/related.py

.. note::

    This looks like a logic expression, but it isn't. It's a sneaky
    conditonal! If means that if include_blank is True, then first_choice
    gets set to blank_choice other wise it's an empty list.

    But blank_choice is a parameter. What if it is something that evaluates to
    false, like a None or an empty set?
    
    Yes: first_choice will be an empty list, not what you pass in as blank_choice.
    
    In this example from Django, this is not an important issue, because a blank
    blank_choice makes no sense. But a blank blank_choice should really result in
    an error because explicit is better than implicit.

----

CONDITIONAL EXPRESSIONS
=======================

.. code:: python

    first_choice = blank_choice if include_blank else []
    
.. note::

    This is the new syntax for one line conditionals. When I say "New" I mean
    since Python 2.5.

----

CONSTANTS AND LOOPS
===================

.. code:: python

    const = 5 * 3.5
    result = 0
    for each in some_iterable:
        result += const
    

.. note::

    This is a pattern that was suggested to me that I should bring up.
    And I wasn't going to do it until I started benchmarking it.
    
    Here we see something simple, calculating a constant outside the loop.
    That should speed up the loop, right because you don't have to calculate
    the constant, right?

----

OUTSIDE VS INSIDE
=================

``5 * 3.5``
-----------

+------------+------+
| Python 2.4 | 2.0x |
+------------+------+
| Python 2.7 | 1.0x |
+------------+------+
| Python 3.3 | 1.0x |
+------------+------+
| PyPy 1.9   | 1.0x |
+------------+------+
| Jython 2.7 | 1.2x |
+------------+------+

.. note::

    Well, kinda. It used to be much faster, but since Python 2.5 it isn't.
    CPython will find that multiplication and calculate only once.
    In Jython it's still marginally faster to calculate it outside.
    
    PyPy of course is ridicolously fast with this code, it does this some
    30-40 times faster than Python 2.7.
    
----

OUTSIDE VS INSIDE
=================

``5 / 3.5``
-----------

+------------+------+
| Python 2.4 | 2.0x |
+------------+------+
| Python 2.7 | 2.0x |
+------------+------+
| Python 3.3 | 1.0x |
+------------+------+
| PyPy 1.9   | 1.0x |
+------------+------+
| Jython 2.7 | 1.2x |
+------------+------+

.. note::

    So if you have a division in the calculation, the Python 2.7 
    gets slow again! 
    
    Python 3.3 and PyPy are still fine, though.
    
    But of course, my example is stupid. 5 * 3.5 is actually 17.5, so when you
    have constants, you can simply change the code to the constant! Problem solved!
    
----

``result = len(some_iterable) * 17.5``
======================================

.. note:

    And it can be replaced with this. Which is about 250 times faster. Except
    on PyPy where it's just 10 times faster. Which is still twice as fast as
    Python 2.7.
    
    So, let us take some less stupid example. 
    
----

CONSTANTS AND LOOPS
===================

.. code:: python

    const = 5 * a_var
    result = 0
    for each in some_iterable:
        result += each * const

.. note::

    Here the constant is "semi-constant" and we multiply with each item in
    the iterable. This makes more sense.

----

OUTSIDE VS INSIDE
=================

``each * 5 * a_var``
--------------------

+------------+------+
| Python 2.4 | 1.3x |
+------------+------+
| Python 2.7 | 1.3x |
+------------+------+
| Python 3.3 | 1.3x |
+------------+------+
| PyPy 1.9   | 1.0x |
+------------+------+
| Jython 2.7 | 1.7x |
+------------+------+

.. note::

    Now the optimization dissappeared. Calculating the constant outside
    of the loop is now faster again.
    
    Except on PyPy which still succeeds in optimizing this.
    
----

OUTSIDE VS INSIDE
=================

``each * 5 ** a_var``
---------------------

+------------+------+
| Python 2.4 | 1.8x |
+------------+------+
| Python 2.7 | 2.0x |
+------------+------+
| Python 3.3 | 2.0x |
+------------+------+
| PyPy 1.9   | 33x  |
+------------+------+
| Jython 2.7 | 6.4x |
+------------+------+

.. note::

    Unless you use a power in the calculation of the constant,
    where PyPy's optimization also dissapears!
    
    On PyPy it's now 33 times faster to calculate this constant outside the loop!
    But still twice as fast as Python 2.7.
    
    So this pattern turns out not to be prehistoric at all!
    
    You *should* calculate constants outside of the loop.

----

STRING CONCATENATION
====================

.. code:: python

    self._leftover = b''.join([bytes, self._leftover])
    
.. class:: ref

Django 1.5.1: django/http/multipartparser.py, Line 355

.. note::

    And now, the prehistoric pattern that was the catalyst for this talk.

    You'll hear many people claiming that concatenating strings
    with + is slow, and that doing a join is faster.
    But, since CPython 2.5 there are optimizations in string
    concatenation, so now it is fast.
    
    But of course, not on PyPy. At least according to the PyPy
    people. Unless you have a compile time parameter, apparently.

    So let's look at the benchmarks.
    
----

``__add__`` vs ``.join``
========================

+------------+-------+
| Python 2.4 | 1.5x  |
+------------+-------+
| Python 2.7 | 1.4x  |
+------------+-------+
| Python 3.3 | 1.3x  |
+------------+-------+
| PyPy 1.9   | 1.0x  |
+------------+-------+
| Jython 2.7 | 1.8x  |
+------------+-------+

.. note::

    These benchmarks have been a big problem. It's been very hard to get
    something sensible, simple, that measures actual concatention, and
    doesn't get completely optimized away by PyPy.
    
    And this is the best I can do. It adds strings between 0 and 999
    characters long. There is overhead in the tests, but I believe that it's
    not enough to make a significant difference to the numbers.
    
    And you see that using addition to concatenate is faster.
    Even on Python 2.4!
    
    So where does this claim that join is faster come from?
    I think this is a big misunderstandning.
    
----

THE MISUNDERSTANDING
====================

This is slow:

.. code:: python

    result = ''
    for text in make_a_lot_of_text():
        result = result + text
    return result

----

THE MISUNDERSTANDING
====================

Much faster:

.. code:: python

    texts = make_a_lot_of_text()
    result = ''.join(texts)
    return result
    
----

``__add__`` vs ``.join``
========================

+------------+--------+
| Python 2.4 | 0.5x   |
+------------+--------+
| Python 2.7 | 0.5x   |
+------------+--------+
| Python 3.3 | 0.5x   |
+------------+--------+
| PyPy 1.9   | 1.0x   |
+------------+--------+
| Jython 2.7 | 0.004x |
+------------+--------+

----

MANY COPIES
===========

.. code:: python

    result = ''
    for text in make_a_lot_of_text():
        result = result + text
    return result

----

:data-x: r-25
:data-y: r80
:data-scale: 0.5
:class: highlight concat1

----

:data-x: r1225
:data-y: 0
:data-scale: 1

ONE COPY!
=========

.. code:: python

    texts = make_a_lot_of_text()
    result = ''.join(texts)
    return result
    
----

:data-x: r-35
:data-y: r63
:data-scale: 0.5
:class: highlight concat2

----

:data-x: r1235
:data-y: 0
:data-scale: 1

THE MISUNDERSTANDING
====================

.. code:: python

    self._leftover = bytes + self._leftover

.. note::

    This only copies each of the strings once.

----    

:data-x: r1200
:data-y: 0
:data-scale: 1

THE MISUNDERSTANDING
====================

.. code:: python

    self._leftover = b''.join([bytes, self._leftover])
    
.. class:: ref

Django 1.5.1: django/http/multipartparser.py, Line 355

.. note::

    This also copies the strings ony once, but it goes via
    creating a list. And creating that list also takes time.

----

WHEN TO USE WHAT?
=================

.. note::

    So if adding strings are fast when you are adding two strings, and
    joining is fast if you have many strings, where is the breakpoint?
    
    Well, it depends. It depends on how long your strings are and how many
    you have. With typical cases it seems join() is faster on CPython
    at somewhere around 4-5 strings.
    
    With PyPy up to ten strings are still as fast to use addition as to use
    join, and I stopped testing there because it was getting silly.
    
    
----

CLOSING CONCATENATION CONCLUSION
================================

.. note::

    I like alliteration. Can you tell?
    
    The conclusion is that you should do what feels natural. If the easiest
    way to concatenate a bunch of strings is by using +, then do that. If the
    strings you have are in a list or generated in a loop, then use join.

    And it's the same with calculating constants outside of the loop.
    It feels like it should be faster, and it often is. Python is such
    a fantastic language partly because what intuitively feels like the
    right thing to do, tends to in fact be the right thing to do.
    
    And on that bombshell, I say thank you for listening!
    
----

THANKS!
=======
