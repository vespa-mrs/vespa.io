# Acknowledgements
We are deeply grateful to many colleagues and open source projects without whom and which Vespa would not have been possible. They are listed below in rough order of significance. Ranking one as absolutely more important than another is doomed to be unfair, so please don't read too much into the order we've chosen.

First and foremost, thanks to the [National Institutes of Health](http://www.nih.gov/) for funding this through grant number 1R01EB008387-01A1. 

Vespa's PIs (Dr. Brian Soher and Dr. Karl Young) would also like to thank Vespa's main developers: Philip Semanchuk and David Todd.

## Colleagues
 * [Dr. Gerald (Jerry) Matson](http://www.cind.research.va.gov/staff/matsong.asp) for Matpulse and expertise
 * Dr. Scott A. Smith et al for [(Py)GAMMA](http://scion.duhs.duke.edu/vespa/gamma/)
 * Lana Kaiser, Assaf Tal, Uzay Emir for code and advice.

## MatPulse
MatPulse is a solo masterpiece by Jerry Matson as part of his long and distinguished career at UC San Francico. It is a tool for producing optimized RF pulses for use in a variety of magnetic resonance investigations. Much of the work on this program has been 'cumulative' across the years. Dr. Matson has consulted extensively with us on which parts of MatPulse should be included in Vespa-RFPulse.

## GAVA
GAVA is the creation of Brian Soher, Karl Young, Aaron Berstein and Zakaria Aygula with funding and inspiration from Andrew Maudsley at UC San Francico. This program was of course motivated by and made possible by the graduate work of Scott Smith who developed the GAMMA C++ spectral simulation library. Dr. Andrew Maudsley had both the inspiration (and funding) to want to make this resource available more easily to others in the clinical magnetic resonance world. Young and Berstein created the initial infrastructure for simulation under Linux. Soher translated this to Windows and wrapped it in an IDL GUI and GAVA was 'born'. Soher, Young and Aygula all worked on maintaining GAVA on Windows and Linux, and towards extending the ability of simulations to account for 'real world' condition while at University of Miami. Soher aquired funding for maintaining and extending GAVA into the Vespa-Simulation application in 2008.

## Metabolite Information
The metabolite prior information that populates the startup database and makes all the PyGamma simulations possible was derived from the stellar publication by Varanavasi Govindaraju (Govind!), Karl Young and Andrew Maudsley, in NMR in Biomedicine, Vol.13, pages 129-153. While there have been a few other contributions towards these values, this work is by far the keystone towards accurate and robust spectral simulation around.

## IDL Vespa (the ancestor of Vespa-Analysis)
IDL Vespa was written by Brian Soher at Duke. Like many great things, or hopefully great things, this program came about out of laziness. As part of Dr. Soher's work with Andrew Maudsley at UC San Francisco and Miami, The SITools application toolbox for processing large spectroscopy data sets was slowly morphing into something ever larger and more regimented towards large data sets. This made testing small changes as well as new algorithms a long and tedious chore. Dr. Soher developed IDL_Vespa to handle smaller spectroscopy data sets and to be easier to use as a test bed for other changes.

## Open Source Projects
 * [Python](http://www.python.org/)
 * [SQLite](http://www.sqlite.org/)
 * [wxWidgets/wxPython](http://wxpython.org/)
 * [wxGlade](http://wxglade.sourceforge.net/)
 * [numpy](http://numpy.scipy.org/)
 * [scipy](http://www.scipy.org/)
 * [matplotlib](http://matplotlib.sourceforge.net/)
 * [gcc and gfortran](http://gcc.gnu.org/)
 * [Trac](http://trac.edgewall.org/)
 * [Subversion](http://subversion.tigris.org/)
 * Linux (especially [Ubuntu](http://www.ubuntu.com/), [Fedora](http://fedoraproject.org/), [Red Hat](http://www.redhat.com/), [Mint](http://linuxmint.com/) and [Lubuntu](http://lubuntu.net/))
 * [Apache](http://www.apache.org/)
 * [GNU tools](http://www.gnu.org/) (especially for giving me a replacement for OS X [grep](http://www.gnu.org/software/grep/))
 * [HLSVD](http://scion.duhs.duke.edu/vespa/analysis/wiki/HlsvdOverview) by Laudadio, Sima and Larsen, and also the version from the [MRUI project](http://www.mrui.uab.es/)
 * [VirtualBox](https://www.virtualbox.org/)
 * [PyDicom](http://code.google.com/p/pydicom/)
 * [PyWavelets](http://www.pybytes.com/pywavelets/)
 * [WWW SQL Designer (Ondrej Zara)](http://code.google.com/p/wwwsqldesigner/)
 * [Eclipse](http://www.eclipse.org/)
 * [TortoiseSVN](http://tortoisesvn.net/)
 * [BLAS](http://www.netlib.org/blas/) and [LAPACK](http://www.netlib.org/lapack/)
 * [FFTW](http://www.fftw.org/)
 * [nmrglue](http://code.google.com/p/nmrglue/)
 * [GDCM (Grassroots DICOM)](http://sourceforge.net/apps/mediawiki/gdcm)
 * [ATT Bell Laboratories](http://www.research.att.com/) (for f2c and Lowess code)
 * [NASA](http://idlastro.gsfc.nasa.gov/) (for minf_parabolic_info code)
 * [LibreOffice](http://www.libreoffice.org/)
 * [ConfigObject](https://hg.gawel.org/ConfigObject/)
 * [Cyberduck](http://cyberduck.ch/)
 * [Transmission Bit Torrent client](http://www.transmissionbt.com/)
 * [Pydev](http://pydev.org/) plugin for Eclipse