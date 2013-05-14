:css: css/stylesheet.css
:skip-help: true
:title: Prehistoric Patterns in Python

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

SORTING WITH CMP
================

.. code:: python

    return sorted(catalog_sequence, lambda x: x.modified())


----

DICTS OF MUTABLES
=================

.. code:: python

    seen = {}
    
    if key in seen:
        seen[key].add(value)
    else:
        seen[key] = set([value])


.. class:: ref

    Django-1.5.1: django/db/models/sql/query.py

----

DICTS OF MUTABLES
=================

Since Python 2.5 we can now use a `defaultdict`.

.. code:: python

    from collections import defaultdict

    seen = defaultdict(set)
    
    seen[key].add(value)

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
