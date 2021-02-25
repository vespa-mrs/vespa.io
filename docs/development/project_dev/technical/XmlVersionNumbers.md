# XML Versions
This technical document explains the version numbers Vespa writes
into the XML (VIFF files) it creates. They have not turned out to be as useful
as we expected.

## Introduction
In all of the XML (VIFF files) written by Vespa, we write a `version` attribute
on major blocks. This is not to be confused with the Vespa version information
which is written into a comment at the top of each VIFF file.

For instance, in the sample below (taken from a real file) 
there are version attributes on the top level `vespa_export` element, the
`dataset` element, and the `user_prior` element --

```
#!xml
<vespa_export version="1.0.0">
	<!--
This XML file is in Vespa Interchange File Format (VIFF). You can download
applications that read and write VIFF files and learn more about VIFF here:
http://scion.duhs.duke.edu/vespa/

It was created with Vespa version 0.6.4.
-->
	<timestamp>2013-01-18T17:28:39</timestamp>
	<comment />
	<dataset id="2b92bc53-d98d-48ea-a60e-d374658926b2" version="1.1.0">
		<user_prior version="1.0.0">
			<auto_b0_range_start>1.7</auto_b0_range_start>
			<auto_b0_range_end>3.4</auto_b0_range_end>
			<auto_phase0_range_start>1.85</auto_phase0_range_start>
```

## Purpose
The purpose behind these was to allow us developers to change the XML format
as necessary without breaking our ability to read in XML files written by older
versions of Vespa. For instance, in version 1.0.0 of Analysis' dataset XML, 
there was a `block_basic` element that moved to a `user_prior` element in 
subsequent versions. Our code can read both the older and newer formats.

## In Practice
In practice, the XML versions aren't very useful for two reasons. 

First, as far as I can tell, in every instance where we've changed an XML
version number, the change to the version number has been superfluous. For
instance, in the example mentioned above where `block_basic` was eliminated in
favor of `user_prior`, the XML version is just a proxy for the presence of a
`block_basic` element.

Our current code does this -- 

```
#!python
if xml_version == "1.0.0":
    for i, block_element in enumerate(block_elements):
        if block_element.tag == "block_basic":
            break
    # ...change block_basic into a user_prior element...
```

But it could just as well do this --

```
#!python
block_basic = block_elements.find("block_basic")
if block_basic is not None:
    # ...change block_basic into a user_prior element...
```

IMO the second version is clearer because it explicitly tests for the condition
in which it's really interested.

The fact that the version number is superfluous was emphasized by the fact 
that Vespa 0.6.1 changed the dataset XML format, but the XML version number 
wasn't changed due to an oversight. The practical consequences of this were
nil (or None, to be Pythonic).

A second, less important reason that the XML version numbers are not as useful
as they could be is that the format is unnecessarily complex. I (Philip) made 
the bad
choice of using app-style version numbers in x.y.z format. A simple integer
would have been sufficient and easier to work with (especially in comparisons).

The x.y.z format orders as one would hope (e.g. '1.0.0' < '1.0.1', and
'2.9.9' < '3.0.0') but such ordering is not as intuitive as simple int
comparison.


## Conclusion
I'm not ready to advocate abandoning the XML version numbers yet. There might 
be a case where they're necessary, we just haven't come across it yet. Currently
it costs us next to nothing to keep writing them to the XML, and if we find
we need them we'll be glad they're there. 

