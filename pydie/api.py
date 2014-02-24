def parse_rolls_argv(rolls_argv):
    """
    Parse n-rolls

    Arguments:
    rolls_argv -- A list of roll argument vectors (see parse_roll_argv)

    Returns list[{dict...}]

    """
    return [parse_roll_argv(argv) for argv in rolls_argv]


def parse_roll_argv(roll_argv):
    """
    Parse a roll argument vector.

    Wraps parser.parse_roll.
    TODO: Not sure this is 100 percent necessary, consider removing

    Arguments:
    roll_argv -- a roll argument vector, '1d20m+1'

    Returns:
    dict

    """
    from pydie import parser
    return parser.parse_roll(roll_argv)


def do_roll(roll_dict, roll_method):
    """
    Execute a roll

    Arguments:
    roll_dict -- a parsed roll argument vector, '1d6m+2'
    roll_method -- the method to produce the roll (see pydie.rollmethods)

    Returns:
    list

    """
    return roll_method(roll_dict)


def do_rolls_from_argv(rolls_argv, roll_method):
    return [do_roll(roll, roll_method) for roll in parse_rolls_argv(rolls_argv)]


def roll(*args):
    """
    Execute n-rolls

    Mostly a convenience wrapper around do_rolls_from_argv for use
    within a python module.

    Takes *args, arguments should match cli input

    Example:

    import pydie
    pydie.roll('1d3', '2d6m+1', '3d12m+2')

    Returns:
    list

    """
    from pydie import rollmethods
    return do_rolls_from_argv(args, rollmethods.anu_pick_n_shuffle)
