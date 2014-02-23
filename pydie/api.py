def parse_rolls_argv(rolls_argv):
    return [parse_roll_argv(argv) for argv in rolls_argv]


def parse_roll_argv(roll_argv):
    from pydie import parser
    return parser.parse_roll(roll_argv)


def do_roll(roll_dict, roll_method):
    return roll_method(roll_dict)


def do_rolls_from_argv(rolls_argv, roll_method):
    return [do_roll(roll, roll_method) for roll in parse_rolls_argv(rolls_argv)]
