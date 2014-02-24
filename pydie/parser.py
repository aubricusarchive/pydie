import re

def parse_roll(roll_argv):
    """
    Parse a roll argument vector.

    Arguments:
    roll_argv -- The roll argument vector

    returns

    # for an argument vector of '2d6m+1-1'
    {
        die: 6,
        modifiers: ['+1', '-1'],
        multiplier: 2,
        argv: '2d6m+1'
    }
    """

    rDie = r'(?P<multiplier>\d+)d(?P<die>\d+)'
    rModifieres = r'\+\d|-\d'
    rDie = re.compile(rDie)
    rModifieres = re.compile(rModifieres)

    roll_and_modifiers = roll_argv.split('m')
    roll = roll_and_modifiers[0]

    try:
        modifiers = roll_and_modifiers[1]

        modifiers = rModifieres.findall(modifiers)
    except:
        modifiers = []

    # TODO: Add error handling here
    roll_dict = rDie.match(roll).groupdict()
    roll_dict['modifiers'] = modifiers
    roll_dict['argv'] = roll_argv

    return roll_dict
