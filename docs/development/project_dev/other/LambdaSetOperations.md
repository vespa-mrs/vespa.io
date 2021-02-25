Lambda operators to perform simple set operators

FYI, Python has a built-in set type which can provide these operations
for you too. See examples below.

The Set has only been around since (I think) Python 2.4 so code 
(and examples) written for older versions of Python might not make use of 
them.

http://docs.python.org/library/stdtypes.html#set

Examples using filter & lambda:

```
        #Example of lambda for simple list AND, OR, XOR, UNION 
        list1=range(5) # [0,1,2,3,4]
        list2=range(3,7) # [3,4,5,6]
        union=list1+filter(lambda x:x not in list1,list2)
        # union = [0,1,2,3,4,5,6]
        
        Intersection is just as easy
        intersection=filter(lambda x:x in list1,list2)
        # intersection=[3,4]

        Difference is the last thing you wanted...
        difference=filter(lambda x:x not in list2,list1)
        # difference=[0,1,2]
        
        And my set vocabulary is rusty but the distinct elements or those from both lists that are NOT in common (un-intersection?) would be:
        distinct=filter(lamba x:x not in list2,list1)+filter(lambda x:x not in list1,list2)
        # distinct=[0,1,2,5,6]
```

Examples using Python's built-in set:

```
    # Sets are easy to create from lists:
    >>> set1 = set(range(5))
    >>> set2 = set(range(3,7))
    # And back again:
    >>> list(set2)
    [3, 4, 5, 6]

    # Union
    >>> print set1.union(set2)
    set([0, 1, 2, 3, 4, 5, 6])

    # Intersection
    >>> print set(set1).intersection(set2)
    set([3, 4])

    # Difference
    >>> set1 - set2
    set([0, 1, 2])

    # Symmetric difference 
    # Return a new set with elements in either the set or other but not both.
    >>> print set1.symmetric_difference(set2)
    set([0, 1, 2, 5, 6])
    >>> 


}}}