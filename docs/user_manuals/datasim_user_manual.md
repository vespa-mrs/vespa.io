---
sort: 3
---

# DataSim User Manual

Version 1.0.0rc4 - Release date: February 15^th^, 2021

Developed by:

-   **Brian J. Soher, Ph.D.** - Duke University, Department of
    Radiology, Durham, NC

-   **Philip Semanchuk** - Duke University, Department of Radiology,
    Durham, NC

-   **Karl Young, Ph.D.** - UCSF, San Francisco, CA

-   **David Todd, Ph.D.** - UCSF, San Francisco, CA

**Developed with support from NIH, grant \# EB008387-01A1**

##  1. Introduction to DataSim

### 1.1 Functionality

Vespa-DataSim is application written in the Python programming language
that allows users to create simulated MR data sets. DataSim allows users
to:

1.  Select from existing Vespa-Simulation Experiments in the Vespa
    database.

2.  Specify a single set of Experiment loop parameters (if more than
    one) on which to base the DataSim's metabolite basis functions.

3.  Specify the spectral resolution as the bandwidth and number of
    points in the FIDs.

4.  Scale individual metabolite areas.

5.  Create a Voigt lineshape envelope that has a specific T~a~ (T~2~)
    value for each metabolite and a global T~b~ (T~2~\*) value for the
    entire Datasim.

6.  Add unlimited Gaussian or Lorentzian spectral peaks with independent
    area, ppm, linewidth and phase to create simulated macromolecular
    signals.

7.  Add unlimited Gaussian or Lorentzian spectral peaks with independent
    area, ppm, linewidth and phase to create simulated baseline signals.

8.  SNR can be set using an independent reference line (not included in
    spectrum) to maintain RMS noise levels even as metabolite line shape
    changes.

9.  Output to Vespa-Analysis compatible data format, a simple
    text/binary header/data format (Siemens \*.rda).

10. Output a single simulated spectrum OR an array of spectra,
    containing the same signal model but different noise, for use in
    Monte Carlo evaluations.

### 1.2 Basic Concepts

**What is a DataSim?** A 'DataSim' consists of a simulated MR
spectroscopy (MRS) data set that has be created using prior information
from a Vespa-Simulation Experiment. The combination of "simulated data
set" has been shortened to "DataSim" in this manual. A DataSim can only
contain metabolites from a single set of loop parameters from the
Experiment. On output, the DataSim contains header information about all
signals, processing and noise that were performed to create the data.

**What is the DataSim Notebook?** This is the main window of the DataSim
application. It contains one or more tabs, each of which contains the
data and processing for an entire DataSim. Multiple DataSim can be
created/loaded as tabs in the DataSim Notebook.

DataSims are created in four steps, organized as four sub-tabs in each
DataSim tab. These sub-tabs are 'Spectral Settings', 'Metabolite
Signals', 'Macromolecular Signals', and 'Baseline Signals'. Upon output,
a full provenance for sub-tab parameters is created as part of the
DataSim XML output data format. A variety of graphical and text-based
methods are available for saving results, as well.

The following chapters run through the operation of the Vespa-DataSim
program both in general and widget by widget. In this manual, command
line instructions will appear in a fixed-width font on individual lines,
for example:

˜/Vespa-DataSim/ % ls

Specific file and directory names will appear in a fixed-width font
within the main text.

*The following sections assumes Vespa-DataSim has been downloaded and
installed. See the Vespa Installation guide on the Vespa main project
wiki for details on how to install the software and package
dependencies. <http://scion.duhs.duke.edu/vespa>*.

In the following, screenshots are based on running DataSim on the
Windows OS, but aside from starting the program, the basic commands are
the same on all platforms.

### 1.3 How to launch Vespa-DataSim

Double click on the DataSim icon that the installer created on your
Desktop.

Shown below is the Vespa-DataSim main window as it appears on first
opening. No actual DataSim windows are open, only the 'Welcome' banner
is displayed.

![](media_datasim\media\image1.png){width="5.455022965879265in"
height="4.152461723534558in"}

Use the **DataSim → Open DataSim** menu to open a saved DataSim session
into a tab, or the **DataSim → New DataSim from Experiment** menu to
create a new DataSim.

Shown below is a screen shot of a Vespa-DataSim session showing data
from a PRESS 30ms simulation. The functionality of all sub-tabs will be
described further in the following sections.

![](media_datasim\media\image2.png){width="6.5in"
height="4.9430555555555555in"}

##  2. The DataSim Main Window

This is a view of the main Vespa-DataSim user interface window. It is
the first window that appears when you run the program. It contains the
datasim notebook, a menu bar and status bar. The datasim notebook can be
populated with one or more datasim tabs, each of which contains input
settings and simulated dat from one datasim. As described above, a
datasim is a comprised of spectral settings, metabolite signals and
baseline signals, each of which has its own sub-tab in the respective
datasim tab. Sub-tabs are organized along the bottom edge, while datasim
tabs are organized along the top edge.

![](media_datasim\media\image3.png){width="4.567361111111111in"
height="3.4770833333333333in"}The datasim Notebook is initially
populated with a welcome text window, but no datasims are loaded. From
the DataSim menu bar you can 1) open a datasim that has previously been
processed by DataSim and then saved into the DataSim VIFF XML format, or
2) create a new datasim. In either case a tab will appear for each
datasim that is opened or imported. The View menu items set the plotting
options for whichever sub-tab is active. The Help menu provides links to
useful resources.

The status bar provides information about where the cursor is located
within the various plots in the interface throughout the program. During
plot zooms or region selections, it also provides useful information
about the cursor start and end points and the distance between. Finally,
it also reports short messages that reflect current processing while
events are running.

### 2.1 On the Menu Bar

These are the functions of various menu items in the application:

-   **DataSim→Open** - Opens an existing VIFF datasim XML file into a
    new datasim tab in the datasim Notebook. The state of the datasim as
    it was saved, including all sub-tab settings and simulated data, are
    restored as the datasim is opened into its tab.

-   **DataSim→New** - Allows the user to create a new datasim in a new
    Tab.

-   **DataSim→Save** - Saves the state of the datasim as it currently
    exists, including all sub-tab settings and data, into a VIFF (Vespa
    Interchange File Format) XML file. *Note that this does NOT save out
    a simulated data set, but just a file that DataSim can read back in
    to recreate the current state shown in the program. In other words,
    it saves the DataSim program stuff, not the simulated data stuff.
    Use Export menu items (below) to save out simulated data.*

-   **DataSim→Save As** - Same as Save, but allows the user to change
    the file name into which the datasim is saved.

-   **DataSim→ Close** - Closes the active tab.

-   **DataSim→Export Spectrum \<various\>** - Writes the simulated data
    from the datasim out to various formats. For formats that allow it,
    provenance for the simulated data is included. Otherwise. Provenance
    is saved to a separate text file in the same directory.

-   **DataSim→Export Monte Carlo \<various\>** - Similar to Export
    Spectrum, but an array of spectral data with the same signal model,
    but different added noise is saved out to various formats.

-   **DataSim→Exit** - Closes the application window.

-   **View→\<various\>** - Changes plot options in the plots on each
    sub-tab of the active datasim tab, including: display a zero line,
    turn x-axis on/off or choose units, select the data type (real,
    imag, magn) displayed, and various output options for all plot
    windows and experiment in text format.

-   **Help→User Manual** - Launches the user manual (from vespa/docs)
    into a PDF file reader.

-   **Help→DataSim/Vespa Online Help** - Online wiki for the DataSim
    application and Vespa project

-   **Help→About** - Giving credit where credit is due.

### 2.2 The DataSim Notebook

The datasim notebook offers a lot of flexibility. Multiple tabs can be
opened up inside the window. They can be moved around, arranged and
"docked" as the user desires by left-click and dragging the desired tab
to a new location inside the notebook boundaries. In this manner, the
tabs can be positioned side-by-side, top-to-bottom or stacked. They can
also be arranged in any mixture of these positions. There is only the
one Notebook in the DataSim application, but it can display multiple
simulated MRS data sets by loading them into DataSim tabs.

### 2.3 DataSim Tabs

The datasim notebook can be populated with one or more datasim tabs,
each of which contains the spectral settings, metabolite signals,
macromolecule signals and baseline signals of one datasim. Tabs for
datasims are arranged along the top of the notebook and can be grabbed
(left-click and drag) and moved to different locations inside the
notebook as you like. Tabs can be closed using the X box on the tab or
with a middle-click on the tab itself. When a tab is closed, the datasim
is removed from memory, but can be restored to its current state at a
future time - assuming it was saved to DataSim VIFF format.

Each datasim tab has four sub-tabs that represent the spectral settings,
metabolite signals, macromolecule signals and baseline signals in the
data. Each processing sub-tab is described in more detail in the
following section.

DataSims are only saved to file when specifically requested by the user.
On selecting **DataSim → Save**, the current state of the datasim, ie.
all settings and results in all tabs, is saved into a file in the Vespa
Interchange File Format, or VIFF. This file can be updated when desired
by the user by again hitting Save, or a new filename can be used to save
different states in different files by using **DataSim → Save As**. When
a VIFF file is opened in DataSim, all tabs and results are restored to
the state they were in upon save.

Each processing sub-tab displays name of the Simulation Experiment that
provides the basis functions for the metabolites, the indices of the
specific Experiment set of loop parameters that is being used, and the
y-scale of the plot in the sub-tab.

The View menu on the main menu bar can be used to modify the display of
the plots in the active sub-tab. The state of plot options in each
sub-tab is maintained in each sub-tab as the user switches between them.
The following lists the functions on the View menu item:

**The following Menu Bar items specifically affect the Plot Canvas in
the currently active DataSim tab**

-   **View→ZeroLine→Show** - toggle zero line off/on

-   **View→ZeroLine→Top/Middle/Bottom** - display the zero line in the
    top 10% region, middle or bottom 10% region of the canvas as it is
    drawn on the screen

-   **View→Xaxis →Show** - display the x-axis or not

-   **View→Xaxis→PPM/Hz** - x-axis value in PPM or Hz

-   **View→Data Type** - select Real, Imaginary, or Magnitude spectral
    data to display

-   **View→Plot Views→Final/All Three** - select whether only the final
    simulated spectrum is displayed, or the final spectrum, the
    metabolite signals and, macromolecule signals + baseline signals are
    each displayed in their own plot.

-   **View→Output Experiment Text** - displays the selected Experiment
    object in text format in a separate text editor, similarly to what
    can be displayed in the Vespa-Simulation application.

-   **View→Output→View→\<various\>** - writes the entire plot to file as
    either PNG, SVG, EPS or PDF format

### 2.4 Mouse Events in Plots

Most processing sub-tabs have plots in their right hand panels. These
plots may contain one or more axes which may change dynamically.
Typically, the DataSim plot will show either one spectrum which is the
sum of metabolite signals + macromolecule signals + baseline signals +
noise, or three plots which display the summed spectrum, the metabolite
spectrum and the baseline spectrum, respectively.

You can control a number of functions by using your mouse interactively
within the plot area of most sub-tabs. Vespa-DataSim is best used with a
'two-button' mouse that has a scroll wheel, but can also work fine with
a 'two-button' mouse, as most mouse-driven features for the scroll wheel
also have a corresponding widget that can be clicked on or typed in to
cause the same effect. The following describes the typical actions that
can be effected using the mouse in a plot window. Any variations from
this will be noted in the following sub-tab sections.

The mouse can be used to set the X-axis and cursor values in sub-tab
plots. When there are three plots, the same X-axis or cursors are set on
all three. The left mouse button sets the X-axis zoom range. Click and
hold the left mouse button in the window and a vertical cursor will
appear. Drag the mouse either left or right and a second vertical cursor
will appear. PPM value changes will be reflected in the status bar.
Release the mouse and the plot will be redisplayed for the axis span
selected. This zoom span will display its range in a pale yellow that
disappears when the left mouse is released. Click in place with the left
button and the plot will zoom out to its max x- and y-axis settings.

In a similar fashion, two vertical cursors can be set inside the plot
window. Click and drag, then release, to set the two cursors anywhere in
the window. This cursor xpan will display as a light gray span. Click in
place with the right mouse button and the xursor span will be turned
off.

The cursor values are used to determine the "area under the peak" values
that are displayed in the status bar. While performing a right-click and
drag to create a cursor span the status bar will also display the
start/end location of the span and the delta Hz and delta PPM size of
the span.

The roller bar can be used to increment/decrement the Y-axis scale
value. A maximum value for the Y-axis scale is determined the first time
a datasim is loaded and displayed. That max value is the value displayed
in the scale widget (top right in the datasim) and used when you zoom
all the way out. As you roll the ball up/down (or you click on the
SpinCtrl widget next to the scale field) the scale value changes and the
plot is updated. (Note. It may be necessary to actually click in the
plot window to move the focus of the scroll wheel into the plot, before
the scroll wheel events will be applied to the Scale value.)

Roller balls can typically be used also as a 'middle button' but pushing
down on it without rolling it up or down. DataSim plots do not make use
of events from this middle button.

Click and release the left mouse button in place and the plot will zoom
out to its max setting. Click and release the right mouse button in
place and the cursor span will be turned off

##  3. Spectral Settings Sub-tab

### 3.1 General

Each datasim tab has four sub-tabs called Spectral Settings, Metabolite
Signals, Macromolecule Signals and Baseline Signals. The Spectral
Settings tab is shown below.

![](media_datasim\media\image4.png){width="6.5in"
height="4.9430555555555555in"}

**Theoretical Details**

The formula below describes how the simulated data signals are created
in the time domain as a sum of metabolite *Metab(t)*, macromolecule
*Mmol(t),* baseline *Base(t)* and noise *N(t*) functions, and
subsequently transformed into the spectral domain using the FFT for
display in the DataSim plot panel. Note that macromolecular and baseline
signal contributions are listed separately in order to allow various
artifactual signals to be described independently with either Gaussian
or Lorentzian lineshapes.

The metabolite signal starts with a set of basis functions generated
from the *a priori* Simulation Experiment information. The set of all *a
priori* resonance lines for each metabolite are indexed over n from 1 to
*N~Mmol~*. These sinusoids are created at the digital/spectral
resolution set by the user. Only the metabolites selected by the user
are included. Metabolite basis functions are modified by the
user-specified areas (*A~m~*) and T~2~ decays (*T~a~*) and global
frequency shift (*ω~0~*), phase 0 (*φ~0~*) and T~2~\* decay (*T~b~*)
terms.

If the 'Left Shift' widget/parameter is not zero, then after the time
domain FID has been calculated, it is truncated by N integer points (as
set by the spectral resolution widget) before being Fourier transformed.
The value N is taken from the Left Shift widget setting.

![](media_datasim\media\image5.png){width="6.466288276465442in"
height="3.822589676290464in"}

### 3.2 Metabolite Spectral Settings Section

The Metabolite Spectral Settings section contains controls that affect
the spectral resolution, SNR and global spectral parameters for the
simulated data. The data in the plot on the right will update
interactively as you change parameters.

Spectral resolution and the PPM range of metabolite basis peaks is set
by using the **Set metabolite spectral resolution and basis PPM range**
button. This button will launch a dialog (shown below):

![](media_datasim\media\image6.png){width="2.439903762029746in"
height="1.8837106299212598in"}

You can set the **Frequency**, **Spectral Points,** **Spectral Width**
and metabolite inclusion range in PPM using spin control widget.
**Note** -- changes to any of these widgets will result in a
recalculation of all basis functions from the selected Experiment, but
not until you hit the OK button. Depending on the number of steps in all
Experiment parameter loops, this recalculation can take an appreciable
amount of time. However, it does speed up display of different basis
sets when the Loop indices change.

The **Phase 0** and **B0 shift** widget spin controls set these global
values for the simulated data.

The **Tb** spin control is used to set effects of simulated T~2~\* line
broadening. An estimate of the resulting Line Width (in Hz) is displayed
in the field below. This estimate is based on an assumed T~a~ (T~2~)
value of 0.3 seconds because each metabolite can have its own T~2~
value, thus we use this value as a reasonable average.

The nominal FWHM linewidth that is created by the **Tb** value is
calculated interactively as you change the widget. Because the linewidth
also depends on the Ta value for each metabolite, there is a "**Ta --
(for LW display only)**" widget that you can set as part of the
linewidth calculation. We recommend that you set it to the **Ta** value
for the metabolite from which you would normally calculate the SNR such
as NAA, Cr or Cho singlets.

### 3.3 Dataset Noise Settings Section

The Dataset Noise Settings section contains parameters that affect the
amount of noise that is added to each simulated spectrum. The data in
the plot on the right will update interactively as you change
parameters. ***Note, the noise displayed is updated every time a
parameter is changed, thus low SNR plots will change appreciably each
time a parameter changes.***

**Background on SNR calculation**

Arrays of random noise are created using the numpy.random.randn() method
which creates random floats sampled from a univariate "normal"
(Gaussian) distribution of mean 0 and variance 1. Two numpy ndarrays of
the proper length are combined to create a complex set of random noise
samples.

The normalized noise is scaled to create a particular SNR setting based
on the traditional "peak height divided by RMS noise value" method. In
DataSim, the RMS noise is taken directly from the randn() method, but
the peak height is measured from a user defined 'reference peak' that is
set up on the Spectral Settings sub-tab. The reference peak is NOT
plotted as part of the final spectrum. Its definition is used to create
a temporary peak at high spectral resolution whose peak height for a
given linewidth and sweep width can be measured. This is the peak height
used to calculate the SNR value displayed in the **Effective SNR**
field.

The reason we use the reference method is that it allows us to keep the
same noise scaling factor as metabolite line width changes. Thus, we can
create DataSims that have the same noise level and the same metabolite
areas but at different peak linewidths. It also allows users to use a
simple definition of SNR in spectra that do not have simple (singlet)
lines against which to set an SNR value.

The default reference line is a singlet peak with 3 spins (aka. --CH~3~
group). The user sets the **Reference Peak Ta** and **Tb** values to
achieve the desired **Effective Linewidth** value and then scales to the
desired SNR level using the **Noise RMS Multiplier** spin control.

Finally, the user can select to turn the noise in the spectrum on/off
using the **Display noise in the spectrum** check box. This is a
convenience function only.

##  4. Metabolite Signals Sub-tab

### 4.1 General

Each datasim tab has four sub-tabs called Spectral Settings, Metabolite
Signals, Macromolecule Signals and Baseline Signals. The Spectral
Settings tab is shown below.

![](media_datasim\media\image7.png){width="6.5in"
height="4.9430555555555555in"}

### 4.2 Metabolite Signals Parameters

A metabolite inclusion range (in PPM) can be set using the 'spectral
resolution' dialog. Depending on the spectral lines in each metabolite,
the metabolite list is repopulated with metabolites that have lines
within the inclusion range. Next, the user has to explicitly select a
metabolite for inclusion by clicking on the check box at the start of a
line in the metabolite list. Metabolite areas and an intrinsic T~2~
decay value can be set in each line for each metabolite. Only the
metabolites with checks are included in the simulated spectrum.

The plot to the right displays the spectrum you are designing. The top
plot shows the summed metabolite + baseline + noise signals. The middle
plot shows the summed metabolite signals (black) overlaid on the
individual metabolite signals (blue). The bottom plot shows the summed
macromolecule + baseline signals (black) overlaid on the individual
baseline signals (blue). You can zoom in/out of this plot the same as
described in Section 2.3. You will likely need to zoom in to clearly see
the lines you are creating.

##  5. Macromolecule Signals Sub-tab 

### 5.1 General

Each datasim tab has four sub-tabs called Spectral Settings, Metabolite
Signals, Macromolecule Signals and Baseline Signals. The Macromolecule
Signals tab is shown below. It functions similarly to the Baseline
Signals tab, and we have included both tabs to allow you to create
non-metabolite signal contributions with both Lorentzian and Gaussian
lineshapes.

![](media_datasim\media\image8.png){width="6.5in"
height="4.9430555555555555in"}

### 5.2 Macromolecule Signals Controls

You can add/delete as many lines to the Macromolecule signals list as
you like using the **Add Line**, **Delete Selected**, **Select All** and
**Select None**. Only lines with a check in them will be affected by the
Delete Selected button. Lines are added to the bottom of the list. You
can sort the list by clicking on the Column label of choice.

Only the lines that have a check in the box will be included in the
calculated macromolecule signal. For each line, you can specify the
**PPM value** for the peak center, the **area** of the peak, a **zero
order phase** and the **line width**.

Line width can be typed into the **Width \[ppm\]** column or the **Width
\[hz\]** column, but not the **Damp \[sec\]** column which is read only.
When you hit enter (or leave the cell) the other columns are updated.
Spectral peaks are updated and displayed with each change. If this
update becomes too slow, hit the Select None button, make your changes
and then check the boxes you want to include again. You can choose to
have either Gaussian or Lorentzian lineshape lines in your model (but
not both) using the **Macromolecule Lineshape** button box.

The **Macromolecule Presets** drop box contain some preset values that
have been used (and listed) in MRS papers. At the moment, these are
mostly from papers from Martin Wilson's lab. NOTE. When you select any
preset other than None, you will [erase all lines]{.ul} that you
currently have in your list.

The **Group Scale** widget allows you to change the areas of all lines
in the Macromolecule model at once. That is, all the values in the
**Area Factor** column are multiplied by the **Group Scale** factor
while the lines are being calculated for display. The values in the
**Area Factor** column will NOT change when you modify the **Group
Scale** value. This can be a convenient way to create a normalized
Macromolecule set of lines and then scale it to best fit the metabolite
areas you have defined.

The **Import HLSVD File** button allows you to select a file that
contains results from the Vespa-Analysis Spectral tab where you have
used the HLSVD water filter sub-tab to fit an MRS data set. The HLSVD
calculated areas, ppm, phase, and damping values shown in that tab can
be saved from the ViewOutput menu to a file and then read into the
DataSim program into either the Macromolecule or Baseline tabs. Why, you
ask? Well, you can estimate a model from a metabolite nulled spectrum
using the HLSVD algorithm. Then you can read that into the DataSim
application and use that model as a noiseless estimate for macromolecule
signals.

The plot to the right displays the spectrum you are designing. The top
plot shows the summed metabolite + baseline + noise signals. The middle
plot shows the summed metabolite signals (black) overlaid on the
individual metabolite signals (blue). The bottom plot shows the summed
macromolecule + baseline signals (black) overlaid on the individual
macromolecule and baseline signals (blue). You can zoom in/out of this
plot the same as described in Section 2.3. You will likely need to zoom
in to clearly see the lines you are creating.

## 6. Baseline Signals Sub-tab 

### 6.1 General

Each datasim tab has four sub-tabs called Spectral Settings, Metabolite
Signals, Macromolecule Signals and Baseline Signals. The Baseline
Signals tab is shown below. It functions similarly to the Macromolecule
Signals tab, and we have included both tabs to allow you to create
non-metabolite signal contributions with both Lorentzian and Gaussian
lineshapes.

![](media_datasim\media\image9.png){width="6.5in"
height="4.9430555555555555in"}

### 6.2 Baseline Signals Controls

You can add/delete as many lines to the Baseline signals list as you
like using the **Add Line**, **Delete Selected**, **Select All** and
**Select None**. Only lines with a check in them will be affected by the
Delete Selected button. Lines are added to the bottom of the list. You
can sort the list by clicking on the Column label of choice.

Only the lines that have a check in the box will be included in the
calculated baseline signal. For each line, you can specify the **PPM
value** for the peak center, the **area** of the peak, a **zero order
phase** and the **line width**.

Line width can be typed into the **Width \[ppm\]** column or the **Width
\[hz\]** column, but not the **Damp \[sec\]** column which is read only.
When you hit enter (or leave the cell) the other columns are updated.
Spectral peaks are updated and displayed with each change. If this
update becomes too slow, hit the Select None button, make your changes
and then check the boxes you want to include again. You can choose to
have either Gaussian or Lorentzian lineshape lines in your model (but
not both) using the **Baseline** **Lineshape** button box.

The **Group Scale** widget allows you to change the areas of all lines
in the Baseline model at once. That is, all the values in the **Area
Factor** column are multiplied by the **Group Scale** factor while the
lines are being calculated for display. The values in the **Area
Factor** column will NOT change when you modify the **Group Scale**
value. This can be a convenient way to create a normalized Baseline set
of lines and then scale it to best fit the metabolite areas you have
defined.

The **Import HLSVD File** button allows you to select a file that
contains results from the Vespa-Analysis Spectral tab where you have
used the HLSVD water filter sub-tab to fit an MRS data set. The HLSVD
calculated areas, ppm, phase, and damping values shown in that tab can
be saved from the ViewOutput menu to a file and then read into the
DataSim program into either the Macromolecule or Baseline tabs. Why, you
ask? Well, you can estimate a model from a metabolite nulled spectrum
using the HLSVD algorithm. Then you can read that into the DataSim
application and use that model as a noiseless estimate for baseline
signals.

The plot to the right displays the spectrum you are designing. The top
plot shows the summed metabolite + baseline + noise signals. The middle
plot shows the summed metabolite signals (black) overlaid on the
individual metabolite signals (blue). The bottom plot shows the summed
macromolecule + baseline signals (black) overlaid on the individual
macromolecule and baseline signals (blue). You can zoom in/out of this
plot the same as described in Section 2.3. You will likely need to zoom
in to clearly see the lines you are creating.

##  7. Results Output 

### 7.1 Plot results to image file formats

The plots displayed in all sub-tabs which contain View panels can all be
saved to file in PNG (portable network graphic), PDF (portable document
file) or EPS (encapsulated postscript) formats to save the results as an
image. The Vespa-DataSim **View** menu lists commands that only apply to
the active DataSim tab and selected processing sub-tab. Select the
**View→OutputPlots→** option and further select either **View to PNG**,
**View to EPS** or **View to PDF** item. The user will be prompted to
pick an output filename to which will be appended the appropriate
suffix.

### 7.2 Plot results to vector graphics formats 

The plots displayed in all sub-tabs which contain View panels can all be
saved to file in SVG (scalable vector graphics) or EPS (encapsulated
postscript) formats to save the results as a vector graphics file that
can be decomposed into various parts. This is particularly desirable
when creating graphics in PowerPoint or other drawing programs. At the
time of writing this, only the EPS files were readable into PowerPoint.

The Vespa-DataSim **View** menu lists commands that only apply to the
active DataSim tab and selected processing sub-tab. Select the
**View→Output→** option and further select either **Plot to SVG**, or
**Plot to EPS** item. The user will be prompted to pick an output
filename to which will be appended the appropriate suffix.

### 

### 7.3 Simulated Data Output to File 

The simulated data can be output to file in a number of formats. In all
cases you will be prompted to select a director/filename for the output.

Use the **DataSim→Export Spectrum** and **DataSim→Export Monte Carlo**
menu items to select if you want to output just the single spectrum
shown on the plot, or if you want DataSim to create an output file with
multiple spectra consisting of copies of the pure metabolite +
macromolecule signals + baseline signals with different noise signals.
Use the **Voxels in Dataset** spin control on the **Spectral Settings**
sub-tab to indicate how many voxels to create in the Monte Carlo output
file. Note, in a Monte Carlo output file the data will be stored as a
two dimension data set. with **Spectral points** and **Voxels in
Dataset** spin control values as the dimensions.

### 7.3.1 VIFF -- Vespa Interchange File Format

Both single spectrum and Monte Carlo datasims can be output to **VIFF**
(Vespa Interchange File Format) **Raw Data** format. In both cases, the
data output is time domain (k-space) data. The **VIFF Raw Data** format
is importable into Vespa-Analysis and has the added benefit of being
able to store a full provenance of the creation of the simulated data in
its XML hierarchy.

Five files are output with provenance stored in each one's header. The
user selects a base filename (fbase) and then extension strings are
added to fbase to indicate the data in each file:

1.  fbase_metabolites.xml - time domain summed metabolite signals, no
    noise

2.  fbase_macromolecules.xml - time domain summed macromolecule signals,
    no noise

3.  fbase_baseline.xml - time domain summed baseline signals, no noise

4.  fbase_noise.xml - the time domain added noise in the summed data

5.  fbase_summed.xml - the sum of the above three files, final spectrum

### 7.3.2 Siemens \*.RDA Format

This is a simple MRS data export format supported on Siemens MR
scanners. It consists of a text header with single "parameter = value"
pairs on each line. At the end of the text header, the double complex
floating point data is appended as a byte encoded string. See Siemens
(non-existent) documentation for more details. However, this format has
the benefit in that it can be read by a variety of MRS processing
programs including LCModel. Vespa-Analysis can also read this format.

Only a single spectrum result can be saved to the **Siemens \*.RDA**
file format. Six files are output, five data and one provenance. The
user selects a base filename (fbase) and then extension strings are
added to fbase to indicate which data is in the file:

1.  fbase_metabolites.rda - time domain summed metabolite signals, no
    noise

2.  fbase_macromolecules.rda - time domain summed macromolecule signals,
    no noise

3.  fbase_baseline.rda - time domain summed baseline signals, no noise

4.  fbase_noise.rda - the time domain added noise in the summed data

5.  fbase_summed.rda - the sum of the above three files, final spectrum

6.  fbase_provenance.rda - text file, info about Vespa-DataSim setting
    used to create the above files. This is created because Siemens RDA
    has limited ability to store provenance information within its
    header.

# 
