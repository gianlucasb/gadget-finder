gadget-finder
=============

Tool that, given a binary and a number of bytes to look back, finds the gadgets that can be exploited with ROP

## Why

Return Oriented Programming (ROP) is a way of exploiting programs, by using small snippets of code (gadgets) to perform tasks.
The tricky part is to find such gadgets. This program returns, given a binary file and a number of instructions N, the list of all gadgets in the program that are at least of length N.

## Usage

python GadgetFinder.py binary_file num_of_instructions
