# Upgrading to Version 0.3.0
Vespa 0.3.0 contains two distinct and important changes that particularly 
affect users upgrading from a previous version.

## First Change - New Sample Experiments and Pulse Sequences
Your current Vespa install came with three sample experiments and six 
or seven sample pulse sequences. Vespa 0.3.0 contains slightly improved 
versions of all of them and adds an entirely new sample pulse sequence.
The new pulse sequence "PRESS with RFPulse Pulses" demonstrates Simulation's
new ability to use RFPulse pulses.

Rather than clutter up your database by adding all the new examples
automatically, we thought we should let you add them more cleanly. Here's how.
The instructions assume you've already upgraded to Vespa 0.3.0.


### Add the Experiments
1. Download [this experiments.xml file](http://scion.duhs.duke.edu/vespa/project/browser/tags/0_3_0/common/resources/experiments.xml) to your Desktop.
 
1. Use the experiment management dialog (under Simulation's `Management` 
 menu item) to delete the three experiment examples.
1. Use the experiment management dialog to import the file you downloaded
 in step 1. That will replace the examples you just deleted.
 

### Add the Pulse Sequences
1. Download [this pulse_sequences.xml file](http://scion.duhs.duke.edu/vespa/project/browser/tags/0_3_0/common/resources/pulse_sequences.xml) to your Desktop.
 
1. Use the pulse sequence management dialog (under Simulation's `Management` 
 menu item) to delete the 
 six or seven pulse sequence examples: CP-PRESS with Variable R-groups, 
 JPRESS Ideal, One-Pulse, One-Pulse No Binning (which you might not have), 
 PRESS Ideal, STEAM Ideal and Spin-Echo.
1. Use the pulse sequence management dialog to import the file you downloaded
 in step 1. That will replace the examples you just deleted.
 


## Second Change - Export Bug Fixed
When you export an object (like an experiment) from Vespa, Vespa irrevocably
marks it as "public" to try to safeguard its integrity. Public objects are 
"frozen" which means they're almost entirely uneditable. This worked correctly
in Vespa versions prior to 0.3.0, but Vespa failed to mark referenced objects
as public. 

For instance, if I exported an experiment, the experiment would
be marked public but not the metabolites and pulse sequence that it 
referenced. Since the metabolites and pulse sequence are integral parts of 
the experiment, failing to mark them public was a big oversight.

Vespa 0.3.0 corrects that problem. For instance, if I export an experiment
that references a pulse sequence that references a pulse project (which is
newly possible in 0.3.0), then the experiment, its metabolites, its pulse
sequence and the pulse project would all be marked public.

This new behavior is the correct behavior, but it's a change from prior
versions of Vespa so we wanted to make the difference absolutely clear.




