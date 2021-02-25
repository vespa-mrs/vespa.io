# Technical Documentation
This is the central station for technical documentation about Vespa. It's 
_not_ likely to be of interest to those who just want to use Vespa.
It's for those who want to know more about Vespa's development as a software
project, including how to contribute. 

Here you can find high level overviews of various topics (Python, wxPython, 
SQLite, C++, compilers, 3rd party libraries, etc.) as well as detailed
notes written by the technical team.


## General
 * SubversionRepositories - A list of our SVN repositories with links to each
 * TracInstances - A list of our Trac instances with links to each
 * [wiki:Licensing] - About our open source license

## Getting Started
 * DeveloperSetup - Everything you need to get started as a Vespa developer
 including how to get Vespa's source code, how to set up the UI design tools, 
 and various technical notes.

## Distribution and Installation (for Release Managers)
 * [wiki:HowToBuildAVespaWheel] - How to build a wheels for uploading to PyPI
 * PreAndPostInstallUtilities - About the utilities that assist users with installation 
 * [wiki:PasswordsAndPyPI] - Interacting with PyPI

## General Technical Notes About Vespa
 * CodingStandards
 * VespaDataDirectory - How to find Vespa's data directory
 * IniFiles - About Vespa's INI files
 * ExceptionHandler - How Vepsa's custom exception handler works (and how to disable it)
 * [wiki:VIFF] - An overview of VIFF (Vespa Interchange File Format), the XML format Vespa uses for imports and exports
 * XmlVersionNumbers - About the version numbers in our XML
 * ExportFormat - A little about importing and exporting
 * [gamma:wiki:GammaSwigImplementation Swigging Gamma Implementation] and [gamma:wiki:GammaSwigIssues Issues & Solutions]
 * [wiki:Python3Issues] - A summary of changes in Python 3 that we should keep in mind
 * ThePerilsOfStr - Why we should stop using `str()` on strings
 * ImportSubtleties - Some subtle points about Python's `import`, especially for file in `vespa/common`

## Database Topics 
 * SqliteVersions - Some notes about why we must support SQLite 3.5.9
 * ChangingTheDatabaseStructure - How to change the SQL that defines Vespa's database
 * DatabaseUuidEfficiency - An examination of the efficiency of our use of UUIDs in the database and an exploration of alternatives.
 * DatabaseArrayBlobs - How we store arrays as SQLite BLOBs

## GUI Development
Documents about wxWidgets, wxPython and wxGlade and how we use them in our apps.

 * GuiDevelopmentOverview - An overview of how we organize our GUI code
 * WxCommon - A description of the `vespa.common.wx` library
 * WxGladeCustomControls - About wxGlade and custom controls
 * WxTipsBugsAndQuirks - Miscellaneous Tips, Bugs and Quirks
 * InstallingWxGladeUnderWindows - A special note about installing wxGlade under Windows
 * DicomBrowserDemo - A functional DICOM browser that also serves as a wx sample app


## Other Technical Notes
 * [wiki:LambdaSetOperations] - useful in many places to get unique lists or compare two lists 
 * MsvcVersionNumbers
 * SwiggingHlsvd - Philip's experiment with SWIG-ing the HLSVD library
 * InstallerGenerators - Philip's research on tools to generate installers for Windows 
 * [Py2Exe](/wiki:Py2Exe/) - Philip's description of his experiments with Py2exe
 * LinuxBinaryCompatibility - some notes about generating binaries compatible across multiple versions of Linux
 * [wiki:SciPy2009] - Notes from the SciPy 2009 conference 
 * SiemensCsaHeaderParsing - Philip's travelogue of an expedition through a Siemens DICOM CSA header
 * [wiki:AddingProjectsToEclipse] - How to add an existing projects code base to Eclipse.