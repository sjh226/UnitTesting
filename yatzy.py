# doctest:
# python -m doctest yatzy.py

# pytest -m pytest --doctest-modules

# use ellipses to denot text you don't care about (like line numbers in
# an exception output) -> also for memory locations
# treated like a wildcard
#
# ex:
# >>> scores([1, 1, 2, 2, 2]) #doctest: +ELLIPSIS
# [(8, ,function full_house at ...), (2, <function ones at ...>)]
#
# pytest does not need to set ELLIPSIS as on
#
# CAREFUL WITH THE ELLIPSES!!!!!!!! will match more than you may want

# doctest can run text files, must import modules being used
# pytest will look for even text files which start with test_*

def small_straight(dice):
    '''
    Score the given roll in the 'Small Straight' Yatzy category.

    Args:
        dice: a sorted list of 5 integers indicating the dice rolled
    Returns:
        an integer score

    >>> small_straight([1,2,3,4,5])
    15
    >>> small_straight([1,2,3,4,4])
    0

    This function works with lists or sets or other collection types:

    >>> small_straight({1,2,3,4,5})
    15

    It also handles unsorted input

    >>> small_straight([5,4,3,1,2])
    15

    '''
    if sorted(dice) == [1,2,3,4,5]:
        return sum(dice)
    else:
        return 0

def dice_counts(dice):
    '''
    Make a dictionary of how many of each value are in the dice

    >>> dice_counts([1,2,2,3,3])
    {1: 1, 2: 2, 3: 2, 4: 0, 5: 0, 6: 0}

    *** dictionaries have no order so above ^^^ will not work! ***
    use sorted(dice_counts([1,2,2,3,3]).items())

    *** similar issue with number of decimal places
    use round(1.0/7, number of decimal places)

    '''
    return {x: dice.count(x) for x in range(1, 7)}

if __name__ == '__main__':
    print(dice_counts([5, 5, 4, 1, 6]))
