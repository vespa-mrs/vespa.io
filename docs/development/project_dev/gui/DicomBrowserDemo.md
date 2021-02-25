DICOM files come in batches of many files with related 
metadata in each. We have written a browser that displays an organized 
summary of this metadata in a tree and also displays a preview of some 
image files. 

This browser is also small enough to be a manageable introduction to 
wxPython. It runs under OS X, Linux and Windows provided
wxPython is installed.

The browser does just a few things. It allows one to select a directory
containing DICOM files, it reads the metadata in each file while providing
feedback, and then it displays the files organized in a tree. Finally, when
the user chooses a file (or hits cancel), it closes and prints out the user's
selection.

In order to run it, you'll need to install 
[the pydicom library](http://code.google.com/p/pydicom/). 

To run it, `cd` to the directory where `main.py` lives and type 
`python main.py`.

If you don't have any DICOM files with which to test, you can download some
from our SVN repository (see the `siemens_dicom_export` directory):
https://scion.duhs.duke.edu/svn/sample_data

There are three versions, each an improvement on the previous. They live in
the orphans SVN 
repository (https://scion.duhs.duke.edu/svn/orphans/) in the directory 
`philip`. 

The simple version is in `orphans/philip/dicom_browser-1.0/`. This version doesn't
offer image preview. It also assumes that all DICOM files contain a
Siemens-specific tag.

A more sophisticated version is in `orphans/philip/dicom_browser-2.0/`. 
This offers
image previewing (for certain files, notably the 55* series in our sample
data). It differentiates between Siemens and
non-Siemens files, and it makes the dialog easy to subclass for coders who
want to change how the dialog constructs the tree item description string.

The most recent version in `orphans/philip/dicom_browser-2.1/` adds 
optional multi-select capability and a subclass-friendly dialog class method 
that can filter files out of the tree.


## The Files
 * `browser_ui.wxg` is the wxGlade file that describes the user interface.
 wxGlade generates `gui_browser.py` for me. 
 * `dicom_browser.py` subclasses the dialog created in `gui_browser.py`.
 * `util_dicom.py` contains the code that talks to the pydicom library and
 generates a list of DICOM files for the dialog box.
 * `util_dicom_generic.py` contains the DicomFile class which is a generic
 container for DICOM files.
 * `util_dicom_siemens.py` contains a Siemens-specific subclass of the 
 DicomFile class.
 * `main.py` creates a dummy main window that launches the dialog.
 
## Technical Notes
 * It might be tempting to combine `dicom_browser.py` and `util_dicom.py`,
 but separating them is useful. It allows the latter to be used with a
 dependency on wx. It can be used, for example, on a server to generate
 a DICOM file list for a Web application. In that context a wx dependency 
 would be a headache.
 
 * Similarly, we want to be careful with integrating `dicom_browser.py` with
 our library of wx utilities since it has a depedency on the pydicom library.
 We can add it to the library but it should remain a separate file so that
 only applications that `import dicom_browser` will have a dependency on 
 pydicom. The rest of the files in the wx utilities library will remain
 free of this depedency.
 
 * wxPython code is always a little awkward because Python and wxWidgets
 follow different naming conventions. Python naming convention uses
 `lower_case_variables_names` while wx uses `TitleCaps`. 
 This results from the fact that 
 wxWidgets is written in C++ and wxPython is a thin, auto-generated 
 wrapper around it. In practice, it's unusual to find a Python library that 
 doesn't follow Python's naming conventions.

 In our code we've 
 introduced a third style (from Java, I think) for naming GUI controls and
 event handlers which 
 is `firstLetterLowerThenUpper` (e.g. the dialog has an event handler called 
 `onTreeItemActivated()`). 
 
 Using two different naming conventions is 
 confusing enough; I do not recommend following our example and introducing
 a third. In this code, I used firstLetterLowerThenUpper only to be 
 consistent with our existing libraries.
 
 * The function `util_dicom.get_files()` is a Python generator which is 
 something you might not be familiar with. There's a lot of tutorials online
 about generators, all of which I find much harder to grasp than the actual code.
 Maybe it's just me! Here's one such article:
 http://www.ibm.com/developerworks/library/l-pycon.html


