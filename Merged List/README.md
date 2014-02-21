Merged List
===========

Suppose you have two lists of strings, one labeled Source and the other is labeled Prefix. Design a program that will merge the Source and Prefix lists under the following rules.

An item X is in the merged list if and only if one of the following is true.

* X is from the Source list and there is an item Y in the Prefixes list that is a case-insensitive string prefix for X.

* X is from the Prefixes list and there is no item in the Source list for which X is a case-insensitive string prefix.

The completed merged list should be sorted as follows. The string lists contain 7-bit nonzero ASCII characters and are sorted using a standard case-insensitive ASCII string comparison test with strings that are less than other strings by the comparison coming first in the list. It can also be assumed that no two strings in a given list are identical under this comparison.
