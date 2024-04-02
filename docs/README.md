#  Overview of the Vespa MRS Tools Package

Vespa is an integrated, open source, open development platform for magnetic resonance spectroscopy (MRS) research. It contains four  software applications, written in Python, called: 

1. Pulse      - for RF pulse design
2. Simulation - allows spectral simulation and prototyping
3. DataSim    - an application for creating synthetic MRS data sets 
4. Analysis   - interactive spectral data processing and analysis

These applications can be run separately, but can also communicate via a shared database of objects/results. Integration allows one application to use the output from another as input. For example, Simulation can make use of an RF pulse designed in Pulse to create a more realistic MR simulation.

The Vespa project addresses software limitations seen across the MRS field, including: non-standard data access, closed source multiple language software that complicates algorithm extension and comparison, lack of integration between programs for sharing prior information, and incomplete or missing documentation and educational content.

## Acknowledgements

This work has been supported by NIH grants: R01 EB008387, R01 EB000207, R01 NS080816 and R01 EB000822

## Citation

If you publish material that makes use of Vespa, please cite the following publication:

Soher B, Semanchuk P, Todd D, Ji X, Deelchand D, Joers J, Oz G and Young K. Vespa: Integrated applications for RF pulse design, spectral simulation and MRS data analysis. Magn Reson Med. 2023 Sep;90(3):823-838. doi: 10.1002/mrm.29686. Epub 2023 May 15. PMID: 37183778; PMCID: PMC10330446.

**Other Resources**

The Vespa project and each of its applications have GitHub Pages User Manuals with extensive information about how to use, and develop new functionality, for each application. 

More technical information for the Vespa Project as a whole, and for each application specifically, can be found in the DEVELOPMENT Pages

**_Note. These GitHub Pages are translations of earlier Trac documents. We are still weeding through them to get all the links and formatting sorted out.  Thank you for your patience._**