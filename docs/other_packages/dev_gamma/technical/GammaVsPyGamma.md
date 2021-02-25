# PyGamma vs Gamma
Speed comparisons between the SWIG-ed version of gamma, called pygamma, and the C++ version of gamma.  The comparisons were done using python2.5 for the python code and compiling the C++ code using the _gamma_ program (installed by making and installing the gamma code).  e.g. 'gamma fid_speed.cc'. The differences in timing ranges from 9% to 25%. Presumably this depends on how C++ intensive the code is and how much data needs to be passed between Python and C++ in the pygamma version.

## A. Free Induction Decay Experiment
A simple FID test.

### 1. For a 6 spin system, and doing 100 iterations
  * glutamate.sys

The time comparisons are listed below:

  * *gamma*:     14.2 seconds
  * *pygamma*: 16.93 seconds

Ratio 1.192, or 19% slower.


### 2. Using a 3 spin system and 15,000 iterations
  * System: gsh_test.sys

Timing results below:

  * *gamma*:    6.77 seconds
  * *pygamma*: 8.45 seconds

Ratio of 1.25 or 25% slower for pygamma.

In this case there is more setup and calling of gamma routines from python.

## B. Spin Echo with a Real Pulse
### Simulation of 400 realpulse spin-echo experiments each with a varying time delay
Rough Results reported via email:
  * *gamma*  the  average  (of  3 runs) took: 20.5 seconds
  * *pygamma* the average (of 3 runs)  took: 23.5 seconds

More Accurate Results (on a separate computer) with cleaned-up code:
  * *gamma*  the average of 4 runs took  : 15.92 seconds
  * *pygamma* the average of 4 runs took : 17.405 seconds

Ratio: 1.093 or 9.3% difference.


## Code Used for these two experiments
From: orphans/dtodd/performance/gamma_vs_pygamma

### FID Experiment
#### Python: fid_speedtest.py```
from __future__ import division
import pygamma as pg
import time
import fid_kernel

#infile = 'glutamate.sys' 
infile = 'gsh_test.sys' 


t1 = time.time()

sys1 = pg.spin_system() 
sys1.read(infile) 

mxlist = []

i=0
while i<15000 :
    mx = fid_kernel.fid_kernel(sys1)
    mxlist.append(mx)
    i+=1

t2 = time.time()

print 'fid_speedtest took %0.3f seconds' % ((t2-t1),)
```


#### C++: fid_speed.cc
```
#include "gamma.h"
#include <vector>
#include <string> 

using namespace std;

TTable1D & fid_test(spin_system & sys, TTable1D &mx);

//string sysfile = glutamate.sys
string sysfile ="gsh_test.sys";


int main()
{
    clock_t start, end;
    start = clock();

    spin_system	sys1;
    sys1.read(sysfile);

    vector<TTable1D> mxlist;
    
    TTable1D mx;
    for(int i=0; i<15000; i++)
    {
        fid_test(sys1, mx);
        mxlist.push_back(mx);
    }

    end = clock();

    double elapsed_time = static_cast<double>((end - start))/static_cast<double>(CLOCKS_PER_SEC);
    char str_time[100];
    sprintf(str_time, "%.2f", elapsed_time);\
    cout << "\nElapsed time: " << str_time << "\n\n";

    return 0;
}


TTable1D & fid_test(spin_system & sys, TTable1D &mx)
{

  gen_op		H;
  gen_op		D;
  gen_op		sigma0;
  acquire1D		ACQ;

  H = Hcs(sys) + HJ(sys);
  D = Fm(sys);

  acquire1D ac(D, H, 0.001);     // Set up acquisition
  ACQ = ac;				  

  sigma0 = sigma_eq(sys);	       // Equilibrium density matrix
  sigma0 = Ixpuls(sys, sigma0, 90.0);    // Apply a 90x pulse

  mx = ACQ.table(sigma0);	       // Transitions table (no lb)

  return mx;
}
```

### Spin Echo Realpulse Experiment
  * spinecho_realpulse_speedtest.py

```
from __future__ import division
import pygamma as pg
import spin_echo_realpulse_kernel
import time

dir = ""
insysfile = dir + "gsh_test.sys"
inpulse180file = dir + "bjs180_1.txt"


sys1 = pg.spin_system()
sys1.read(insysfile)

pulse1 = pg.row_vector.read_pulse(inpulse180file, pg.row_vector.ASCII_MT_DEG)


t1 = time.time()

mxlist = []
times = []
for i in range(400):
   times.append(.024 + i*.001/200.)

#print times

for time1 in times :
    mx = spin_echo_realpulse_kernel.spin_echo_realpulse_kernel(time1, sys1, pulse1)
    mxlist.append(mx)

t2 = time.time()

print 'fid_speedtest took %0.3f seconds' % ((t2-t1),)
```

  * spin_echo_realpulse_kernel.py

```
from __future__ import division
import pygamma as pg

def spin_echo_realpulse_kernel(time, sys, pulse):

    t1 = time
    t2 = time
    pulsestep = 0.00001

    specfreq = sys.Omega()

    ptime = pg.row_vector(pulse.size())

    #need to use pg.complex() so it can find correct function to call.
    for j in range(pulse.size()):
        ptime.put(pg.complex(pulsestep, 0), j)

    pwf = pg.PulWaveform(pulse, ptime, "TestPulse")

    pulc = pg.PulComposite(pwf, sys, "1H")

    H = pg.Hcs(sys) + pg.HJ(sys);
    D = pg.Fm(sys);

    Udelay1 = pg.prop(H, t1);
    Udelay2 = pg.prop(H, t2);

    # Neet to effectively typecast D as a gen_op.
    ac = pg.acquire1D(pg.gen_op(D), H, 0.001)

    ACQ = ac;

    sigma0 = pg.sigma_eq(sys)

    sigma1 = pg.Iypuls(sys, sigma0, 90.0)   #Apply a 90y pulse

    sigma0 = pg.evolve(sigma1, Udelay1)     #Evolve through T1

    Ureal180  = pulc.GetUsum(-1)            #Get the propagator for steps of 180

    sigma1 = Ureal180.evolve(sigma0)        #Evolve through pulse

    sigma0 = pg.evolve(sigma1, Udelay2)     #Evolve through T2

    mx = ACQ.table(sigma0)                  #Transitions table (no lb)

    return mx
```

  * spinecho_realpulse_speed.cc

```
// This file contains a set of gamma tests
#include "gamma.h"
#include <vector>
#include <string> 

using namespace std;


TTable1D & spinecho_realpulse_test(double time, spin_system & sys, row_vector & pulse, TTable1D &mx);


string sysfile ="gsh_test.sys";
string pulse180file = "bjs180_1.txt";


int main()
{
    clock_t start, end;

    string dir = "";
    string insysfile = dir + "gsh_test.sys";
    string inpulse180file = dir + "bjs180_1.txt";


    spin_system	sys1;
    sys1 = spin_system();

    sys1.read(sysfile);

    // Read Pulse Files, Initialize Waveform --------------------------
    row_vector pulse1 = row_vector::read_pulse(inpulse180file, row_vector::ASCII_MT_DEG);

    start = clock();

    vector<double> times;
    cout << "\n";
    for(int i=0; i<400; i++)
    {
        times.push_back(.024 + double(i)*.001/200.);
        //cout << times[i] << " ";  
    }
    //cout << "\n";


    vector<TTable1D> mxlist;
    vector<double>::iterator tv;
    
    TTable1D mx;
    for(tv = times.begin(); tv != times.end(); tv++)
    {
        spinecho_realpulse_test(*tv, sys1, pulse1, mx);
        mxlist.push_back(mx);
    }

    end = clock();

    double elapsed_time = static_cast<double>((end - start))/static_cast<double>(CLOCKS_PER_SEC);
    char str_time[100];
    sprintf(str_time, "%.2f", elapsed_time);\
    cout << "\nElapsed time: " << str_time << "\n\n";

    return 0;
}


TTable1D & spinecho_realpulse_test(double time, spin_system & sys, row_vector & pulse, TTable1D &mx)
{
  string outname = "test_lines";

  gen_op		H;
  gen_op		D;
  gen_op		sigma0;
  gen_op        sigma1;
  gen_op        Udelay1;
  gen_op        Udelay2;
  HSprop        Ureal180;
  double        t1 = time; 
  double        t2 = time; 
  double        pulsestep = 0.00001; // 1 msec pulse steps
  acquire1D		ACQ;
 

  row_vector ptime(pulse.size());

  for(int j=0; j<pulse.size(); j++) 
  {
	ptime.put(pulsestep, j); // pulse steps
  }

  PulWaveform	pwf(pulse, ptime, "TestPulse");

  PulComposite	pulc = PulComposite(pwf, sys, "1H");

  H = Hcs(sys) + HJ(sys);
  D = Fm(sys);

  Udelay1 = prop(H,t1);
  Udelay2 = prop(H,t2);

  acquire1D ac(D, H, 0.001);     // Set up acquisition
  ACQ = ac;				  

  sigma0 = sigma_eq(sys);	       // Equilibrium density matrix
  sigma1 = Iypuls(sys,sigma0,90.0);    // Apply a 90y pulse
  sigma0 = evolve(sigma1,Udelay1);     // Evolve through T1

  Ureal180  = pulc.GetUsum(-1);       // Get the propagator for steps of 180
  sigma1 = Ureal180.evolve(sigma0);    // Evolve through pulse
  sigma0 = evolve(sigma1,Udelay2);     // Evolve through T2

  mx = ACQ.table(sigma0);	       // Transitions table (no lb) 

  return mx;
}
```
