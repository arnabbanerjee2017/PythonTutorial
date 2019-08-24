Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 3
5
>>> 2+3
5
>>> 9-8
1
>>> 4*6
24
>>> 8/4
2.0
>>> 8 / 3
2.6666666666666665
>>> 8 // 3
2
>>> 5 / 2
2.5
>>> 5 / 0
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    5 / 0
ZeroDivisionError: division by zero
>>> (8 + 2) * 5
50
>>> 8 + 2 * 5
18
>>> 2 * 2 * 2 * 2
16
>>> 2 ** 8
256
>>> 2 ** 10 -1
1023
>>> 'arnab'
'arnab'
>>> "arnab"
'arnab'
>>> print('arnab')
arnab
>>> print("arnab")
arnab
>>> print("arnab's \"laptop\"")
arnab's "laptop"
>>> 'arnab' * 3
'arnabarnabarnab'
>>> 'arnab ' * 3
'arnab arnab arnab '
>>> print('c:\docs\arnab')
c:\docsrnab
>>> print(r'c:\docs\arnab')
c:\docs\arnab
>>> print('c:\docs\\arnab')
c:\docs\arnab
>>> x = 9
>>> y = 5
>>> x + y
14
>>> _ + 33
47
>>> name = 'arnab'
>>> name
'arnab'
>>> print(name)
arnab
>>> print(name, 'rocks')
arnab rocks
>>> _ + 'again
SyntaxError: EOL while scanning string literal
>>> print(name, 'rocks')
arnab rocks
>>> va = _ + ' again'
>>> print(va)
arnab again
>>> myList = ['arnab', 5.1, 98, 'KOLKATA']
>>> print(myList)
['arnab', 5.1, 98, 'KOLKATA']
>>> myList.reverse()
>>> print(myList)
['KOLKATA', 98, 5.1, 'arnab']
>>> tup = (1, 2, 3, 4)
>>> tup
(1, 2, 3, 4)
>>> print(tup)
(1, 2, 3, 4)
>>> myList[0] = 'arnab banerjee'
>>> print(myList)
['arnab banerjee', 98, 5.1, 'arnab']
>>> tup[0] = 10
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    tup[0] = 10
TypeError: 'tuple' object does not support item assignment
>>> len(tup)
4
>>> s = {1, 2, 3, 4}
>>> s = {111, 22, 3, 24}
>>> s
{24, 3, 22, 111}
>>> s
{24, 3, 22, 111}
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> main
No Python documentation found for 'main'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> module
No Python documentation found for 'module'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> modules

Please wait a moment while I gather a list of all available modules...

__future__          atexit              http                scrolledlist
__main__            audioop             hyperparser         search
_abc                autocomplete        idle                searchbase
_ast                autocomplete_w      idle_test           searchengine
_asyncio            autoexpand          idlelib             secrets
_bisect             base64              imaplib             select
_blake2             bdb                 imghdr              selectors
_bootlocale         binascii            imp                 setuptools
_bz2                binhex              importlib           shelve
_codecs             bisect              inspect             shlex
_codecs_cn          browser             io                  shutil
_codecs_hk          builtins            iomenu              signal
_codecs_iso2022     bz2                 ipaddress           site
_codecs_jp          cProfile            itertools           smtpd
_codecs_kr          calendar            json                smtplib
_codecs_tw          calltip             keyword             sndhdr
_collections        calltip_w           lib2to3             socket
_collections_abc    cgi                 linecache           socketserver
_compat_pickle      cgitb               locale              sqlite3
_compression        chunk               logging             squeezer
_contextvars        cmath               lzma                sre_compile
_csv                cmd                 macosx              sre_constants
_ctypes             code                macpath             sre_parse
_ctypes_test        codecontext         mailbox             ssl
_datetime           codecs              mailcap             stackviewer
_decimal            codeop              mainmenu            stat
_dummy_thread       collections         marshal             statistics
_elementtree        colorizer           math                statusbar
_functools          colorsys            mimetypes           string
_hashlib            compileall          mmap                stringprep
_heapq              concurrent          modulefinder        struct
_imp                config              msilib              subprocess
_io                 config_key          msvcrt              sunau
_json               configdialog        multicall           symbol
_locale             configparser        multiprocessing     symtable
_lsprof             contextlib          netrc               sys
_lzma               contextvars         nntplib             sysconfig
_markupbase         copy                nt                  tabnanny
_md5                copyreg             ntpath              tarfile
_msi                crypt               nturl2path          telnetlib
_multibytecodec     csv                 numbers             tempfile
_multiprocessing    ctypes              opcode              test
_opcode             curses              operator            textview
_operator           dataclasses         optparse            textwrap
_osx_support        datetime            os                  this
_overlapped         dbm                 outwin              threading
_pickle             debugger            paragraph           time
_py_abc             debugger_r          parenmatch          timeit
_pydecimal          debugobj            parser              tkinter
_pyio               debugobj_r          pathbrowser         token
_queue              decimal             pathlib             tokenize
_random             delegator           pdb                 tooltip
_sha1               difflib             percolator          trace
_sha256             dis                 pickle              traceback
_sha3               distutils           pickletools         tracemalloc
_sha512             doctest             pip                 tree
_signal             dummy_threading     pipes               tty
_sitebuiltins       dynoption           pkg_resources       turtle
_socket             easy_install        pkgutil             turtledemo
_sqlite3            editor              platform            types
_sre                email               plistlib            typing
_ssl                encodings           poplib              undo
_stat               ensurepip           posixpath           unicodedata
_string             enum                pprint              unittest
_strptime           errno               profile             urllib
_struct             faulthandler        pstats              uu
_symtable           filecmp             pty                 uuid
_testbuffer         fileinput           py_compile          venv
_testcapi           filelist            pyclbr              warnings
_testconsole        fnmatch             pydoc               wave
_testimportmultiple formatter           pydoc_data          weakref
_testmultiphase     fractions           pyexpat             webbrowser
_thread             ftplib              pyparse             window
_threading_local    functools           pyshell             winreg
_tkinter            gc                  query               winsound
_tracemalloc        genericpath         queue               wsgiref
_warnings           getopt              quopri              xdrlib
_weakref            getpass             random              xml
_weakrefset         gettext             re                  xmlrpc
_winapi             glob                redirector          xxsubtype
abc                 grep                replace             zipapp
aifc                gzip                reprlib             zipfile
antigravity         hashlib             rlcompleter         zipimport
argparse            heapq               rpc                 zlib
array               help                rstrip              zoomheight
ast                 help_about          run                 zzdummy
asynchat            history             runpy               
asyncio             hmac                runscript           
asyncore            html                sched               

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> 
topics

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> topics
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    topics
NameError: name 'topics' is not defined
>>> help()

Welcome to Python 3.7's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.7/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> 
Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> METHODS
Methods
*******

Methods are functions that are called using the attribute notation.
There are two flavors: built-in methods (such as "append()" on lists)
and class instance methods.  Built-in methods are described with the
types that support them.

If you access a method (a function defined in a class namespace)
through an instance, you get a special object: a *bound method* (also
called *instance method*) object. When called, it will add the "self"
argument to the argument list.  Bound methods have two special read-
only attributes: "m.__self__" is the object on which the method
operates, and "m.__func__" is the function implementing the method.
Calling "m(arg-1, arg-2, ..., arg-n)" is completely equivalent to
calling "m.__func__(m.__self__, arg-1, arg-2, ..., arg-n)".

Like function objects, bound method objects support getting arbitrary
attributes.  However, since method attributes are actually stored on
the underlying function object ("meth.__func__"), setting method
attributes on bound methods is disallowed.  Attempting to set an
attribute on a method results in an "AttributeError" being raised.  In
order to set a method attribute, you need to explicitly set it on the
underlying function object:

   >>> class C:
   ...     def method(self):
   ...         pass
   ...
   >>> c = C()
   >>> c.method.whoami = 'my name is method'  # can't set on the method
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AttributeError: 'method' object has no attribute 'whoami'
   >>> c.method.__func__.whoami = 'my name is method'
   >>> c.method.whoami
   'my name is method'

See The standard type hierarchy for more information.

Related help topics: class, def, CLASSES, TYPES

help> exit
Help on Quitter in module _sitebuiltins object:

exit = class Quitter(builtins.object)
 |  exit(name, eof)
 |  
 |  Methods defined here:
 |  
 |  __call__(self, code=None)
 |      Call self as a function.
 |  
 |  __init__(self, name, eof)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> num = 555
>>> id(num)
88514592
>>> name = 'arnab banerjee'
>>> id(name)
20756744
>>> newnum = 555
>>> id(newnum)
88516768
>>> newname = 'arnab banerjee'
>>> id(newname)
17880432
>>> anothernum = num
>>> id(anothernum)
88514592
>>> anothername = name
>>> id(anothername)
20756744
>>> id(555)
88518352
>>> id('arnab banerjee')
69067624
>>> type(num)
<class 'int'>
>>> type(name)
<class 'str'>
>>> abc
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    abc
NameError: name 'abc' is not defined
>>> abc = none
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    abc = none
NameError: name 'none' is not defined
>>> abc = None
>>> abc
>>> 
>>> 
>>> 
>>> 
>>> dic = {'name': 'arnab', 'city': 'kolkata'}
>>> dic
{'name': 'arnab', 'city': 'kolkata'}
>>> type(dic)
<class 'dict'>
>>> dic.keys()
dict_keys(['name', 'city'])
>>> dic.values()
dict_values(['arnab', 'kolkata'])
>>> dic['name']
'arnab'
>>> dic['city']
'kolkata'
>>> dic.get('name')
'arnab'
>>> print(dic.get('city'))
kolkata
>>> c, d = 5, 6.6
>>> c
5
>>> type(c)
<class 'int'>
>>> d
6.6
>>> type(d)
<class 'float'>
>>> c, d, e = 5, 6, 7
>>> 6++
SyntaxError: invalid syntax
>>> n = 6
>>> n++
SyntaxError: invalid syntax
>>> n
6
>>> c < d
True
>>> c > d
False
>>> c == d
False
>>> boo = c == d
>>> boo
False
>>> type(boo)
<class 'bool'>
>>> c != d
True
>>> c
5
>>> d
6
>>> c < 8 and d < 8
True
>>> c < 8 and d > 8
False
>>> c < 8 or d < 8
True
>>> c < 8 or d > 8
True
>>> c < 8 || d < 8
SyntaxError: invalid syntax
>>> c < 8 not and d < 8
SyntaxError: invalid syntax
>>> x = True
>>> c
5
>>> x
True
>>> not x
False
>>> x = not x
>>> x
False
>>> !x
SyntaxError: invalid syntax
>>> bin(4)
'0b100'
>>> x = 4
>>> bin(x)
'0b100'
>>> x = bin(4)
>>> x
'0b100'
>>> type(x)
<class 'str'>
>>> bin(25)
'0b11001'
>>> bin(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
'0b11011100001000011010000100010111000111010100001001100100010111010111011001110000011101010100001111110100111110100001111101110011101100000101111110011000011111111101101111101101001111000010011111010000100011100010001101011010111000100010010011100111001101100010001010010011001110010000111110111000011101110011111000001111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
>>> 0b11011100001000011010000100010111000111010100001001100100010111010111011001110000011101010100001111110100111110100001111101110011101100000101111110011000011111111101101111101101001111000010011111010000100011100010001101011010111000100010010011100111001101100010001010010011001110010000111110111000011101110011111000001111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
>>> 0b100101001010010
19026
>>> oct(x)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    oct(x)
TypeError: 'str' object cannot be interpreted as an integer
>>> x = 4
>>> oct(x)
'0o4'
>>> bin(0o4)
'0b100'
>>> oct(9999999999999999999999999999999999999999999999999999999)
'0o6414751324147742016627777513234375640717331777777777777777777'
>>> hex(9999999999999999999999999999999999999999999999999999999)
'0x6867a5a867f103b2fffa5a71fba0e7b67fffffffffffff'
>>> ~1
-2
>>> !0
SyntaxError: invalid syntax
>>> ~0
-1
>>> ~-0
-1
>>> ~4
-5
>>> bin(4)
'0b100'
>>> bin(-5)
'-0b101'
>>> 
copyright
Copyright (c) 2001-2019 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved.
>>> credits
    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information.
>>> license()
A. HISTORY OF THE SOFTWARE
==========================

Python was created in the early 1990s by Guido van Rossum at Stichting
Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands
as a successor of a language called ABC.  Guido remains Python's
principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for
National Research Initiatives (CNRI, see http://www.cnri.reston.va.us)
in Reston, Virginia where he released several versions of the
software.

In May 2000, Guido and the Python core development team moved to
BeOpen.com to form the BeOpen PythonLabs team.  In October of the same
year, the PythonLabs team moved to Digital Creations, which became
Zope Corporation.  In 2001, the Python Software Foundation (PSF, see
https://www.python.org/psf/) was formed, a non-profit organization
created specifically to own Python-related Intellectual Property.
Zope Corporation was a sponsoring member of the PSF.

All Python releases are Open Source (see http://www.opensource.org for
the Open Source Definition).  Historically, most, but not all, Python
Hit Return for more, or q (and Return) to quit: 
releases have also been GPL-compatible; the table below summarizes
the various releases.

    Release         Derived     Year        Owner       GPL-
                    from                                compatible? (1)

    0.9.0 thru 1.2              1991-1995   CWI         yes
    1.3 thru 1.5.2  1.2         1995-1999   CNRI        yes
    1.6             1.5.2       2000        CNRI        no
    2.0             1.6         2000        BeOpen.com  no
    1.6.1           1.6         2001        CNRI        yes (2)
    2.1             2.0+1.6.1   2001        PSF         no
    2.0.1           2.0+1.6.1   2001        PSF         yes
    2.1.1           2.1+2.0.1   2001        PSF         yes
    2.1.2           2.1.1       2002        PSF         yes
    2.1.3           2.1.2       2002        PSF         yes
    2.2 and above   2.1.1       2001-now    PSF         yes

Footnotes:

(1) GPL-compatible doesn't mean that we're distributing Python under
    the GPL.  All Python licenses, unlike the GPL, let you distribute
    a modified version without making your changes open source.  The
Hit Return for more, or q (and Return) to quit: 
    GPL-compatible licenses make it possible to combine Python with
    other software that is released under the GPL; the others don't.

(2) According to Richard Stallman, 1.6.1 is not GPL-compatible,
    because its license has a choice of law clause.  According to
    CNRI, however, Stallman's lawyer has told CNRI's lawyer that 1.6.1
    is "not incompatible" with the GPL.

Thanks to the many outside volunteers who have worked under Guido's
direction to make these releases possible.


B. TERMS AND CONDITIONS FOR ACCESSING OR OTHERWISE USING PYTHON
===============================================================

PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
--------------------------------------------

1. This LICENSE AGREEMENT is between the Python Software Foundation
("PSF"), and the Individual or Organization ("Licensee") accessing and
otherwise using this software ("Python") in source or binary form and
its associated documentation.

Hit Return for more, or q (and Return) to quit: 
2. Subject to the terms and conditions of this License Agreement, PSF hereby
grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce,
analyze, test, perform and/or display publicly, prepare derivative works,
distribute, and otherwise use Python alone or in any derivative version,
provided, however, that PSF's License Agreement and PSF's notice of copyright,
i.e., "Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019 Python Software Foundation;
All Rights Reserved" are retained in Python alone or in any derivative version
prepared by Licensee.

3. In the event Licensee prepares a derivative work that is based on
or incorporates Python or any part thereof, and wants to make
the derivative work available to others as provided herein, then
Licensee hereby agrees to include in any such work a brief summary of
the changes made to Python.

4. PSF is making Python available to Licensee on an "AS IS"
basis.  PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO AND
DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF PYTHON WILL NOT
INFRINGE ANY THIRD PARTY RIGHTS.

Hit Return for more, or q (and Return) to quit: 
5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON
FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS
A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON,
OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material
breach of its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any
relationship of agency, partnership, or joint venture between PSF and
Licensee.  This License Agreement does not grant permission to use PSF
trademarks or trade name in a trademark sense to endorse or promote
products or services of Licensee, or any third party.

8. By copying, installing or otherwise using Python, Licensee
agrees to be bound by the terms and conditions of this License
Agreement.


BEOPEN.COM LICENSE AGREEMENT FOR PYTHON 2.0
-------------------------------------------

BEOPEN PYTHON OPEN SOURCE LICENSE AGREEMENT VERSION 1
Hit Return for more, or q (and Return) to quit: 

1. This LICENSE AGREEMENT is between BeOpen.com ("BeOpen"), having an
office at 160 Saratoga Avenue, Santa Clara, CA 95051, and the
Individual or Organization ("Licensee") accessing and otherwise using
this software in source or binary form and its associated
documentation ("the Software").

2. Subject to the terms and conditions of this BeOpen Python License
Agreement, BeOpen hereby grants Licensee a non-exclusive,
royalty-free, world-wide license to reproduce, analyze, test, perform
and/or display publicly, prepare derivative works, distribute, and
otherwise use the Software alone or in any derivative version,
provided, however, that the BeOpen Python License is retained in the
Software, alone or in any derivative version prepared by Licensee.

3. BeOpen is making the Software available to Licensee on an "AS IS"
basis.  BEOPEN MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, BEOPEN MAKES NO AND
DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF THE SOFTWARE WILL NOT
INFRINGE ANY THIRD PARTY RIGHTS.

4. BEOPEN SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF THE
Hit Return for more, or q (and Return) to quit: 
SOFTWARE FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS
AS A RESULT OF USING, MODIFYING OR DISTRIBUTING THE SOFTWARE, OR ANY
DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

5. This License Agreement will automatically terminate upon a material
breach of its terms and conditions.

6. This License Agreement shall be governed by and interpreted in all
respects by the law of the State of California, excluding conflict of
law provisions.  Nothing in this License Agreement shall be deemed to
create any relationship of agency, partnership, or joint venture
between BeOpen and Licensee.  This License Agreement does not grant
permission to use BeOpen trademarks or trade names in a trademark
sense to endorse or promote products or services of Licensee, or any
third party.  As an exception, the "BeOpen Python" logos available at
http://www.pythonlabs.com/logos.html may be used according to the
permissions granted on that web page.

7. By copying, installing or otherwise using the software, Licensee
agrees to be bound by the terms and conditions of this License
Agreement.


Hit Return for more, or q (and Return) to quit: 
CNRI LICENSE AGREEMENT FOR PYTHON 1.6.1
---------------------------------------

1. This LICENSE AGREEMENT is between the Corporation for National
Research Initiatives, having an office at 1895 Preston White Drive,
Reston, VA 20191 ("CNRI"), and the Individual or Organization
("Licensee") accessing and otherwise using Python 1.6.1 software in
source or binary form and its associated documentation.

2. Subject to the terms and conditions of this License Agreement, CNRI
hereby grants Licensee a nonexclusive, royalty-free, world-wide
license to reproduce, analyze, test, perform and/or display publicly,
prepare derivative works, distribute, and otherwise use Python 1.6.1
alone or in any derivative version, provided, however, that CNRI's
License Agreement and CNRI's notice of copyright, i.e., "Copyright (c)
1995-2001 Corporation for National Research Initiatives; All Rights
Reserved" are retained in Python 1.6.1 alone or in any derivative
version prepared by Licensee.  Alternately, in lieu of CNRI's License
Agreement, Licensee may substitute the following text (omitting the
quotes): "Python 1.6.1 is made available subject to the terms and
conditions in CNRI's License Agreement.  This Agreement together with
Python 1.6.1 may be located on the Internet using the following
unique, persistent identifier (known as a handle): 1895.22/1013.  This
Hit Return for more, or q (and Return) to quit: 
Agreement may also be obtained from a proxy server on the Internet
using the following URL: http://hdl.handle.net/1895.22/1013".

3. In the event Licensee prepares a derivative work that is based on
or incorporates Python 1.6.1 or any part thereof, and wants to make
the derivative work available to others as provided herein, then
Licensee hereby agrees to include in any such work a brief summary of
the changes made to Python 1.6.1.

4. CNRI is making Python 1.6.1 available to Licensee on an "AS IS"
basis.  CNRI MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR
IMPLIED.  BY WAY OF EXAMPLE, BUT NOT LIMITATION, CNRI MAKES NO AND
DISCLAIMS ANY REPRESENTATION OR WARRANTY OF MERCHANTABILITY OR FITNESS
FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF PYTHON 1.6.1 WILL NOT
INFRINGE ANY THIRD PARTY RIGHTS.

5. CNRI SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON
1.6.1 FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS
A RESULT OF MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 1.6.1,
OR ANY DERIVATIVE THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material
breach of its terms and conditions.
Hit Return for more, or q (and Return) to quit: 

7. This License Agreement shall be governed by the federal
intellectual property law of the United States, including without
limitation the federal copyright law, and, to the extent such
U.S. federal law does not apply, by the law of the Commonwealth of
Virginia, excluding Virginia's conflict of law provisions.
Notwithstanding the foregoing, with regard to derivative works based
on Python 1.6.1 that incorporate non-separable material that was
previously distributed under the GNU General Public License (GPL), the
law of the Commonwealth of Virginia shall govern this License
Agreement only as to issues arising under or with respect to
Paragraphs 4, 5, and 7 of this License Agreement.  Nothing in this
License Agreement shall be deemed to create any relationship of
agency, partnership, or joint venture between CNRI and Licensee.  This
License Agreement does not grant permission to use CNRI trademarks or
trade name in a trademark sense to endorse or promote products or
services of Licensee, or any third party.

8. By clicking on the "ACCEPT" button where indicated, or by copying,
installing or otherwise using Python 1.6.1, Licensee agrees to be
bound by the terms and conditions of this License Agreement.

        ACCEPT
Hit Return for more, or q (and Return) to quit: 


CWI LICENSE AGREEMENT FOR PYTHON 0.9.0 THROUGH 1.2
--------------------------------------------------

Copyright (c) 1991 - 1995, Stichting Mathematisch Centrum Amsterdam,
The Netherlands.  All rights reserved.

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appear in all copies and that
both that copyright notice and this permission notice appear in
supporting documentation, and that the name of Stichting Mathematisch
Centrum or CWI not be used in advertising or publicity pertaining to
distribution of the software without specific, written prior
permission.

STICHTING MATHEMATISCH CENTRUM DISCLAIMS ALL WARRANTIES WITH REGARD TO
THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS, IN NO EVENT SHALL STICHTING MATHEMATISCH CENTRUM BE LIABLE
FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
Hit Return for more, or q (and Return) to quit: 
OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.



Additional Conditions for this Windows binary build
---------------------------------------------------

This program is linked with and uses Microsoft Distributable Code,
copyrighted by Microsoft Corporation. The Microsoft Distributable Code
is embedded in each .exe, .dll and .pyd file as a result of running
the code through a linker.

If you further distribute programs that include the Microsoft
Distributable Code, you must comply with the restrictions on
distribution specified by Microsoft. In particular, you must require
distributors and external end users to agree to terms that protect the
Microsoft Distributable Code at least as much as Microsoft's own
requirements for the Distributable Code. See Microsoft's documentation
(included in its developer tools and on its website at microsoft.com)
for specific details.

Redistribution of the Windows binary build of the Python interpreter
complies with this agreement, provided that you do not:
Hit Return for more, or q (and Return) to quit: 

- alter any copyright, trademark or patent notice in Microsoft's
Distributable Code;

- use Microsoft's trademarks in your programs' names or in a way that
suggests your programs come from or are endorsed by Microsoft;

- distribute Microsoft's Distributable Code to run on a platform other
than Microsoft operating systems, run-time technologies or application
platforms; or

- include Microsoft Distributable Code in malicious, deceptive or
unlawful programs.

These restrictions apply only to the Microsoft Distributable Code as
defined above, not to Python itself or any programs running on the
Python interpreter. The redistribution of the Python interpreter and
libraries is governed by the Python Software License included with this
file, or by other licenses as marked.



--------------------------------------------------------------------------
Hit Return for more, or q (and Return) to quit: 

This program, "bzip2", the associated library "libbzip2", and all
documentation, are copyright (C) 1996-2010 Julian R Seward.  All
rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

2. The origin of this software must not be misrepresented; you must 
   not claim that you wrote the original software.  If you use this 
   software in a product, an acknowledgment in the product 
   documentation would be appreciated but is not required.

3. Altered source versions must be plainly marked as such, and must
   not be misrepresented as being the original software.

4. The name of the author may not be used to endorse or promote 
   products derived from this software without specific prior written 
   permission.
Hit Return for more, or q (and Return) to quit: 

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Julian Seward, jseward@bzip.org
bzip2/libbzip2 version 1.0.6 of 6 September 2010

--------------------------------------------------------------------------


  LICENSE ISSUES
  ==============

  The OpenSSL toolkit stays under a double license, i.e. both the conditions of
Hit Return for more, or q (and Return) to quit: 
  the OpenSSL License and the original SSLeay license apply to the toolkit.
  See below for the actual license texts.

  OpenSSL License
  ---------------

/* ====================================================================
 * Copyright (c) 1998-2019 The OpenSSL Project.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in
 *    the documentation and/or other materials provided with the
 *    distribution.
 *
 * 3. All advertising materials mentioning features or use of this
 *    software must display the following acknowledgment:
Hit Return for more, or q (and Return) to quit: 
 *    "This product includes software developed by the OpenSSL Project
 *    for use in the OpenSSL Toolkit. (http://www.openssl.org/)"
 *
 * 4. The names "OpenSSL Toolkit" and "OpenSSL Project" must not be used to
 *    endorse or promote products derived from this software without
 *    prior written permission. For written permission, please contact
 *    openssl-core@openssl.org.
 *
 * 5. Products derived from this software may not be called "OpenSSL"
 *    nor may "OpenSSL" appear in their names without prior written
 *    permission of the OpenSSL Project.
 *
 * 6. Redistributions of any form whatsoever must retain the following
 *    acknowledgment:
 *    "This product includes software developed by the OpenSSL Project
 *    for use in the OpenSSL Toolkit (http://www.openssl.org/)"
 *
 * THIS SOFTWARE IS PROVIDED BY THE OpenSSL PROJECT ``AS IS'' AND ANY
 * EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE OpenSSL PROJECT OR
 * ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
Hit Return for more, or q (and Return) to quit: q
>>> 

>>> sqrt(25)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    sqrt(25)
NameError: name 'sqrt' is not defined
>>> import math
>>> math.sqrt(25)
5.0
>>> math.sqrt(.999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
1.0
>>> math.sqrt(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
1e+57
>>> math.pow(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    math.pow(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
OverflowError: math range error
>>> pwr = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 ^ 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
>>> pwr
0
>>> math.e
