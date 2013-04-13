Prehistoric Patterns in Python
==============================

0.  Don't <>

    From the Python 1.4 documentation:
    "<> and != are alternate spellings for the same operator. (I couldn't choose between ABC and C! :-)"
    Well, by 1.6 <> is marked as obsolescent.
    
Unless you are Barry Warsaw.

.. code::

    >>> from __future__ import barry_as_FLUFL
    >>> 1 != 2
      File "<stdin>", line 1
        1 != 2
           ^
    SyntaxError: invalid syntax
    >>> 1 <> 2
    True
    
    distribute-0.6.34-py2.7.egg/setuptools/command/easy_install.py:
    
        if k<>'target_version':
        
    Django-1.3.7/django/core/servers/basehttp.py:
    
        self._headers[:] = [kv for kv in self._headers if kv[0].lower()<>name]




1.  Don't concatenate strings by joining them
    CPython string concatenation is fast since (2.4)
    
    /Django-1.5.1/django/http/multipartparser.py:
    
        self._leftover = b''.join([bytes, self._leftover])
        
    Faster shorter simpler:
    
        self._leftover = bytes + self._leftover 
    
    Products.ATContentTypes-2.1.8-py2.6.egg/Products/ATContentTypes/browser/calendar.py:
        
        return ''.join((url, title, fingerprint))
        
    Thats' more sensible, but still, can't you just?:
        
        return url + title + fingerprint
    
    
    So when should you use join()? Whenever you are concatenating something that is an iterable.
    
    Don't concatenate in a loop. Append to a list, and ''.join() after.
    
    
    
2.  Don't sort things by putting them into a list
    Use sorted() (2.4)

    From Django-1.5.1/django/core/management/commands/makemessages.py
    
        retval = []
        for tn in template_names:
            retval.extend(search_python(python_code, tn))
        retval = list(set(retval))
        retval.sort()
        return retval

    The loop can't be a list comprehension, since each loop *extends*, so that part makes sense
    But better code would be:
    
        retval = []
        for tn in template_names:
            retval.extend(search_python(python_code, tn))
        return sorted(set(retval)))

    Even worse:
    Products.ATContentTypes-2.1.12-py2.7.egg/Products/ATContentTypes/tool/topic.py

        available = pcatalog.indexes()
        val = [field for field in available]
        val.sort()
        return val
    
    What does this do, and why? Well, I think the list comprehension is to make sure it's a list.
    I've looked through the code and even in 1999 pcatalog.indexes() returns just the keys() of a list,
    so it *is* a list, because this code does not run on Python 3. So I dont' know what that is about.

    Modern version:
    
        return sorted(pcatalog.indexes())
        
    Better eh?        


    
3.  Don't use cmp when sorting
    Use key (2.4)
    
    Here's a good one from Plone 4.0 (thankfully gone in Plone 4.1):
    Plone-4.0.10-py2.6.egg/Products/CMFPlone/skins/plone_scripts/sort_modified_ascending.py
    
        sorted = catalog_sequence[:]
        sorted.sort(lambda x, y: cmp(x.modified(), y.modified()))
        return sorted
        
    Which would be much faster with just:
    
        return sorted(catalog_sequence, lambda x: x.modified())
        
    catalog_sequence is a parameter that is passed in, so it doesn't want to
    modify it inplace, which is why it makes a copy.
    
    Django seems to have gotten rid of all cmp= even before 1.3. In Django
    1.5 you can't use it, because it doesn't work in Python 3.



4.  Don't handle resources with try/finally
    Use context managers (from __future__ import with_statement in 2.5)

    Django 1.5 is pretty good at doing this, and usually only does it when it's needed.
    For example with temporary files from tempfile. In Python 3, these files can be used as
    context managers, but not in Python 2.6.
    
    Django-1.5.1/django/contrib/sessions/backends/file.py

        output_file_fd, output_file_name = tempfile.mkstemp(dir=dir,
            prefix=prefix + '_out_')
        try:
            os.write(output_file_fd, self.encode(session_data).encode())
        finally:
            os.close(output_file_fd)

    Can now be:
    
        with tempfile.TemporaryFile(dir=dir, prefix=prefix + '_out_') as output_file:
            output_file.write(self.encode(session_data).encode())

6.  Don't use the string module for string methods.
   
    from string import lower >> str.lower

    Check: PyPY speed?    
    
      
7.  Don't do if x not in dict: dict[x] = []
    Use a defaultdict (2.5), or setdefault (2.0).
   
8.  Don't use has_key().

9.  Don't use `x == b and t or f`

10. Don't use type([]), type([]) etc.
    isinstance(x, collections.Sequence) is better.
   
11. Don't start octals with 0.
    They start with 0o now.
   
12. Don't use Set()

13. Don't calculate constants outside the loop.
    No need since CPython 2.5
   
14. Don't use dicts to replace sets.


Thanks to everyone who suggested outdated idioms, even if I didn't include them:

Radomir Dopieralski
James Tauber
Sasha Matijasic
Brad Allen
Antonio Sagliocco
Doug Hellman
Domen Kožar
Christophe Simonis
