# Changing Vespa's Database Structure
As of this writing (January 2013), Vespa's database format has changed seven
times. This document explains how to change the database in the future and
points to some of the old changes as examples.

We've use a free tool called SQL Designer to edit our database definition.
It's helpful but not necessary. We have a document that tells you
[UsingSqlDesigner what you need to know about SQL Designer] before
you get started.


## First Steps
Vespa's database is very forgiving in that it's easy to recreate locally.
This allows for lots of experimentation before you share your changes with
others.

Vespa's database is defined by
[browser:trunk/common/resources/create_tables.sql create_tables.sql]. 
It creates the database structure that's later populated by Python code. 
Your first step in modifying the database will be to change that file.

There are two other files in that same directory -- 
[browser:trunk/common/resources/create_indices.sql create_indices.sql]
and [browser:trunk/common/resources/create_views.sql create_views.sql] -- that
build on the output of `create_tables.sql`. Creating indices speeds up access
to frequently-accessed items at the expense of insert speed, and views are 
sometimes useful but at present we're not using any so `create_views.sql`
is empty.

You probably won't need to alter `create_indices.sql` nor `create_views.sql`.

Once you've modified `create_tables.sql`, you can use 
[browser:trunk/devtools/recreate_database.py recreate_database.py] to rebuild
the database or just delete your existing database and then run a Vespa app.
This is sufficient for local changes (i.e. testing on your machine) and you'll 
probably repeat this cycle many times.

## The Database and Vespa Init
Every Vespa app calls 
[browser:trunk/common/util/init.py init_app() in util_init.py] very early in 
the app's invocation. This function does a number of things, including 
upgrading or (re)creating Vespa's database if necessary. You can trigger a database recreation by 1) deleting or 2) renaming the database file. This can be useful for testing new code. When you are done testing, you can (if you want to) re-rename the original database back to its original name and Vespa will use that file going forward. This can be especially useful while testing database "upgrade" code, more on this below.

The file [browser:trunk/common/create_database.py create_database.py] handles
the work of building and populating a database from scratch. You might want
to read this; it's pretty straightforward and shows how the database is 
constructed. You might also need to modify it if you're adding tables to the
database that need to be populated.

Upgrading the database is handled by the 
[browser:trunk/common/util/db_upgrader.py db_upgrader] module. This is explained
in detail below.


## Triggering an Update
When you're ready to make your changes part of an official Vespa release, 
you'll need to tell Vespa to upgrade the database, and you'll need to write
the code to do it.

Upgrading a database occurs when `init_app()` notices that the value of
`DATABASE_VERSION` in [browser:trunk/common/constants.py constants.py] is
greater than the value of the field `database_version` in the table `vespa` in
the database. (This is an administrative table; it doesn't contain any user 
data. It only contains one row and one column.) When those values are 
different, the [browser:trunk/common/util/db_upgrader.py db_upgrader] 
calls a function to upgrade that version.


## Upgrade Functions
All of the code to upgrade a database is in the `DatabaseUpgrader` class.
That class knows how to upgrade based on the value of the database version
field. 

Upgrades are always stepwise. If `DATABASE_VERSION` 
in constants.py is 7, and the value of `database_version` in the database is 5,
`DatabaseUpgrader` will call `upgrade_5()` to upgrade the database from 
version 5 to 6, and then it will call `upgrade_6()` to upgrade it from 6 to 7.

The method `upgrade_N()` is what you'll write, where `N` is the number of the
current database (i.e. the one you're updating _FROM_, not to). Your code
can be simple like `_upgrade_3()` which merely added a table, or complex like
`_upgrade_2()` which broke the old `simulations` table into several parts and
replaced it with a different table of the same name.

The code in `DatabaseUpgrader` contains comments to help you on your way, 
and you can use the existing code as a template.

## Summary
I put the summary last so you won't be tempted to skip the details above. 
They're important, please read them.

1. When working locally, there's no need to change version numbers anywhere.
 Just alter `create_tables.sql` as you see fit, and delete/rename your database to
 force Vespa to recreate it.
1. Repeat step 1 as necessary.

When you're ready to include your changes in a new Vespa version --

1. Increment `DATABASE_VERSION` in `constants.py`
1. Write an `upgrade_N()` method for `DatabaseUpgrader` in `db_upgrader.py`.

 

