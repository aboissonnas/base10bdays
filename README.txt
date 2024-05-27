This is a translation to Python of a college assignment in Clojure. I don't actually have the prompt any more, but from reading my own code, I believe it was along these lines:

Our years have 365 days, split into 12 months with varying amounts of days. This is silly.
Base Ten is the obviously superior way to count anything. A Base Ten year has 1000 days. Write a program that translates someone's age to Base Ten.

This script deviates from the original assignment, which was intended to teach the students about Clojure as a language and utilized lazy sequences. The translation is a bit more Pythonic in execution.
I would include the original code, but I'm worried that my college professors would hunt me for sport for giving future students a finished product to look at.

In order to run this code:
    - Ensure that main.py and utils.py are in the same directory
    - Using the command line, navigate to the directory ABOVE the one containing the code
    - Run `python -m {directory}.main`, replacing {directory} with the directory containing the code

In order to run the unit tests:
    - Ensure that main.py, utils.py, and unit_tests.py are all in the same directory
    - Using the command line, navigate to the directory ABOVE the one containing the code
    - Run `python -m unittest {directory}.unit_tests`, replacing "{directory}" with the name of the directory containing the code