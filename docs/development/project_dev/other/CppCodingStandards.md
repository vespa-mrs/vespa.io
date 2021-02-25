# C++ Coding Standards

## Overview
Below I will describes in Gory detail suggested guidelines for C++ code.  These rules apply to new code: new files, new modules, new projects.

When editing an older file to fix a minor bug, etc, I think it's prudent to make as small a change as possible to the source. In this case, it will be best for readability if you use the standard that was there previously.  That includes following the established indentation, placement of curly brackets "{}", naming conventions, etc.

Obviously if the code requires a complete rewrite, then use the suggested coding standards listed below.

Here are some resources, and books that I like for learning about C++, coding standards, and general conventions for C++.  NOTE: As of this writing (July 2009) C++ is scheduled for a major revision (http://en.wikipedia.org/wiki/C%2B%2B0x), and I imagine many new books will come out, and make some of my original suggestions obsolete:

## Resources
Bjarne Stroustrup's C++ Style and Technique FAQ: http://www.research.att.com/~bs/bs_faq2.html

Great website for all things C++, STL, and C) : http://www.cplusplus.com/

Coding Standards 
  * Used as an initial resource for the coding standards listed below: http://www.possibility.com/Cpp/CppCodingStandard.html
  * Looks useful as a secondary source: http://geosoft.no/development/cppstyle.html

## Good Books
There are many, and what you like depends on your learning style.  Here are some of my favorites.

__Intermediate and Advanced__

_Effective C++_, and _More Effective C++_, by Scott Meyers


__Beginning__

_C++ Primer Plus_, by Stephen Prata


__Coding Standards (Meta Rules)__

_C++ Coding Standards: 101 Rules, Guidelines, and Best Practices_, by Herb Sutter and Andrei Alexandrescu.

"look upon this primarily as a set of meta-rules... and ignore this book at your peril"
- Bjourne Strousturp

__STL__

  * _Effective STL_, by Scott Meyers
  * _C++ Templates: The Complete Guide_, by David Vandevoorde and Nicolai M. Josuttis

## Proposed C++ coding Standard
TOPICS TO BE INCLUDED

  * Preamble
  * Introduction
  * Curly bracket conventions and placement, i.e "{ }"
  * Tab locations and size conventions
  * Scoping of class attributes (e.g. only private class attributes, public for structures)
  * Naming Conventions (general, and in detail)
  * Misc: One declaration at a time, always 'spell out' boolean equality, use header file protection, use const as much as possible, keep scope on variables as low as possible, if ( isGood == true ) vs. if(isGood==true).

### Preamble
As mentioned above, some of this was borrowed from, http://www.possibility.com/Cpp/CppCodingStandard.html, with permission as described here, "If you want to make a local copy of this standard and use it as your own you are perfectly free to do so. That's why I made it! If you find any errors or make any improvements please let me know at tmh@possibility.com."  See also http://www.possibility.com/Tmh and http://www.possibility.com/epowiki/Wiki.jsp.

However, as this is a new gamma standard, if you have any immediate issues, complaints or suggestions then send an email to david.todd@va.gov, or whoever is managing this standard.

### Introduction
Standardization is Important. It helps if the standard annoys everyone in some way, so that all members of the team feel they are on the same playing field. 

#### Good Things about a Standard
When a project tries to adhere to common standards a few good things happen: 
  * Programmers can go into any code and figure out what's going on. 
  * New people can get up to speed quickly. 
  * People new to C++ are spared the need to develop a personal style and defend it to the death. 
  * People new to C++ are spared making the same mistakes over and over again. 
  * People make fewer mistakes in consistent environments. 
  * Programmers have a common enemy - yes, the standard.

#### Bad Points about Having a Standard
Now the bad: 
  * The standard is usually stupid because it was "obviously made by someone who doesn't understand C++". 
  * The standard is usually stupid because it's "not what I do". 
  * Standards reduce creativity. 
  * Standards are unnecessary as long as people are consistent. 
  * Standards enforce too much structure. 
  * Why bother, people ignore standards anyway. 
  * Standards can be used as a reason for NIH syndrome(not invented here), because the new/borrowed code won't follow the standard. 

### Curly bracket conventions
In Brief:

```

// foobar.h

class Foobar  // should really be Fubar !!
{
public:
    Foobar(int foo, double bar);
    Foobar(Foobar & oldFoobar);

    int Foo();
    double Bar();

    SetFoo(int foo);
    SetBar(double bar);

    bool IsBeyondRecognition();

private:

    int m_Foo;
    double m_Bar;
};


// foobar.cc

bool Foobar::IsBeyondRecognition()
{
    bool is_beyond_recon = false;

    if(m_Foo > 100 || m_Bar > 10000.0)
    {
       is_beyond_recon = true;
    }
    else
    {
        int temp_foo = 3;
        double temp_bar = m_Bar + 100.0;
        while(temp_foo != 10)
        {
            if(temp_foo > 8 && temp_bar < 300.0)
            {
                is_beyond_recon = true;
                break;
            }
            else
            {
                temp_bar = this.GetNewBar(temp_bar);
            }
            
            temp_foo += 1;
        }
    }

    return is_beyond_recon;
}
```
           
*:FinishUp:*          

### Tab locations and size conventions
*:FinishUp:*

### Scoping of class attributes
 (e.g. only private class attributes, public for structures)
*FinishUp:*

### NAMES - General Discussion
_Using appropriate names for the purpose at hand._

* Good names are the heart of clear programming!! *

In ancient times people believed that knowing someone's _true_ name gave them magical power over that person. If you can think up the true name for something, you can give yourself, and the people who read your code, power over the domain.

A name is the result of a long deep thought process (or should be) about the ecology it which it lives. Only a programmer who understands the system as a whole can create a name that "fits" with the system. 

If the name is appropriate everything fits together naturally, relationships are clear, meaning is derived and derivable, and reasoning from common human expectations works as is desired. 

If you find that all your names look like _Thing_ and _Do_It_, then you should probably revisit your design. 

#### Class Names
  * Name the class after what it is. If you can't think of what it is, then that's a clue you have not thought through the design well enough. Avoid vague and generic names unless the concept is really vague and generic, which should only be true for abstract classes.  i.e. a Typewriter should be called a Typewriter and not a PushKeyInputSystem.
  * Compound names of over three words are a clue that your design may be confusing various entities in your system. Revisit your design. Consider trying a CRC card session to see if your objects have more responsibilities than they should. 
  * Try to avoid the temptation of bringing the name of the parent class into the derived class's name. A class should stand on its own. It doesn't matter what it derives from.  Only possible exceptions would be abstact class names, like "GroundTransport" (e.g. ChevyMalibu derives from GeneralMotorsCars derives from Automobile derives from GroundTransport derives from Transport... remember it's just an example!).  Of course if you're doing this, you better have a good reason to justify the added complexity of all the abstract classes!
  * Suffixes are sometimes helpful. For example, if your system uses agents, then naming an object DownloadAgent conveys real information. 


#### Method and Function Names
  * Usually every method and function performs an action, so the name should make clear what it does: CheckForErrors() instead of ErrorCheck(), DumpDataToFile() instead of DataFile(). This will also make functions and data objects more distinguishable. 
Classes are often nouns. By making function names verbs and following other naming conventions programs can be read more naturally. 

  * Suffixes are sometimes useful: 
    * Max - to mean the maximum value something can have. 
    * Cnt - the current count of a running count variable. 
    * Key - key value
    * (For example: RetryMax to mean the maximum number of retries, RetryCnt to mean the current retry count.)

  * Prefixes are sometimes useful: 
    * Is - to ask a question about something. Whenever someone sees Is they will know it's a question. 
    * Get - get a value. 
    * Set - set a value. 
    * (For example: IsHitRetryLimit, or GetValueCnt.)


#### Include Units in Names when Appropriate
If a variable represents time, weight, or some other unit then include the unit in the name so developers can more easily spot problems, and also know what values to use as input. 

For example: 
```
uint32 m_TimeoutMsecs;
uint32 m_MyWeightLbs;
```

Better yet, is to make a variable into a class so bad conversions can be caught. (:Example:?) 


#### No All Upper Case Abbreviations
When confronted with a situation where you could use an all upper case abbreviation, don't.  Instead use an initial upper case letter followed by all lower case letters. 

__Justification__

People seem to have very different intuitions, when making names containing abbreviations. It's best to settle on one strategy so the names are absolutely predictable. 

Take for example NetworkABCKey. Notice how the C from ABC and K from key can be confused. Some people don't mind this, and others just hate it, so you'll find different policies in different code and then you never know what to call something. 

Example: 
```
   class FluidOz;             // NOT FluidOZ
   class NetworkAbcKey;       // NOT NetworkABCKey
```


### Names - In Detail
#### Class Names
  * Use upper case letters as word separators, lower case for the rest of a word (CamelCaseForm)
  * First character in a name is upper case 
  * No underbars ('_') 

Justification 
  * Of all the different naming strategies many people found this one the best compromise. 

Example 
```
   class NameOneTwo;
   class Name;
   class CoolAutomobiles;
```

#### Class Library Names
  * Name spaces will hopefully make this section unnecessary, but use this if you're working with older code and need to add a new library.
  * i.e. _When not using name spaces_, it's common to prevent class name clashes by prefixing class names with a unique string. Two characters is often sufficient, but a longer length is fine. 

Example 

John Johnson's data structure library could use JJ as a prefix, so classes would be:
```
   class JjLinkList
   {
   };
```

### Class Method Names  * Use the same rule as for class names. 
  * i.e. use camel case, first letter capital, no "_" underbars.

Justification 
  * Of all the different naming strategies, this one is the best compromise. 

Example 
```
   class NameOneTwo
   {
   public:
      int                   DoIt();
      void                  HandleError();
   };
```

#### Class Attribute Names
  * Attribute names should be prepended with the character 'm_'. 
  * After the 'm' use the same rules as for class names. 
  * 'm' always precedes other name modifiers like 'p' for pointer, or 'r' for reference.
 
Justification 

  * Prepending 'm_' prevents any conflict with method names. Often your methods and attribute names will be similar, especially for accessors. 

Example 
```
   class TreeHouse
   {
   public:
      int                   VarAbc();
      int                   ErrorNumber();
   private:
      int                   m_VarAbc;
      int                   m_ErrorNumber;
      String*               m_pName;
      Deck&                 m_rDeck;
   };
```

The original spec had mVarAbc, but I think that m_VarAbc is more clear as the m is separated from the "VarAbc".  My only reservation is that it's harder to type, but usually worth the extra effort.


#### Method Argument Variable Names  * The first character should be lower case. 
  * All word beginnings after the first letter should be upper case as with class names. 

Justification 
  * You can always tell which variables are passed in variables. 
  * You can use names similar to class names without conflicting with class names. 

Example 
```
   class NameOneTwo
   {
   public:
      int  CompareEngines(Engine& rSomeEngine, 
                          Engine& rAnotherEngine, 
                          int comparisonFlag, 
                          bool doItRight);
   };
```

#### Variable Names on the Stack
i.e. Automatic variables.

  * use all lower case letters 
  * use '_' as the word separator. 

Justification 
  * With this approach the scope of the variable is clear in the code. 
  * Now all variables look different and are identifiable in the code. 

Example 
```
   int NameOneTwo::HandleError(int errorNumber)
   {
      int            error = OsErr();
      Time           time_of_error;
      ErrorProcessor error_processor;
      Time*          p_out_of_time= 0;
   }
```

The standard pointer notation is not entirely satisfactory because it doesn't look quite right, but it is consistent. 

How to handle statics? 

There's almost never a reason to have a static local to a function so there's no reason to invent a syntax for it. But like for most rules, there is an exception, that is when making singletons. Use a "s_" prefix in this case. Take a look at Singleton Pattern for more details. 


#### Pointer Variables  * pointers should be prepended by a 'p' or a 'p_' in most cases (when are the :Exeptions:?).
  * place the * close to the pointer type not the variable name 

Justification 

  * The idea is that the difference between a pointer, object, and a reference to an object is important for understanding the code, especially in C++ where -> can be overloaded, and casting and copy semantics are important. 

  * Pointers really imply a modification of type, so the * belongs near the type. One reservation with this policy relates to declaring multiple variables with the same type on the same line. In C++ the pointer modifier only applies to the closest variable, not all of them, which can be very confusing, especially for newbies. 

  * *For this reason, and for documentation reasons, only have one declaration per line.*

Example 
```
  String* pName = new String;

  String* pName, name, address; // note, only pName is a pointer.  __DON'T DO THIS__
```

#### Reference Variables and Functions Returning References  * References should be prepended with 'r'. 

Justification 
  * The difference between variable types is clarified. 
  * It establishes the difference between a method returning a modifiable object and the same method name returning a non-modifiable object. 

Example 
```
   class Test
   {
   public:
      void               DoSomething(StatusInfo& rStatus);

      StatusInfo&        rStatus();
      const StatusInfo&  Status() const;

   private:
      StatusInfo&        m_rStatus;

   };
```

#### Global Variables  * Global variables should be prepended with a 'g_'. Originally this had just a 'g', but since we are using 'm_' for class attributes, I think using 'g_' for global would distinguish the scope form the type ('p' and 'r').

Justification 
  * It's important to know the scope of a variable. 

Example 
```
    Logger  g_Log;
    Logger* g_pLog;
```

#### Global Constants  * Global constants should be all caps with '_' separators. 

Justification 
  * It's tradition for global constants to named this way. You must be careful to not conflict with other global #defines and enum labels. 

Example 
```
    const int GLOBAL_CONSTANT_FIVE = 5;
```

#### Static Variables  * Static variables should be prepended with 's_'. 

Justification 
  * It's important to know the scope of a variable. 
  * while this may seem a bit cumbersome, static variables should not be used that often.
  * Alternative choices are sm_Status, ms_Status, and m_sStatus and msStatus.  None of which is satisfactory.

Example 
```
   class Test
   {
   public:
   private:
      static StatusInfo m_s_Status;
   };
```

#### Type Names  * When possible for types based on native types make a typedef. 
  * Typedef names should use the same naming policy as for a class with the word Type appended. 

Justification 
  * Of all the different naming strategies many people found this one the best compromise. 
  * Types are things so should use upper case letters. Type is appended to make it clear this is not a class. 

Example 
```
   typedef uint16  ModuleType;
   typedef uint32  SystemType;
```

*One should be careful about when and why to create a type from system types, as it creates confusion for readers.  What is a SystemType?  Why not just call things of that type uint32?  If there is no good reason then don't do it!*


#### Enum Names  * Labels should be All Upper Case with '_' Word Separators 
  * This is the standard rule for enum labels. 

Example 
```
   enum PinStateType
   {
      PIN_OFF,
      PIN_ON
   };
```

#### Enums as Constants without Class Scoping
  * Sometimes people use enums as constants. 
  * When an enum is not embedded in a class, make sure you use some sort of differentiating name before the label so as to prevent name clashes. 

Example 
```
   enum PinStateType            If PIN was not prepended, a conflict 
   {                            would occur as OFF and ON are probably
      PIN_OFF,                  already defined.
      PIN_ON
   };
```

#### Enums with Class Scoping
  * Just name the enum items what you wish and always qualify with the class name: Aclass::PIN_OFF. 
  * Make a Label for an Error State 
  * It's often useful to be able to say an enum is not in any of its valid states. Make a label for an uninitialized or error state. Make it the first label if possible. 

Example 
```
   enum 
   { 
      STATE_ERR,  
      STATE_OPEN, 
      STATE_RUNNING, 
      STATE_DYING
   };
```

#### #define and Macro Names
  * Put #defines and macros in all upper using '_' separators. 

Justification 

  * This makes it very clear that the value is not alterable and in the case of macros, makes it clear that you are using a construct that requires care. 
  * Some subtle errors can occur when macro names and enum labels use the same name. 

Example 
```
#define MAX(a,b) blah
#define IS_ERR(err) blah
```

#### C Function Names  * In a C++ project there should be very few C functions. 
  * For C functions use the GNU convention of all lower case letters with '_' as the word delimiter. 

Justification 
  * It makes C functions very different from any C++ related names. 

Example 
```
   int some_strange_c_function()
   {
   }
```

### File Names
#### Use all lower case names
  * For classes use the camel case words, but all in lower case with a "_" separator.
  * e.g. For class *TreeHouse*
    * Call the .h file: *tree_house.h*
    * Call the .cc file: *tree_house.cc*

Justification

  * Windows does not recognize the difference between upper an lower case, so keep the file naming convention simple.  
  * i.e. If you have a file called TreeHouse.cc on windows and try to open a new file treeHouse.cc it opens the one already there, "TreeHouse.cc", however on linux, if you open up treeHouse.cc, it would create a new file.


#### C++ File Extensions
In short: Use the .h extension for header files and .cc for source files. 
For some reason an odd split occurred in early C++ compilers around what C++ source files should be called. C header files always use the .h and C source files always use the .c extension. What should we use for C++? 

The short answer is as long as everyone on your project agrees it doesn't really matter. The build environment should be able to invoke the right compiler for any extension. 

Historically speaking here have been the options: 
  * Header Files: .h, .hh, .hpp 
  * Source Files: .C, .cpp, .cc 

#### Header File Extension Discussion
Using .hh extension is not widely popular but makes a certain kind of sense, i.e. C header files use .h file extension and C++ based header files use .hh file extension. *The problem is* if we consider a header file an interface to a service then we can have a C interface to a service and C++ interface to the service in the same file. Using preprocessor directives this is possible and common. The recommendation is to stick with using the .h extension.
 
#### Source File Extension Discussion
The problem with the .C extension is that it is indistinguishable from the .c extensions in operating systems that aren't case sensitive. Yes, this is a UNIX vs. windows issue. Since it is a simple step aiding portability we won't use the .C extension. The .cpp extension is a little wordy. So the .cc extension wins by default. 


### Misc
* :FinishUp: all of these! *

  * One declaration at a time
  * always 'spell out' boolean equality
  * use header file protection
  * use const as much as possible
  * keep scope on variables as low as possible
  * if ( isGood == true ) vs. if(isGood==true)

