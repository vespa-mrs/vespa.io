# Where to find out what compiler was used to create my Python installation
1. When Python starts up you usually see an info string like the one below with the compiler name.  Here it is "MSC v.1915". See below for what that means.

```
Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
```

2. You can also get this same string within Python from the command 

```
import sys
print(sys.version)
```

## What Visual Studio version matches to the MSC string in my Python install
```
Visual C++ version            _MSC_VER
Visual C++ 4.x                  1000
Visual C++ 5                    1100
Visual C++ 6                    1200
Visual C++ .NET                 1300
Visual C++ .NET 2003            1310
Visual C++ 2005  (8.0)          1400
Visual C++ 2008  (9.0)          1500
Visual C++ 2010 (10.0)          1600
Visual C++ 2012 (11.0)          1700
Visual C++ 2013 (12.0)          1800
Visual C++ 2015 (14.0)          1900

Visual C++ 2017 (15.0)          1910
Visual C++ 2017 (15.3)          1911
Visual C++ 2017 (15.5)          1912
Visual C++ 2017 (15.6)          1913
Visual C++ 2017 (15.7)          1914
Visual C++ 2017 (15.8)          1915
Visual C++ 2017 (15.9)          1916

Visual C++ 2019 RTW (16.0)      1920
Visual C++ 2019 (16.1)          1921
Visual C++ 2019 (16.2)          1922
Visual C++ 2019 (16.3)          1923
```

Source: the documentation for the _MSC_VER predefined macro
