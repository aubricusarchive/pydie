import re

def parse_roll(roll_argv):
    """
    Parse a roll argument vector.

    Arguments:
    roll_argv -- The roll argument vector

    returns

    # for an argument vector of '2d6+1-1'
    {
        die: 6,
        modifiers: ['+1', '-1'],
        multiplier: 2,
        argv: '2d6+1'
    }
    """

    # Just leaving this here for reference
    # (?P<mulit>\d+)d(?P<die>\d+)(?P<mod>[\+\d|\-\d]+)

    rRoll = r'(?P<multiplier>\d+)d(?P<die>\d+)'
    rModifieres = r'\+\d+|\-\d+'
    rRollPattern = re.compile(rRoll)
    rModifieresPattern = re.compile(rModifieres)

    modifiers = rModifieresPattern.findall(roll_argv)
    roll_dict = rRollPattern.match(roll_argv).groupdict()
    roll_dict['modifiers'] = modifiers
    roll_dict['argv'] = roll_argv

    return roll_dict
