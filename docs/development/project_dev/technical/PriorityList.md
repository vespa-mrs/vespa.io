
# Vespa ToDo Priorities

## High Priority
 * Brian: sketch new Analysis architecture with fixed processing blocks and associated 'BlockRawHybrid' magic
 * DONE - Analysis - create workflow for reading and processing edited SVS pulse sequence data (see above)
 * DONE - Brian/Philip: work with list to add GE and Bruker data import
 * Brian: review FIXMEs 
 * DONE - Analysis - saved workspaces (preset files)
 * Analysis - command line
 * all apps - decide - preferences dialog? 
 * DONE - Analysis - write/append fit results to CSV or tabbed ASCII file

## Medium Priority
 * RFPulse - off-resonance profiles contour plots
 * howto videos
 * RFPulse - new transformations (concat?)
 * review how Simulation operates. Maybe a new UUID every time user  hits save?
 * Analysis - outline work needed to add SI data handling and processing
 * Analysis - spatial
 * Simulation - workflow for creating and displaying edited pulse sequence Experiments

## Low Priority
 * concentrated focus on adding unit tests
 * Simulation - vertical scale on Visualize tab


## Completed
 * Philip: assess if dynamic_list_xxxx.py modules can share a base class
 * Analysis - collate and standardize all ppm utility calls
 * Analysis - disconnect Chain result arrays from View plot displays, return as a dict to Tab after Chain.run()
 * Analysis - rework block/chain/view architecture (design then implement) BJS-much cleaner now
 * Analysis - math tabs (deprecated for associated Add/Sub BlockRaw and BlockRawHybrid architecture)
 * Analysis - delete tabs (should be dealt with in new architecture)
 * main wiki - include priorset when discussing the apps in the Vespa suite
 * port Sima HLSVD to Python
 * Philip & Brian: review scion setup
 * Analysis - re-optimize the fileio reader model to make it as clear and simple as possible
 * contrib Trac instance
 * develop a wxPython 2.9 strategy
 * test wxPython 2.9
 * Analysis - use Sima HLSVD
 * decide - Release prior app?
 * Share Twix code with Siemens geeks (mailing list?)
 * drop support for Python 2.5. It's not holding us back, but it won't get tested once Philip is gone
 * review all open tickets
 * develop a 64-bit strategy
 * all apps - decide - relax name rules?
 * improve GAMMA wiki pages
 * A thank you to open source projects without which our work would not have been possible.
 * downloadable prebuilt virtual instance.
 * work out a way to do off-site backups that doesn't involve Philip
 * Simulation - multiple simultaneous experiment visualizations ([simulation:ticket:15 ticket 15])
 * figure out how to create/get Windows binaries for pywavelets for Python 2.7
 * Need to revisit plot_options messiness
 * Philip & Brian: training, how to do a release
 * Philip & Brian: review vespa.bugs@gmail.com setup
 * Philip & Brian: review database upgrade procedure
 * Philip & Brian: training, database management+extension
 * Philip: document native Python HLSVDPro code, find it a home?
 * Philip & Brian: training, SVN methodologies
 * Philip & Brian: training, Trac methodologies
 * Philip: change Dataset.get_source_data() to return left neighbor
 * Philip: add a BlockSpatialIdentity to Dataset blocks list to test self.data pass-through and inflate/deflate magic