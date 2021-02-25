# Example: fid.py
Here is the source code for fid.py:

```
import pygamma as pg 

infile = 'glutamate.sys' 
outfile = "glutamate_fid__test.txt" 
h1 = "FID Simulation Test"
h2 = "using input sys file: " + infile
header = (h1, h2)
sys = pg.spin_system() 
sys.read(infile) 
specfreq = sys.Omega() 
H = pg.Hcs(sys) + pg.HJ(sys) 
D = pg.Fm(sys) 
ac = pg.acquire1D(pg.gen_op(D), H, 0.001) 
ACQ = ac 
sigma = pg.sigma_eq(sys) 
sigma0 = pg.Ixpuls(sys, sigma, 90.0) 
mx = ACQ.table(sigma0) 
mx.dbwrite_old(outfile, "glutamate", 0, 10, specfreq, .1, 0, header)
```

And here is the sample input file (glutamate.sys):

```
SysName (2) : glutamate (For J's and chemical shifts, refer to NMR Biomed 13, 129-153 (2000))
NSpins  (0) : 6  - Chemical shifts were measured in H2O solution.
Iso(0) (2) : 1H
Iso(1) (2) : 1H
Iso(2) (2) : 1H
Iso(3) (2) : 1H
Iso(4) (2) : 1H
Iso(5) (2) : 1H
PPM(0) (1) : 3.7433
PPM(1) (1) : 2.0375
PPM(2) (1) : 2.1200
PPM(3) (1) : 2.3378
PPM(4) (1) : 2.3520
PPM(5) (1) : 500
J(0,1) (1) : 7.331
J(0,2) (1) : 4.651
J(0,3) (1) : 0.0
J(0,4) (1) : 0.0
J(0,5) (1) : 0.0
J(1,2) (1) : -14.849
J(1,3) (1) : 6.413
J(1,4) (1) : 8.406
J(1,5) (1) : 0.0
J(2,3) (1) : 8.478
J(2,4) (1) : 6.875
J(2,5) (1) : 0.0
J(3,4) (1) : -15.915
J(3,5) (1) : 0.0
J(4,5) (1) : 0.0
Omega  (1) : 170.67
```

