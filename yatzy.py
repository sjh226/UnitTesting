# doctest:
# python -m doctest yatzy.py


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

    '''
