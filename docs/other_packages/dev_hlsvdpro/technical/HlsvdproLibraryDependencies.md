# HLSVDPRO Library Dependencies
This document discusses some of the libraries that HLSVDPRO depends on
and how (and why) they're linked statically or dynamically.

## Main Dependencies
HLSVDPRO depends principally on the GFortran runtime library. It might also depend on some low-level system libraries, but we'll ignore them for the purpose of this document.

## Why So Much Static Linking?
HLSVDPRO was built for the [Vespa project](http://scion.duhs.duke.edu/vespa/).
As of this writing, all support comes from that project. As a result, the HLSVDPRO package is tuned to the needs of Vespa.

We want to make the install process for Vespa as simple as possible. It's important to us that HLSVDPRO doesn't add dependencies for Vespa users.

Ironically, the version of the GFortran runtime library that HLSVDPRO uses is old and may not be available on some popular modern Linuxes (Ubuntu 20.04 LTS being a prime example). Rather than sending users on a wild goose chase to hunt down this library, we link it statically.

In general, we link statically where possible, and provide the library when static linking is not possible.
