def anu_pick_n_shuffle(roll_dict):
    """Generates a roll result from a parsed roll argument vector.

    Pick and Shuffle Method
    Generate results by putting "n-balls" into a "bag" with values
    between min and max, mix it up thoroughly, pick out a ball,
    and record the result. Repeat this process m times.

    You might notice I use ANU numbers to pick the figurative
    balls out of the figurative bag. Doing this not only stays
    true to the exercise found on the ANU website but
    also produces, in my experience, more 'natural'
    results overall.

    Returns:
    {
        'raw': [1],
        'modifiers': [],
        'multiplier': '1',
        'die': '3',
        'rolls': [1],
        'argv': '1d3'
    }
    """

    # TODO: Consider making this a plugin, or some form
    #   of IOC to make the shuffling method swappable.
    from pydie import anu
    import random

    # extract roll data
    multiplier = int(roll_dict['multiplier'])
    die = int(roll_dict['die'])
    modifiers = [int(x) for x in roll_dict['modifiers']]

    #+1 compsensates for range min at 1
    balls = range(1, die+1)
    picks = anu.randint(min=0, max=die, length=multiplier)

    # oh ya, shuffle-lufogus!
    for x in range(10, random.randint(10, 100)):
        random.shuffle(balls)

    # pick values from balls and don't forget to add modifiers
    # an empty list is safe, sum will return 0, i.e. +0
    raw = [balls[x] for x in picks]
    roll_results = [x + sum(modifiers) for x in raw]

    results = {
        'rolls': roll_results,
        'raw': raw
    }

    results.update(roll_dict)

    return results
