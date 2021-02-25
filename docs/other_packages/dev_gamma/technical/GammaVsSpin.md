# Gamma Performance Vs. Spin Count
Gamma's performance as a function of the spin count, using a simple free induction decay.

As can be seen by the chart below there is a rapid increase in time for this simple calculation, as the spin count increases.


|| Spin count || Molecule                    || Time (seconds) ||  Ratio t(n)/t(n-1) ||  Memory(kB) ||
||            ||                             ||                ||                    ||             ||
||      5     || Glutamate                   ||      0.0045    ||  n/a               ||      265    ||
||      6     || Creatine                    ||      0.031     ||  6.89              ||      575    ||
||      7     || Tyrosine                    ||      0.402     ||  12.96             ||    3,610    ||
||      8     || Phenylalanine               ||      5.08      ||  12.64             ||    7,980    ||
||      9     || Phosphorylcholine-trimethyl ||     61.6       ||  12.12             ||   21,000    ||
||     10     || Choline-trimethyl           ||   5087.0       ||  83.40             ||  134,000    ||


What is most notable about this table is how out of step with the other calculations the spin 10 system is - in terms of the trend in performance. It was roughly 4 times slower than expected based on the other calculations.

The memory requirements of these calculations were all well below what was available on the test system, a Dell M4400 laptop, with Intel Core 2 Duo p9550 (2.66 GHz, 6M L2 cache, 1066 Mhz FSB) with 4 GB main memory. The 10 spin calculation required 134 MBytes (out of 2.26 GBytes available at the time). There was no disk swapping.

One theory is that the number of L2 Cache misses is increasing, since the memory requirement went from 21 to 134 MBytes. Attempts were made to study this using the Valgrind testing tool - specifically "valgrind --tool=cachegrind" - which shows the number of cache lookups and misses. However, after seeing an 80 fold degradation in the performance on smaller spin systems (9 spins went from 61 to 5047 seconds), it was estimated that this would take about 5 days for a 10 spin system. This will have to wait until a large period of idle time to let run, and is therefore temporarily on hold as of this writing.








