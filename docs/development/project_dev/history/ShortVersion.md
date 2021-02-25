# Vespa Overview - the Novel
VeSPA is a project, the goal of which is to utilize current software engineering "best practices" to refactor 3 existing and widely used MRS software packages, written by the authors and colleagues, to create an integrated open source package for performing and analyzing MRS experiments. VeSPA, the resulting integrated package, provides a greatly enhanced, more complete, easier to use, easier to extend set of tools for MRS simulation and analysis. 

The original applications were written in closed source languages ([GAVA/Gamma](http://cds.ismrm.org/ismrm-2003/0852.pdf) and IDL_Vespa in [IDL](http://www.ittvis.com/ProductServices/IDL.aspx), and [MatPulse](http://www.rrmind.research.va.gov/software/matpulse.asp) in [Matlab](http://www.mathworks.com/)) that have licensing issues (primarily restricted use and substantial fees) that make their use for scientific collaboration problematic, as well as make them relatively difficult to extend and virtually impossible to integrate. Rewriting the applications in the open source language, [Python](http://www.python.org/), and utilizing the powerful [NumPy](http://numpy.scipy.org/), [SciPy](http://www.scipy.org), and [Matplotlib](http://matplotlib.sourceforge.net/) libraries allows for a clean, robust, full featured and open source (i.e. FREE) integration of the packages. It provides a much more natural work flow for researchers as well as making the integrated package much more easily extended by those who need added functionality. As an example it has been straightforward for the authors to add functionality corresponding to recent developments in MRS, providing substantial added value to the integrated VeSPA package for a modest coding effort.

One of the goals of the earlier individual packages as well as the integrated package is to provide sophisticated tools to non experts who would otherwise have great difficulty in taking advantage of capabilities that have become available to researchers in MRS. 

The original MatPulse package, written by Professor Gerald Matson, encapsulated a large body of knowledge regarding RF pulse design and allowed users with relatively little experience to explore and utilize that knowledge in a straightforward manner that resulted in rapid development of useful RF pulses. 


Similarly the gamma NMR simulation library written by Dr. Scott Smith allowed users with with limited knowledge of the underlying quantum mechanical details to write C++ programs that explored the effects of various pulse and pulse sequence designs using full quantum mechanical density matrix calculations. The GAVA/Gamma package was an attempt to further simplify access to NMR simulations by providing a graphical interface to a subset of the gamma library thus freeing users with no knowledge or interest in C++ programming to explore the effects of pulse and pulse sequence designs. The Simulation component of VeSPA goes even further by using the SWIG package to provide a python interface to gamma, referred to as pygamma. Simulation itself provides a graphical interface with powerful plotting and analysis functionality that is built on top of pygamma. But pygamma can be be used independently to produce powerful NMR simulations in python with the majority of the calculations performed in underlying fast C++ code. 

The Analysis component of VeSPA provides an updated, greatly extended, python version of the IDL_Vespa spectral fitting package originally written by the authors and colleagues. The updating and integration of these 3 packages provides greatly enhanced possibilities for exploring, developing, and analyzing MRS experiments.         

# Spectral Simulation References
De Graaf AA, Bovee WMMJ. Improved quantification of in vivo 1H NMR spectra by optimization of signal acquisition and processing and by incorporation of prior knowledge into the spectral fitting. Magn Reson Med 1990;15:305-319.

Provencher SW. Estimation of metabolite concentrations from localized in vivo proton NMR spectra. Magn Reson Med 1993;30(6):672-679.

Graveron-Demilly D, Diop A, Briguet A, Fenet B. Product-operator algebra for strongly coupled spin systems. J Magn Reson 1993;101:233-239.

Smith SA, Levante TO, Meier BH, Ernst RR. Computer simulations in magnetic resonance. An object-oriented programming approach. J Magn Reson 1994;A106:75-105.

Matson GB. An integrated program for amplitude-modulated RF pulse generation and re-mapping with shaped gradients. Magn Reson Imaging 1994;12(8):1205-1225.

Allman T, Bain A, Garbow J. SIMPLTN, a Program for the Simulation of Pulse NMR Spectra. J Magn Reson 1996;A123(1):26-31.

Slotboom J, Boesch C, Kreis R. Versatile frequency domain fitting using time domain models and prior knowledge. Magn Reson Med 1998;39:899-911.

Soher BJ, Young K, Govindaraju V, Maudsley AA. Automated spectral analysis III: Application to in vivo proton MR spectroscopy and spectroscopic imaging. Magn Reson Med 1998;40:822-831.

Young K, Soher BJ, Maudsley AA. Automated spectral analysis II: Application of wavelet shrinkage for characterization of non-parameterized signals. Magn Reson Med 1998;40:816-821.

Young K, Govindaraju V, Soher BJ, Maudsley AA. Automated spectral analysis I:  Formation of a priori information by spectral simulation. Magn Reson Med 1998;40:812-815.

Young K, Matson GB, Govindaraju V, Maudsley AA. Spectral simulations incorporating gradient coherence selection. J Magn Reson 1999;140:146-152

Ebel A, Soher BJ, Maudsley AA. Assessment of 3D 1H NMR echo-planar spectroscopic imaging using automated spectral analysis. Magn Reson Med 2001;46:1072-1078.

Naressi A, Couturier C, Devos JM, Janssen M, Mangeat C, de Beer R, Graveron-Demilly D. Java-based graphical user interface for the MRUI quantitation package. Magma 2001;12(2-3):141-152.

Thompson RB, Allen PS. Response of metabolites with coupled spins to the STEAM sequence. Magn Reson Med 2001;45:955-965.

Soher BJ, Maudsley AA. Evaluation of variable line-shape models and prior information in automated 1H spectroscopic imaging analysis. Magn Reson Med 2004;52(6):1246-1254.

Maudsley A, Govindaraju V, Young K, Aygula Z, Pattany PM, Soher BJ, Matson G. Numerical simulation of PRESS localized MR spectroscopy. J Magn Reson 2005;173(1):54-63.

Kim H, Thompson RB, Hanstock CC, Allen PS. Variability of metabolite yield using STEAM or PRESS sequences in vivo at 3.0 T, illustrated with myo-inositol. Magn Reson Med 2005;53(4):760-769.

Veshtort M, Griffin RG. SPINEVOLUTION: a powerful tool for the simulation of solid and liquid state NMR experiments. J Magn Reson 2006;178:248-282.

Soher BJ, Young K, Bernstein A, Aygula Z, Maudsley AA. GAVA: spectral simulation for in vivo MRS applications. J Magn Reson. 2007;185(2):291-299.

Kaiser LG, Young K, Matson G. Elimination of spatial interference in PRESS-localized editing spectroscopy. Magn Reson Med 2007;58(4):813-818.

Kaiser LG, Young K, Meyerhoff D, Mueller SG, Matson G. A detailed analysis of localized J-difference GABA editing: theoretical and experimental study at 4 T. NMR Biomed 2008;21(1):22-32.

