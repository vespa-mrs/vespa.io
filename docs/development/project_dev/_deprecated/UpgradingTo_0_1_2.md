# Upgrading to Version 0.1.2
There's [PulseSequenceInterfaceChange a new pulse sequence code interface] in 
version 0.1.2 that breaks compatibility with the old interface. Existing
pulse sequences won't work with the new interface. This guide outlines the
most comfortable way to upgrade to Vespa 0.1.2 from an older version.


## Before You Upgrade
Your current Vespa install came with three sample experiments and six sample 
pulse sequences.
None of them will work after the upgrade. You'll get updated, working
versions of these examples when you upgrade, so there's no point to keeping
the old, broken examples around.

To delete the examples, use the experiment management dialog (under 
Simulation's `Management` menu item) to delete the three experiment
examples. Then use the pulse sequence management dialog to delete the 
six pulse sequence examples (CP-PRESS with Variable R-groups, JPRESS Ideal,
One-Pulse, PRESS Ideal, STEAM Ideal and Spin-Echo).

## Upgrade
Upgrade Vespa using the [upgrade instructions](/wiki:Upgrading/).


## After You Upgrade
Any custom experiments or pulse sequences that you have need to be migrated to
the new interface. It's easiest to migrate the pulse sequences first.

### Migrating an Existing Pulse Sequence
If the pulse sequence is
[simulation:wiki:Concepts#FrozenExperimentsMetabolitesandPulseSequences frozen],
you'll need to clone it before you can edit the sequence and binning code.
In the management dialog, select the pulse sequence and click the `Clone`
button.

Next, edit the pulse sequence and 
[#HowToMigrateExistingSequenceandBinningCode change the code to use the new interface].
You should test it to make sure it's working properly.

If you have trouble, let us know via 
[the Vespa mailing list](https://groups.yahoo.com/neo/groups/vespa-mrs/info).


### Migrating an Existing Experiment
Assuming you've already migrated the pulse sequence, here's the the steps
to migrate an experiment. 

1. Open the experiment.
1. Use the `Copy Tab to New` item on the Experiment menu.
1. Change the experiment's pulse sequence to a version that uses the 
 new interface.
1. Re-run the experiment.

If you have trouble, let us know via 
[the Vespa mailing list](http://tech.groups.yahoo.com/group/vespa-mrs/).


## How To Migrate Existing Sequence and Binning Code
1. *Make your code look like a module with a function.* Indent your 
 existing code one level and add this header (unindented):
```
#!python
import pygamma as pg
 
def run(sim_desc):
```
 You're free to name the `sim_desc` parameter anything that 
 makes sense to you. Similarly, you're not compelled to alias the pygamma
 module.
1. *Rename all instances of `sim_dict`.* Rename them to match the 
 parameter name you chose (e.g. `sim_desc`).
1. *Switch from dictionary key access to object.attribute.* The attributes
 of the simulation description class are named the same as the dictionary
 keys of the old interface, so this is a simple syntax change. For example, 
 change this:
```
#!python
b0 = sim_dict["field"]
```
 to this:
```
#!python
b0 = sim_desc.field
```
1. *Change spin system references.* The old interface provided a variable
 called `sys` which contained a PyGAMMA spin system object. That object is 
 now an attribute called `spin_system` on the object that's passed to your 
 code. You'll want to change `sys` to `sim_desc.spin_system`.
1. *Change your binning code to return ppm, area and phase.* Most code 
 can just add this line to the end of the binning function:
```
#!python
return (ppm, area, phase)
```

Remember, you can always refer to the sample pulse sequences in Simulation
as a programming guide.


## Before and After Example
Here's an example using the sequence and binning code from the One Pulse 
pulse sequence example. 

### One Pulse Sequence Code Before
```
#!python
#------------------------------------------------------------------------------
# This is an example PyGamma pulse sequence for use in Vespa-Simulation
#
# A timing diagram for this pulse sequence can be found in the Appendix 
# of the Simulation User Manual.
#------------------------------------------------------------------------------

# set up steady state and observation variables
#
# NB. 'sys' is a spin_system object that is provided by the Vespa-Simulation
#        program as a convenience to users.  It can be overwritten or not used
#        as preferred by the user.

H   = pg.Hcs(sys) + pg.HJ(sys) 
D   = pg.Fm(sys, "1H") 
ac  = pg.acquire1D(pg.gen_op(D), H, 0.000001) 
ACQ = ac 

# excite and acquire the data
sigma  = pg.sigma_eq(sys) 
sigma0 = pg.Iypuls(sys, sigma, "1H", 90.0) 

# instantiate transition table of simulation results
# 'mx' is a required named variable for use in the 
# binning code execution.

mx     = ACQ.table(sigma0)
```

### One Pulse Sequence Code After

```
#!python
import pygamma as pg

def run(sim_desc):
    #------------------------------------------------------------------------
    # This is an example PyGAMMA pulse sequence for use in Vespa-Simulation
    #
    # A timing diagram for this pulse sequence can be found in the Appendix 
    # of the Simulation User Manual.
    #------------------------------------------------------------------------
    spin_system = sim_desc.spin_system

    # set up steady state and observation variables
    H   = pg.Hcs(spin_system) + pg.HJ(spin_system) 
    D   = pg.Fm(spin_system, "1H") 
    ac  = pg.acquire1D(pg.gen_op(D), H, 0.000001) 
    ACQ = ac 

    # excite and acquire the data
    sigma  = pg.sigma_eq(spin_system) 
    sigma0 = pg.Iypuls(spin_system, sigma, "1H", 90.0) 

    # instantiate and save transition table of simulation results
    sim_desc.mx = pg.TTable1D(ACQ.table(sigma0))
```

### One Pulse Binning Code Before
```
#!python

area   = pg.DoubleVector(0)
ppm    = pg.DoubleVector(0)
phase  = pg.DoubleVector(0)
field  = sys.Omega()
nspins = sys.spins()
tolppm = float(sim_dict["blend_tolerance_ppm"])
tolpha = float(sim_dict["blend_tolerance_phase"])
ppmlow = float(sim_dict["peak_search_ppm_low"])
ppmhi  = float(sim_dict["peak_search_ppm_high"])

bins = mx.calc_spectra(ppm, area, phase, field, nspins, tolppm, tolpha, ppmlow, ppmhi)

if bins > 0:
    area  = [i for i in area]
    ppm   = [i for i in ppm]
    phase = [i for i in phase]
else:
    area  = []
    ppm   = []
    phase = []
```

### One Pulse Binning Code After
```
#!python
import pygamma

def run(sim_desc):
    area   = pygamma.DoubleVector(0)
    ppm    = pygamma.DoubleVector(0)
    phase  = pygamma.DoubleVector(0)
    field  = sim_desc.field
    nspins = sim_desc.nspins
    tolppm = sim_desc.blend_tolerance_ppm
    tolpha = sim_desc.blend_tolerance_phase
    ppmlow = sim_desc.peak_search_ppm_low
    ppmhi  = sim_desc.peak_search_ppm_high

    bins = sim_desc.mx.calc_spectra(ppm, area, phase, field, nspins, tolppm, tolpha, ppmlow, ppmhi)
    
    return (ppm, area, phase)
}}}