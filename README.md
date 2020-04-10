# Challenges proposed by Epitech's HUB during this quarantine period

## Challenge 01

This challenge has to be solved in python.

A pangram is a sentence that contains every alphabet letter at least once. For example "Pack my box with five dozen liquor jugs" is a pangram (a pangram is case insensitive).
With a given string as argument, return True if it is a pangram and False if not. You got to ignore ponctuation.

Prototype:

```python
def is_pangram(s):
```

## Challenge 02

This challenge has to be solved in python

Once upon a time on a road through the Far Ouest ...

... A Man had received instructions to go from a point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". It is clear that "NORTH" and "SOUTH" are opposed as well as "WEST" and "EAST" are.

Go in a direction and go backward immediately is a useless effort. As it is the Far Ouest, with heat and few water, it is important to save power, otherwise you could die of thirst!

Instructions given to the man are for example as follow:

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].

You can see that going "NORTH" to go right after that "SOUTH" isn't reasonable, better stay at the same place!
The task consist in giving the man a simplified version of the plan. A better plan in this case is simply:

["WEST"]

Prototype:
```python
def dirReduit(arr):
```
