# VIFF (XML) Version History
The objects that we write to [wiki:VIFF] embed a version string so that when
we need to change the VIFF format, our code can tell the difference between
the new and old formats. Note that the version string is associated with 
individual elements (e.g. experiments, pulse projects, etc.); there is not
one monolithic VIFF version. The version numbers for one object's format can
change indepdendently of the others.

Once a VIFF version is released "into the wild", we have to support it 
forever.

This document describes the differences from one VIFF version to another. As
of this writing (July 2011), only experiments and simulations have changed
from their original version (1.0.0).


## Experiments and Simulations
### VIFF Version 1.0.0
Used in Vespa < 0.2.4. 

Vespa < 0.1.6 didn't write version info on anything but the root element 
(`vespa_export`).

Here's an example of 
[browser:/trunk/common/resources/experiments.xml?rev=2000 experiments.xml with versions on the subelements]
and 
[browser:/trunk/common/resources/experiments.xml?rev=1739 one without (as used in Vespa < 0.1.6).]


### VIFF Version 1.1.0
Used in Vespa >= 0.2.4.

In VIFF 1.1.0, simulations are much more compact.

In VIFF 1.0.0, the following is true --

1. Each `simulation` element is a direct child of the `experiment` element.
1. Each `simulation` element has a version attribute so the string 
    `version="1.0.0"` repeats for each simulation (which is just
    a waste of space).
1. Each `simulation` element has a `spectrum` element that contains 0 or 
    more `line` elements. Each `line` contains a `ppm`, `area` and `phase`
    element each of which in turn contains a single float.

In 1.1.0, here's how those change.

1. We added a layer between the `experiments` element and the simulations 
    in the form of a `simulations` element. Contrast --
    
    Version 1.0.0 ---
    ```
    <experiment version="1.0.0">
        <simulation version="1.0.0">
            ...
        </simulation>
        <simulation version="1.0.0">
            ...
        </simulation>
        <simulation version="1.0.0">
            ...
        </simulation>
    ```
    
    Version 1.1.0 --
    ```
    <experiment version="1.1.0">
        <simulations version="1.1.0">
            <simulation>
                ...
            </simulation>
            <simulation>
                ...
            </simulation>
            <simulation>
                ...
            </simulation>
        </simulations>
    ```
    
    The `simulations` element serves two purposes. First, it gives us a place
    to store the VIFF version without repeating it on every simulation. 
    Second, gives XML text editors a tag they can fold to hide the simulations.
1. As shown above, the XML version moved from the `simulation` elements
    to the `simulations` element.
1. We did away with the `spectrum` element entirely by representing the 
    ppm, area and phase info as [encoded arrays](/wiki:VIFF#BinaryData/) and
    making them subelements of the `spectrum` element.
    
    Version 1.0.0 ---
    ```
    <experiment version="1.1.0">
        <simulation version="1.0.0">
            <started>2011-01-24T11:00:00</started>
            <completed>2011-01-24T11:00:00</completed>
            <metabolite_id>f03efaa3-d686-41db-8df2-8a2e450f596b</metabolite_id>
            <dim>0.0</dim>
            <dim>0.0</dim>
            <dim>0.0</dim>
            <spectrum version="1.0.0">
                <line>
                    <ppm>3.185</ppm>
                    <area>3.0</area>
                    <phase>0.0</phase>
                </line>
            </spectrum>
        </simulation>
    ```

    Version 1.1.0 ---
    ```
    <experiment>
        <simulations version="1.1.0">
            <simulation>
                <started>2011-01-24T11:00:00</started>
                <completed>2011-01-24T11:00:00</completed>
                <metabolite_id>f03efaa3-d686-41db-8df2-8a2e450f596b</metabolite_id>
                <dim>0.0</dim>
                <dim>0.0</dim>
                <dim>0.0</dim>
                <ppms data_type="float64" encoding="xdr zlib base64" shape="1">eNpz4Kx66L5OpBoADVEDKQ==</ppms>
                <areas data_type="float64" encoding="xdr zlib base64" shape="1">eNpz4GAAAwACQABJ</areas>
                <phases data_type="float64" encoding="xdr zlib base64" shape="1">eNpjYIAAAAAIAAE=</phases>
            </simulation>
        </simulations>
    </experiment>
    ```
    
