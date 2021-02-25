## Motivation for the Vespa Project
#### History
Vespa was born out the combination of three applications called RFPulse, Simulation and Analysis that were migrated from three previous standalone applications:

    * RFPulse <-> [MatPulse](http://www.rrmind.research.va.gov/software/matpulse.asp) - software for RF pulse design written in [Matlab](http://www.mathworks.com/)
    * Simulation <-> [GAVA](http://cds.ismrm.org/ismrm-2003/0852.pdf) - software for spectral simulation written in [IDL](http://www.ittvis.com/ProductServices/IDL.aspx) (along with the [GAMMA](https://scion.duhs.duke.edu/vespa/gamma) package written in C++).
    * Analysis <-> IDL_Vespa - a package for spectral data processing and analysis written in [IDL](http://www.ittvis.com/ProductServices/IDL.aspx)

#### Limitations
Some limitations of the previous MRS tools:
  * Non-standard data access
  * Complexities of integrating multiple languages
  * Closed-source software that complicates algorithm extension and free sharing
  * Lack of integration between programs for sharing prior information
  * Incomplete or missing documentation and educational content

#### Solutions
The new VeSPA project addresses these limitations as follows:
  * Create a free, liberally-licences (BSD) open source MRS toolset
  * Build it on top of the Python language with it's vast library of integration tools
  * Make sure there are straight forward ways for user community expansion
  * Have results saved into a free SQL database (Sqlite) which can be searched and queried
  * Enable the export of pulse sequences, experiments, rfpulses, etc. into an XML format that other Vespa users can then Import into their own local Vespa platforms