## Morse Code decoder
This is a test framework (and solution) for working on the Morse Code katas 1 and 2 from Codewars:
https://www.codewars.com/kata/decode-the-morse-code-advanced/python

The tests are broken into two classes:
 - TestMorseA
 - TestMorseB

The TestMorseA class will only test the `decodeMorse()` function.
To run all of the cases defined in TestMorseA, use the following cmd line:

`$ python -m unittest test_morse.TestMorseA`

The TestMorseB class will test both the `decodeMorse()` function as well as the `decodeBits()` function.

`$ python -m unittest test_morse.TestMorseB`

If you want to run all tests combined, try this:

`$ python -m unittest discover`