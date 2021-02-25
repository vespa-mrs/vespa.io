# SQLite Versions
## Summary*Our code must be compatible with SQLite 3.5.9* which was released in
May 2008.

## What Determines the Minimum
SQLite is often "baked into" Python, meaning that it is an integral part of 
Python and can't be upgraded. Therefore, the oldest SQLite version we 
must support is whatever is in
the oldest Python we support, and that's Python 2.6.0. The SQLite version
in that Python varies, but the oldest appears to be in the Windows 
version of Python 2.6.0. That Python reports that it uses SQLite 3.5.9.

For reference, Python 2.6.0 on OS X 10.6 reports SQLite 3.6.1, but SQLite
is an integral part of OS X and I don't think Python includes it statically 
on this platform. It uses the version that OS X supplies, and I imagine
that could be upgraded over time.

I didn't test any Linux versions of Python 2.6.0. I don't think
any package managers provide that version. They provide a more advanced
version of the 2.6 series, like 2.6.4.

## Do We Care?
Not so much, anymore.

Vespa versions up to and including 0.5.1 supported 
Python 2.5. In Python 2.5.0, the oldest SQLite was 3.3.4 (released in 
Feb 2006). 

Early in Vespa's development, there were some features
in SQLite that I wanted to use that had been added after 3.3.4, so
the SQLite version mattered a lot. For instance, SQLite added
features for generating UUIDs, but not until 3.3.13. That meant
that generating UUIDs at the database level was out of the question
for Vespa.

I learned to live without those features (which was fine, really).

As of this writing, the database is mature. Any new tables are
likely to follow the pattern we've established which deliberately
avoids using SQLite's "newer" features.

To see the limitations that were present when we used Python 2.5,
read [version 16 of this page](/wiki:SqliteVersions?version=16/).


