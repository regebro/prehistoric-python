:css: css/stylesheet.css
:skip-help: true
:title: Prehistoric Patterns in Python
:auto-console: false

----

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

On Afternoon 16:35, Friday 17th of May, 2013

----

DEFAULTDICT
===========

.. code:: python

    from collections import defaultdict

    data = defaultdict(set)
    
    data[key].add(value)

.. note::

   I'll start off with some patterns that center around dictionaries, and
   this first one is a fairly common pattern.
   
   When you have many values per key, so that every value in your dictionary should
   be a list or a set or a tuple or another dictionary, or in fact anything mutable,
   and you use, of course a defaultdict.
   
   Anyone who doesn't know how defaultdict works?
   
   Essentially, if you access a key that doesn't exist, it creates the key!
   But it only landed in Python in 2.5, so how did you do before this?

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
  

----

:data-x: r884
:data-y: r-129
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

  This looks of the key we are currently looking at exists in the dictionary.
  
----

:data-x: r92
:data-y: r34
:data-scale: 0.5
:class: highlight mutable2

.. note::

  And if it does, it adds the value to the existing set.

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

:data-x: r0
:data-y: r65
:data-scale: 0.5
:class: reveal

``Django-1.5.1: django/db/models/sql/query.py``
-----------------------------------------------


.. note::

    Yeah, Django 1.5.1.
    
    Why? Because the code once supported Python 2.4. It doesn't anymore
    but nobody has changed it. It works... It's definitely not a speed issue.
    
    Anybody here on Jython?
    

----

:data-x: r1000
:data-y: r-178
:data-scale: 1

SPEED
=====

``defaultdict vs add_to_dict()``
--------------------------------

CPython: 1.6x

PyPy: 1.2x

Jython 0.3x

----

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

    Yes! Dictionary keys!
    I could not, to my dissapointment find any examples of this in Django. :-)

----

SPEED
=====

dicts vs lists

Python 2.7: 40x

Python 3.3: 50x

PyPy 1.9: 200x

----

SPEED?
======

sets vs dicts

Python 2.7: 1.1x

Python 3.3: 1.05x

PyPy 1.9: 1.06x



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

Django 1.5.1: django/core/management/commands/makemessages.py

----

:data-x: r-266
:data-y: r-7
:data-scale: 0.5
:class: highlight sort1

----

:data-x: r293
:data-y: r70
:data-scale: 0.5
:class: highlight sort2

----

:data-x: r-127
:data-y: r35
:data-scale: 0.5
:class: highlight sort3

----

:data-x: r1100
:data-y: r-98
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

----

:data-x: r-197
:data-y: r99
:data-scale: 0.5
:class: highlight sort4

----

:data-x: r1197
:data-y: r-99
:data-scale: 1

SORTING
=======

.. code:: python

    retval = set()
    for tn in template_names:
        retval.update(search_python(python_code, tn))
    return sorted(retval)

----

:data-x: r-135
:data-y: r116
:data-scale: 0.5
:class: highlight sort5

----

:data-x: r1135
:data-y: r-116
:data-scale: 1

SORTING WITH CMP
================

.. code:: python

    sorted = catalog_sequence[:]
    sorted.sort(lambda x, y: cmp(x.modified(), y.modified()))
    return sorted
    
.. class:: ref

    Plone 4.0: Products/CMFPlone/skins/plone_scripts/sort_modified_ascending.py
    
----

:data-x: r1000
:data-y: r0
:data-scale: 1

SORTING WITH KEY
================

.. code:: python

    return sorted(catalog_sequence, lambda x: x.modified())

----

CONDITIONAL EXPRESSIONS
=======================

.. code:: python

    first_choice = include_blank and blank_choice or []
    

.. class:: ref

    Django-1.5.1: django/db/models/related.py

.. note::

    blank_choice is a parameter. What if it is something that evaluates to
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

STRING CONCATENATION
====================

**Prehistoric Claim:**

Don't use ``+``
---------------

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

THE MISUNDERSTANDING
====================

But this:

.. code:: python

    self._leftover = bytes + self._leftover
    
is not slower than this:

.. code:: python

    self._leftover = b''.join([bytes, self._leftover])
    
.. class:: ref

Django 1.5.1: django/http/multipartparser.py, Line 355

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

:data-x: r1025
:data-y: r-80
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

:data-x: r1035
:data-y: r-63
:data-scale: 1

INSERT BENCHMARKS HERE
======================

If I get that damn benchmarking module finished.


----

:data-x: r1000
:data-y: r0
:data-scale: 1

Foo

