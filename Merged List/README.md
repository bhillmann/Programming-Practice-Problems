Merged List
===========

Suppose you have two lists of strings, one labeled Source and the other is labeled Prefix. Design a program will produce a new list that combines the Source and Prefix under certain restriction. The string lists contain 7-bit nonzero ASCII characters and are sorted using a standard case-insensitive ASCII string comparison test with strings that are less than other strings by the comparison coming first in the list. It can also be assumed that no two strings in a given list are identical under this comparison.

An item X is in the merged list if and only if one of the following is true.

* X is from the Source list and there is an item Y in the Prefixes list that is a case-insensitive string prefix for X.

* X is from the Prefixes list and there is no item in the Source list for which X is a case-insensitive string prefix.

The completed merged list should be sorted as is defined above.