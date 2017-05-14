:css: css/stylesheet.css
:skip-help: true
:title: Prehistoric Patterns in Python
:auto-console: false

.. header::

    .. image:: images/shoobx.png

----

Prehistoric Patterns in Python
==============================

.. class:: name

    Lennart Regebro

PyCon US 2017, Portland

.. note::

    Hi! So yes, I'm Lennart, I've been working with Python fulltime since 2001.
    Most of the time with web development.

----

.. note::

    I work for Boston company Shoobx. We make a webapp that
    anyone with a corporation should use, especially startups.
    I'm not gonna bore you with what we do, it's legal stuff, but if you work
    for a startup tell the bosses about us, they'll love us.

----

.. image:: images/magda_elenor.jpg
    :class: left
    :width: 70%

.. image:: images/elenor_quince.jpg
    :class: right
    :width: 29.5%

.. image:: images/cats.jpg
    :class: left
    :width: 50%

.. image:: images/quince.jpg
    :class: right
    :width: 50%

.. note::

    I'm born in Swedish occupied territor, but I live in Poland, with my
    wife, daughter, cats and fruit trees. But enough about me!

    This talk is going to be about old code patterns, both real and mythical!

    Because the standard patterns in Python has changed throughout time,
    as Python gained more features. But there is loads of old code out there,
    so I will try to explain why that old code looks like it does, and why
    you should change it.

----

.. image:: images/django.png

.. class:: ref

    Photo: Reinout van Rees

.. note::

    And old does not mean unmaintained. If you wrote a library that needed to
    support Python 2.4 old patterns may very well remain, because they still
    work. I did a shorter version of this talk on a Django Con EU a few years
    back, typically using examples from what was then the latest version of
    Django, because Django once supported Python 2.4.

    But don't look for those patterns in Django now. By the end of the talk
    the Django maintainers had pushed fixes for most of them. :-)

    And it's also easy to just keep going with your old code patterns even
    when they aren't needed, so often new code uses old patterns as well,
    because that's what the programmer is used to. Us old programmers are
    extra susceptible to this.

    And, old tutorials and old books have old patterns. And people keep using
    them.

    Let's start!

----

.. code:: python

    if mydict.has_key(x):

.. note::

    OK, firstly, stop doing this.

----

.. code:: python

    if x in mydict:

.. note::

    This has been the norm since Python 2.2. It's been 15 years. has_key
    doesn't even exist in Python 3. Stop using has_key() on dictionaries. And
    you probably think I'm silly for mentioning this. Let me present to you,
    github!

----

.. image:: images/has_key_usage_1.png

.. image:: images/has_key_usage_2.png


.. note::

    Yes, when you search for this on github, has_key tends to show up in
    commits about every five minutes or so.

----

.. image:: images/has_key_commit_1.png
    :width: 100%

.. note::

    I even found this! But don't worry, the actual commit replaces has_key
    with in. It's just the commit message that is backwards.

----

.. code:: python

    for x in mydict.keys():

.. note::

    And this isn't that much better.

----

.. image:: images/keys_usage_1.png

.. note::

    This is way less common than has_key, but still happens.
    In fact, if you are using the keys() method at all,
    you are probably doing it wrong.

----

.. code:: python

    keys = mydict.keys()


.. note::

    This is also fairly common. But...

----

.. code:: python

    keys = list(mydict)

.. note::

    This is nicer if you want a list.

----

.. code:: python

    eater = iter(mydict)

.. note::

    And if you want an iterator, this is the way to do it. In addition the
    keys method has different results in Python 2.7 and Python 3, but list()
    and iter() has the same result.

    OK, enough about dictionaries, now let's talk about sets!

----

Sets
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

.. code:: python

    d = {}
    for each in list_of_things:
        d[each] = None

    list_of_things = d.keys()

.. note::

    Yes! Dictionary keys! So in fact I lied, this pattern isn't about sets,
    it's also about dictionaries!

    This code example makes a list unique by putting it into a dictionary
    as keys with a value of None, and then getting a list of keys back.


----

.. code:: python

    list_of_things = set(list_of_things)

.. note::

    Today you would just do this instead.

    Another usage of dictionary keys like this is when you wanted to do very
    fast lookups. Checking if a value exists in a dictionary is way faster
    than checking if it exists in a list.

----

``dicts`` vs ``lists``
======================

+------------+-----+
| Python 2.7 | 45x |
+------------+-----+
| Python 3.6 | 60x |
+------------+-----+
| PyPy2 5.4  | 35x |
+------------+-----+
| PyPy3 5.5  | 35x |
+------------+-----+

.. note::

    This is simply looking if a value exists in a dictionary vs a list.
    Data is random integers, the set is 200 random integers. Yes, just 200.

    And as you see, dictionaries are *way* faster than lists. So it
    used to be a pattern that if you needed to do that a lot, you used
    a dictionary.

    And this means that if you are making a lookup to see if some values
    exist in a list, consider that maybe it should be a set instead.

----

``sets`` vs ``dicts``
=====================

+------------+-------+
| Python 2.7 | 1.05x |
+------------+-------+
| Python 3.6 | 1.05x |
+------------+-------+
| PyPy2 5.4  | 1.03x |
+------------+-------+
| PyPy3 5.5  | 1.01x |
+------------+-------+

.. note::

    And don't worry, sets are a little bit faster than dictionaries.

    OK, enough with dictionaries for real now. Now lets talk about sorting.

----

.. image:: images/cookbook1.png

.. note::

    Remember I mentioned old books and tutorials? Yeah, this is from the
    Python Cookbook as you can see. Probably 1st edition, from 2002. Why
    people commit it to Github in 2016 I don't know.

    Let's look at the code.

----

.. code:: python

    keys = os.environ.keys()
    keys.sort()
    for x in keys:
        print x,

.. note::

    We already talked about not using keys. But worse here is that it uses
    lists in-place-sorting sort() method. And that's because that was the only
    option in 2002. But since Python 2.4 we have the sorted() builtin.

----

.. code:: python

    for x in sorted(os.environ):
        print x,

.. note::

    Much better. Because less lines means less bugs.

    Even better would have been if we could use a list
    comprehension, of course. But we can't, because of the print statement.

    Or... can we?


----

:data-y: r800
:data-x: r-600

.. code:: python

    [print(x, end=' ') for x in sorted(os.environ)]

.. note::

    from __future__ import print_function

    Of course we can. Not that you would use that except for debugging, would
    you? That's OK, I won't judge you.

----

:data-y: r0
:data-x: r1200

.. image:: images/judge.jpg

[Yes I will]

.. note::

    OK, that was a small diversion, back to sorting, because we aren't done!

----

:data-y: r-800
:data-x: r-600

.. note::

    If you know that the iterable you are sorting is a list, you can sort it
    in place with .sort(). But in other cases you don't know it. And sorted()
    takes any iterable. It can be a list, or set or a generator. This makes
    the code more robust.

    Calling sort() on an existing list is a little bit faster than calling
    sorted on the list, as it ends up creating a new list. But the difference
    is very small, around 2%, less on PyPy.

----

:data-x: r1200
:data-y: 0

.. code:: python

    candidates.sort(lambda a, b: -cmp(a[1], b[1]))


.. note::

    The next old sorting pattern *is* all about speed.

    This code, from a book about Django and Javascript, uses the standard way
    of sorting a list by passing in a comparison function, in this case a
    lambda.

    comparison functions return 1, 0 or -1 to tell which item of the two is
    larger, so by sticking a minus first you get a reverse sort.

----

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

    Buuuut, the comparison function compares pairs, and the longer the list is,
    the more possible pairings is there.

    Jarret Hardie in the sadly defunct Python Magazine wrote an article on this
    and this is his numbers, and they sound reasonable. You see that long
    lists quickly gets very slow to sort.

----

.. code:: python

    candidates.sort(key=lambda a: a[1], reverse=True)

.. note::

    So therefore, a key argument to sort() and sorted() was introduced
    already in Python 2.4.

    The function now got much simpler, and has only one argument    .
    But how does the statistics look for how many calls the function gets?

----

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

    And the lambda only does one key lookup, not two, so we get 1/17th as
    many key lookups on a list with 40.000 items. This makes sorting much
    faster. 40.000 random integers take only around 20% of the time to sort.

    That's it for sorting.

----

:data-x: r1200

.. code:: python

    result = include_blank and blank_value or []

.. note::

    This looks like a logic expression, but it isn't. It's a sneaky
    conditonal! If means that if include_blank is True, then result
    gets set to blank_value other wise it's an empty list.

    But blank_value was a parameter. What if it is something that evaluates to
    false, like a None or an empty set?

    Yes: result will be an empty list, not what you pass in as blank_value.

----

.. code:: python

    result = blank_value if include_blank else []


.. note::

    This is the new syntax for one line conditionals. When I say "New" I mean
    since Python 2.5. The reason it was added so late is that Guido
    supposedly didn't want a one line conditional at all, and I agree it's
    not very readable, but his hand was forced, because people would make
    the sneaky conditionals instead.

----

.. code:: python

    t = database.start()
    try:
        try:
            t.insert(a_bunch_of_records)
            t.commit()
        except DatabaseException:
            log.exception("Something went wrong!")
            t.abort()
    finally:
        t.close()


.. note::

    Yeah, this also isn't very readable. It's a made up example, of course,
    no maintained code would still do this. But you might encounter it in
    some old app somewhere, and more problematic, there are still tutorials
    around that do things that are similar to this.

    And what the code does, is that it does resource handling. We make sure
    that the database transaction is aborted if something goes wrong, and
    that it's closed at the end.

    Context managers happened in Python 2.5 and try/except/finally also
    happened in 2.5. Before that you had to nest one try/except inside a
    try/finally, like this code, and it's those nested try statements that make
    this code ugly.

----

.. code:: python

    t = database.start()
    try:
        t.insert(a_bunch_of_records)
        t.commit()
    except DatabaseException:
        log.exception("Something went wrong!")
        t.abort()
    finally:
        t.close()

.. note::

    Already this is better.

----

.. code:: python

    with database.start() as t:
        try:
            t.insert(a_bunch_of_records)
            t.commit()
        except DatabaseException:
            log.exception("Something went wrong!")
            t.abort()

.. note::

    But of course, even better is with a context manager.
    I like context managers.

----

.. code:: python

    class MagicResource(object):

        def __del__(self):
            # deallocate the object!

.. note::

    Here's another example of something people did, especially influenced by
    Java and C++. This was never a good idea, as __del__ isn't guaranteed to
    be called. A context manager would be the solution instead.

    For the reason that it never was a good idea, I thought deallocating things
    in dunder del would be unusual.

----

.. image:: images/del_use1.png

.. note::

    Boy was I wrong.

----

.. code:: python

    self.assertRaises(DatabaseException, add_records,
                      arg1, arg2, keyword=True)

.. note::

    On the topic of context managers, unittests assertRaises is a
    contextmanager in 2.7 and later.

----

.. code:: python

    with self.assertRaises(DatabaseException):
        add_records(arg1, arg2, keyword=True)

.. note::

    So much nicer.

----

.. code:: python

    import tempfile

    with tempfile.TemporaryDirectory() as dir:
        # Do stuff

.. note::

    Also worth mentioning is that in Python 2.7 TemporaryFile and
    NamedTemporaryFile are context managers. And in Python 3.2 and later
    you also have TemporaryDirectory!

----

Stuck on Python 2?
==================
Sucks for you!
==============

.. note::

    Next: Generators.

----

.. code:: python

    def a_generator():
        for x in another_generator():
            yield x

.. note::

    Generators are awesome, I love generators. But this sort of code annoys
    me every time. Why do I have to write such stupid code?

----

.. code:: python

    def a_generator():
        yield from another_generator()

.. note::

    In Python 3.3 and later, I don't!

----

Stuck on Python 2?
==================
Sucks for you!
==============

.. note::

    On the topic of Generators, Python 3.7 will have a backwards incompatible
    change I thought I should mention.

----

.. code:: python

    def __next__(self):
        x = self.foo()
        if x == 0:
            raise StopIteration
        return x

.. note::

    Generators are a type of iterators, and iterators is any object with a
    __next__ method. You signal the end of the iteration by raising a
    StopIteration exception.

----

.. code:: python

    def testgen(x):
        while x < 100:
            if x == 31:
                raise StopIteration
            x += 1+x
            yield x

.. note::

    And so you should use StopIteration to stop the iteration ins a generator
    as well, right? They are after all just fancy iterators, or?

    Ah, well, no. This above does indeed work. But raising StopIteration in
    generators can under specific circumstance cause some obscure bugs.

----

PEP 479
=======

.. note::

    See PEP 479 if you want the details.

----

.. code::

    >>> list(testgen(0))
    RuntimeError: generator raised StopIteration

.. note::

    The end result is in any case that starting from Python 3.7, raising a
    StopIteration in a generator in fact raises a RuntimeError.

----

.. code:: python

    def testgen(x):
        while x < 100:
            if x == 31:
                return
            x += 1+x
            yield x

.. note::

    The correct way is to just return. Returning from a generator in fact
    raises StopIteration.

----

String Concatenation
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

The Misunderstanding
====================

This is slow:

.. code:: python

    result = ''
    for text in make_a_lot_of_text():
        result = result + text
    return result

----

The Misunderstanding
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

Many Copies
===========

.. code:: python

    result = ''
    for text in make_a_lot_of_text():
        result = result + text
    return result

----

:data-x: r-28
:data-y: r87
:data-scale: 0.5
:class: highlight concat1

----

:data-x: r1228
:data-y: 0
:data-scale: 1

ONE COPY!
=========

.. code:: python

    texts = make_a_lot_of_text()
    result = ''.join(texts)
    return result

----

:data-x: r-41
:data-y: r69
:data-scale: 0.5
:class: highlight concat2

----

:data-x: r1241
:data-y: 0
:data-scale: 1

The Misunderstanding
====================

.. code:: python

    self._leftover = bytes + self._leftover

.. note::

    This only copies each of the strings once.

----

:data-x: r1200
:data-y: 0
:data-scale: 1

The Misunderstanding
====================

.. code:: python

    self._leftover = b''.join([bytes, self._leftover])

.. class:: ref

Django 1.5.1: django/http/multipartparser.py, Line 355

.. note::

    This also copies the strings ony once, but it goes via
    creating a list. And creating that list also takes time.

----

When to Use What?
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

Closing Concatenation Conclusion
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

----

Constants and Loops
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

Outside vs Inside
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

Outside vs Inside
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

.. note:

    And it can be replaced with this. Which is about 250 times faster. Except
    on PyPy where it's just 10 times faster. Which is still twice as fast as
    Python 2.7.

    So, let us take some less stupid example.

----

Outside vs Inside
=================

.. code:: python

    const = 5 * a_var
    result = 0
    for each in some_iterable:
        result += each * const

.. note::

    Here the constant is "semi-constant" and we multiply with each item in
    the iterable. This makes more sense.

----

Outside vs Inside
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

Outside vs Inside
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

Thanks!
=======

Thanks to everyone who suggested outdated idioms, even if I didn't include them:

Radomir Dopieralski,
James Tauber,
Sasha Matijasic,
Brad Allen,
Antonio Sagliocco,
Doug Hellman,
Domen Kožar,
Christophe Simonis

Made with Hovercraft!
---------------------

----
