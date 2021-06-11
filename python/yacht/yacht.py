"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == 0:
        a = set(dice)
        if len(a) == 1:
            return 50
        return 0
    
    if category >= 1 and category <= 6:
        return sum([s for s in dice if s == category])


    if category == 9:
        return 30 * (dice.sort() == [1,2,3,4,5])

    if category == 10:
        return 30 * (dice.sort() == [2,3,4,5,6])

    if category == 11:
        return sum(dice)