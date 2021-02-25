# Enumerations in Pulse, etc
The following enumeration shows how a class can be used to create a set of options (enumerations) for a variable that can be represented nicely in code, the database, and the user interface (e.g. for comboboxes, etc).

The basic idea is to list each of the enumeration items as dictionaries, which is very easy to do in Python.

After importing this code,

```

# File name: my_constants.py

class UsageType(object):
    NONE = {}
    EXCITE = {'display': 'Excite', 'db':'excite'}
    INVERSION = {'display':'Inversion', 'db':'inversion'}
    SPIN_ECHO = {'display':'Spin Echo', 'db':'spin_echo'}
    SATURATION = {'display':'Saturation', 'db':'saturation'}
```

from the file my_constants.py:

```
import my_constants as constants
```

and the value used in the math/logic part of the python code looks like this:

```
usage_type = constants.UsageType.SPIN_ECHO

if usage_type == constants.UsageType.INVERSION:
    results = get_inversion_waveform()
elif usage_type == constants.UsageType.SPIN_ECHO:
    results = get_spin_echo_results()
# // etc.
```

When getting the value to be displayed on the screen one would use,
```
usage_type['display']
```

And, when getting the value to put into the database (and for comparing what comes out of the database):
```
usage_type['db']
```

