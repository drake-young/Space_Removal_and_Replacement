# Space Removal and Replacement

Just as the project title implies, this program has two goals in mind: given a piece of text, remove the spaces. After removing the spaces from the text, put them back. 

I initially wrote a more procedural, "Pythonic" approach to the problem set. I was relatively satisfied with the performance for the problem. O(n) for both the removal and replacement of the spaces. At the time, however, I was learning about genetic algorithms, so I felt compelled to attempt the same problem from a genetic algorithm approach (which was a terrible mistake, more on that later). However, about halfway through writing the script, I discovered the algorithm was more like a "Random Walk on a Discrete Line" with memory rather than a true Genetic Algorithm, so I renamed the file appropriately.

"Okay, but why *this* particular problem?" I actually ended up deciding to implement a solution to this problem when discussing artificial intelligence on a train ride home from classes. We were discussing that this problem is one of the first ones given to students at the introductory level of A.I. classes, and I wanted to see if it could be done with a more procedural approach. And that's exactly what I did.. well, in basic_method.py. The other python file is a much less optimal approach that still technically reaches the correct answer, but with a significantly higher runtime complexity.

## Files

* *basic_method.py:* a "Pythonic" approach to the problem
* *RWOADL_initial.py:* "Random Walk on a Discrete Line" approach to the problem
* *text.txt:* default input text file, can be replaced with anything
* *phrase.txt:* very short text input for testing ("Hello World!")
* *sentence.txt:* One sentence long text input "The Quick Brown Fox Jumped Over The Lazy Dog"
* *paragraph.txt:* Contains the FitnessGram<sup>TM</sup> Pacer Test text transcription
* *large.txt:* contains the entire Bee Movie script on a single line

## basic_method.py

This file (basic_method.py) is meant to highlight a basic method for doing this. It records the indices that spaces (' ') appear in the original text, then removes/restores spaces at those indices.

This method is considered "basic" compared to the other methods implemented, which use various forms of genetic/learning algorithms to "learn" what it is supposed to be doing (see those files for more information)

## RWOADL_initial.py

This file (RWOADL_initial.py) is meant to highlight an other approach for solving this problem. At the time of working on the "basic_method.py" file, I happened to be studying a lot of genetic algorithms. After a developing about half of this file, I ended up realizing this model was more like a "Random Walk on a Discrete Line" rather than a true genetic algorithm. But at this point, I had committed to using the terminology for a genetic algorithm.

Unlike a true genetic algorithm, future generations are spawned from mutations on a single parent, with no cross-over.

## Post-Development Notes

1.   This problem is not ideal for utilizing genetic algorithms. Genetic algorithms are best used for converging to a local minima/maxima in NP-hard problems, not a simple space removal/replacement, especially since the most ideal fitness function requires already knowing the final resulting string, which makes the generation process an unnecessary extra step.
2.   This program is designed as a "proof of concept" to test the theory of genetic algorithms with this problem. I would not recommend using this script if you are looking for an efficient solution -- processing the large dataset took approximately 75 minutes on a windows 10 x86 64-bit machine.
3.   My initial plan was to re-model this as a binary genetic algorithm, where the genes were 1 if space or 0 if not, but I eventually decided that such effort would be redundant because knowing the ideal fitness would knowing the indices of all the spaces in the start.
4.   basic_method.py uses algorithms that I am more satisfied with than this, though I will continue to play with genetic algorithms for problem sets better suited for converging to local minima/maxima in a relatively fast time rather than using convoluted approaches to simple problems.

## Authors

* **Drake Young** - *Initial work* - [drake-young](https://github.com/drake-young)

See also the list of [contributors](https://github.com/drake-young/Euler20_Python/contributors) who participated in this project.

## Additional Links and References

* [.gitignore template](https://github.com/github/gitignore/blob/master/Global/JetBrains.gitignore)
