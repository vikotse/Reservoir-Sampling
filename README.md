Reservoir Sampling algorithm in Python
======================================

The [Reservoir Sampling algorithm](https://en.wikipedia.org/wiki/Reservoir_sampling) is a random sampling algorithm. It is a family of randomized algorithms for randomly choosing a sample of K items from a list S containing N items, where N is either a very large or unknown number. Typically N is large enough that the list doesn't fit into main memory.

Usage
-----
This module is using Reservoir Sampling to randomly choose exactly K (Sample Number) rows on input file. Sampling result's row order is the same as input file.

	using in python 2.7
	$ py -2 reservoir_sampling_py27.py input.txt output.txt 4
	arguments: [python-version] [pyfile] [infile] [outfile] [K]

	using in python 3.6
	& py -3 reservoir_sampling_py36.py input.txt output.txt 4
	arguments: [python-version] [pyfile] [infile] [outfile] [K]

Efficiency
----------
If number of lines on input file is N. Time complexity is O(N). Space complexity is O(K) (regardless of the size of one line). If K is equal or larger than N, output file would be same as input file.
