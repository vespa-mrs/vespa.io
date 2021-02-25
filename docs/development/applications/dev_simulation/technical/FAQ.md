# Vespa - Simulation FAQ Page
Questions and answers specific to the Simulation application and maybe a bit more ...

## Index
 * [#HowdoIdownloadVespa How do I download Vespa?]
 * [#HowdoIinstallVespa How do I install Vespa?]
 * [#WheredoIfindtheSimulationUserManual Where do I find the Simulation User Manual?]
 * [#WherecanIreadmoreaboutNMRsimulationandprocessing Where can I read more about NMR simulation and processing?]
 * [#HowdoIseetheoutputfromprintstatementsinmypulsesequencecode How do I see the output from `print` statements in my pulse sequence code?]
 * [#WhydoesSimulationappeartohangorslowdownforlargespinsystems Why does Simulation appear to hang or slow down for large spin systems?]
 * [#DoesPyGAMMAperformdifferentlyfromGAMMA Does PyGAMMA perform differently from GAMMA?]
 * [#MyPyGAMMAProgramIsUnstableorBehavesBadlyandYetitLooksFine My PyGAMMA Program Is Unstable or Behaves Badly and Yet it Looks Fine?]
 * [#WheredoestheSavemenuitemsavemyExperiment Where does the Save menu item save my Experiment?]
 * [#CanSimulationoutputExperimentresultsasFIDs Can Simulation output Experiment results as FIDs?] 


----
## Questions and Answers
### How do I download Vespa?
You can download Vespa from the [Downloads](http://scion.duhs.duke.edu/vespa/project/wiki/Downloads) page.

### How do I install Vespa?
Complete instructions for installing Vespa are on the [Installation](http://scion.duhs.duke.edu/vespa/project/wiki/Installation) page.

### Where do I find the Simulation User Manual?
The User Manual is in PDF format under the `/vespa/docs/` directory in the package that you downloaded. It can also be [project:export:/trunk/docs/simulation_user_manual.pdf accessed directly here].

### Where can I read more about NMR simulation and processing?
[Here is a list of references for spectral simulation and processing](/wiki:SpectralSimRef/)

### How do I see the output from `print` statements in my pulse sequence code?
Text sent to `stdout` isn't visible when you run Simulation from the Desktop
shortcut. Here's [PulseSequencePrintStatements instructions on how to see text sent to stdout].


### Why does Simulation appear to hang or slow down for large spin systems?
When doing calculations with a spin of 8,9, or 10, your system may appear to slow down or even hang. A likely explanation is that for larger spins it take a much longer time for the spectral calculations in the underlying [gamma:wiki GAMMA] package. For example, at a spin count of 7, a single FID experiment takes GAMMA 0.4 seconds, but at spin 10 it takes 1 hour and 24 minutes (on a 2.66 GHz Intel machine). [gamma:GammaVsSpin Here is a list of GAMMA timing results for various spin sizes]. The "slow down" may be compounded if doing a large number of individual simulations for different timings, or spacial locations. 

Note: The time it takes to run these specific jobs is virtually identical in GAMMA versus Simulation - as there is little overhead (e.g. converting arrays between python and C++) when compared to the overall time of the calculations.

### Does PyGAMMA perform differently from GAMMA?
PyGAMMA wraps actual GAMMA objects to enable you to call them from a Python script. There is some overhead involved in organizing the calls from Python to SWIG to GAMMA and/or back again. A *very* rough estimate is that there is a 10-15% performance difference for using PyGAMMA over a native C++ GAMMA program.  For a more detailed discussion see this page on the GAMMA/PyGAMMA wiki [gamma:wiki:GammaVsPyGamma GAMMA vs PyGAMMA Performance Comparison].

### My PyGAMMA Program Is Unstable or Behaves Badly and Yet it Looks Fine?
Under certain circumstances your PyGAMMA code can be written in perfectly good Python style yet give unpredictable errors (or no error at all). 

We created PyGAMMA by applying SWIG to GAMMA. In this treatment we did not apply any special code for handling return values that are pointers or references. This has caused non-pythonic behavior to be observed in some situations. 

If you have written code that involves subroutines, like this pseudocode,
```
import pygamma as pg

def binning()
   # do something interesting
   pass

def my_pulse_sequence()
    sys = pg.spin_system()
    # do something else interesting
    ACQ = pg.acquire1D(pygamma.gen_op(D), H, 0.000001)
    mx = ACQ.table(sigma0)
    return mx

mxa = my_pulse_sequence()

# About to have a problem...
binning(mxa, field, spin_count)
```

then you are at risk of having one of a number of problems. 

This is because mxa points to a an object that is contained within another object that has been made available for deletion. In this example we are returning mx, a transition table (TTable1D), which is an object that is contained within ACQ (an acquire1D object). The ACQ object will be released at the end of my_pulse_function() and therefore so will mx. When you try to use the return value, in this case mxa, in some other process (e.g. binning(mxa,...)), the behavior is unpredictable and usually bad.

So far in our research we have see this situation cause these errors:

    * Segfault
    * Bus Errors
    * Pointers to uninitialized data
    * An error box saying something bad happened
    * Pointer to the correct value with no notification of any kind of error (and that may not be valid the next time you look) 

We list here a [gamma:SwigIssueSegfault detailed description of the problem and suggest some simple work-arounds].

### Where does the Save menu item save my Experiment?
The Simulation User Manual states that the Experiment->Save menu item "Saves the Experiment in the current tab to the data base ".  The Vespa data base stores the state of the Experiment shown in the Tab at that particular moment to an sqlite file stored in your User Apps directory (location dependent on your OS).  If you make any additional changes you will need to hit save again.  Hitting "Save" allows you to reload this Experiment into Vespa-Simulation at a later date.  If you want access to your results for use in another program you should Export your results.

### Can Simulation output Experiment results as FIDs?
In a word, No. Vespa-Simulation is focused on comparing/analyzing metabolite spectral patterns at the 'single molecule' level. That is, answering the question "what does this pulse sequence do to my metabolite spectral pattern if I do *this*'. If you need to create 'fake data' you can user the Vespa-DataSim application. It reads Vespa-Simulation Experiment results from the data base and lets you create fake spectral data. You can modify line width, line shape, noise level, which metabs are included, what relative scaling factors are applied to each metabolite, etc.  You can then save this data to a file for use in other programs.