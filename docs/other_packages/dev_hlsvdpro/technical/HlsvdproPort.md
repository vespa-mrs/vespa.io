# Porting HLSVDPro from Fortran to Python
In late 2012 I ported HLSVDPro from Fortran to (almost) pure Python. The Python version runs about 2 - 5 times slower than the Fortran version (not bad, considering) and produces the same results. The code is released under [browser:trunk/hlsvdpro/LICENSE a BSD license].

You can get a copy of the code with this Subversion command -- 
```
svn co http://scion.duhs.duke.edu/guest_svn/hlsvdpro/trunk hlsvdpro
```

The Python port is in the directory `experimental_pure_python_port` which 
you can also [source:/trunk/experimental_pure_python_port browse through this Web interface].

## Relationship to Vespa * [HlsvdproPortVespaUsefulness This port's usefulness to Vespa]
 * [HlsvdproPortDbdsqr About the annoying function DBDSQR()]
 * [HlsvdproPortBugs Bugs (in Fortran and Python)]
 * [HlsvdproPortPerformance Performance]

## Development Notes * [HlsvdproPortUnported Unported sections]
 * [HlsvdproPortFortranMemoryAllocation About how the Fortran code allocates memory]
 * [HlsvdproPortRandomness About the supposedly random numbers in zgetu0w()]
 * [HlsvdproPortPlan The plan written in advance of the port]
 * [HlsvdproPortFiles What's there] (a description of the files)
 * [HlsvdproPortNotesToMyself Odds and ends useful to anyone interested in improving this port]