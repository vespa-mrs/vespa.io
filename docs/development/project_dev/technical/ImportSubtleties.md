# Import Subtleties
Python's `import` can behave in a way that might surprise you. This document
explains when that can happen, and what the effects are, and how to avoid it.

## Minimalist Practical Summary
Code in `vespa/common` should always import with the form 
`import vespa.common.foo` rather than the lazier `import foo`.

## Introduction
We use two kinds of import statements. I'll call them _qualified_  and
_local_ imports. Qualified imports start with `vespa.` and specify the 
location of the target module inside the vespa package. Here's
three examples. Note that the `util_xml` alias doesn't change
the fact that what it's aliasing is qualified -- 

```
#!python
import vespa.common.constants
import vespa.common.util.misc
import vespa.common.util.xml_ as util_xml
```

What I call a _local_ import relies on the fact that Python includes the
current directory in the search path for a module reference. That's why
modules in `vespa/common` can do this -- 

```
#!python
import constants
import mrs_metabolite
import util.xml_ as util_xml
```

## Subtle Side Effect Number 1
When Python encouters an import statement for a module that's already been
imported, it checks `sys.modules` to see if the module is already imported.
If it is, then the import is essentially a no-op. So in Vespa where we have
`import wx` and `import numpy` at the top of many, many files, we still only
load one copy of `wx` and one copy of `numpy`.

However, the files in `vespa/common` can be referenced in two ways. Files
outside of that directory tree use qualified references, like in the examples
above. Files in that tree can use qualified _or_ local references. Both work
fine.

However, *importing via both qualified and local references imports the module twice*.

We can demonstrate this with an interactive Python session started in the
`vespa/common` directory.

```
#!python
>>> import mrs_metabolite
>>> import vespa.common.mrs_metabolite
>>> mrs_metabolite is vespa.common.mrs_metabolite
False
>>> import sys
>>> sys.modules["mrs_metabolite"]
<module 'mrs_metabolite' from 'mrs_metabolite.pyc'>
>>> sys.modules["vespa.common.mrs_metabolite"]
<module 'vespa.common.mrs_metabolite' from '/Users/philip/w/duke/src/vespa/common/mrs_metabolite.pyc'>
>>> 
```

The `is` comparison in the example above proves that Python considers these
different modules. `mrs_metabolite` has been loaded twice.

## Subtle Side Effect Number 2
So far we've demonstrated an inefficiency, but nothing worse. Now we'll build
on the previous scenario to show how this creates a real problem. Let's 
pick up where we left off in the interactive Python session.

```
#!python
>>> mrs_metabolite.Metabolite is vespa.common.mrs_metabolite.Metabolite
False
>>> metab = mrs_metabolite.Metabolite()
>>> isinstance(metab, mrs_metabolite.Metabolite)
True
>>> isinstance(metab, vespa.common.mrs_metabolite.Metabolite)
False
>>>     
```

What the session above shows is that although we might think of the modules
as being the same, to Python they're different. Not only are the modules
different, *Python considers the classes inside the module to be different*.
That's why the first `isinstance()` returns `True` and the second `False`.

## Practical Consequences of Multiple Imports
1. It breaks `isinstance()`. This is a headache for us.
1. It's inefficient. In the grand scheme of things, the inefficiences
 probably don't matter much. But add enough small inefficiences together and
 you get trouble.
 
## Recommendation
When we have a choice between using a local or qualified import, we should 
use the latter. Since only files in `vespa/common` have the choice, we 
just need to be careful that those files always use qualified imports. 

## Side Note
Python offers _absolute_ and _relative_ imports. Don't confuse the issue
described in this document with those Python features! Absolute and relative
imports determine how Python resolves ambiguous names. For instance, if
there's a module called `draw.py` in your local directory and also a `draw`
package in your `site-packages` directory, which should Python grab when
your code says `import draw`? That's what _absolute_ and _relative_ 
imports are concerned with.
