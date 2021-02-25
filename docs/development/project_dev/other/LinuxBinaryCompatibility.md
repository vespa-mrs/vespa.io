## Notes about Creating C/C++ Binaries that Run on Different Flavors of Linux
After a little reading, what we've learned so far is --
 * This is not simple
 * I think the level of difficultly increases with the number of linked libraries
 * It is debatable whether static linking helps or causes more problems (see the pixelbeat site for more information on this).
 * It's probably helpful to compile with the oldest version of Linux & gcc that one intends to support.

Here's some articles/conversations on the topic --
 * http://www.pixelbeat.org/programming/linux_binary_compatibility.html
 * http://ask.slashdot.org/article.pl?sid=05/11/24/2230256&threshold=1
 * http://www.linux.org/docs/ldp/howto/Program-Library-HOWTO/shared-libraries.html
 * http://stackoverflow.com/questions/1771366/binary-compatibility-between-linux-distributions

Here's a tool that might help --
http://ldn.linuxfoundation.org/lsb/check-your-app

Here's a list of distros certified for compliance with the Linux Standard Base -- 
http://www.linuxfoundation.org/lsb-cert/productdir.php?by_lsb

Here's an interesting report on binary compatibility:
http://www.complang.tuwien.ac.at/anton/linux-binary-compatibility.html

A few other bits of research on Binary Compatibility:
http://kerneltrap.org/node/4006

