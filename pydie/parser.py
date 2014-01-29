import re

def parse_roll(rollstr):
    """Parse a roll
    """

    rDie = r'(?P<multiplier>\d+)d(?P<die>\d+)'
    rModifieres = r'\+\d|-\d'
    rDie = re.compile(rDie)
    rModifieres = re.compile(rModifieres)

    roll_and_modifiers = rollstr.split('m')
    roll = roll_and_modifiers[0]

    try:
        modifiers = roll_and_modifiers[1]

        modifiers = rModifieres.findall(modifiers)
    except:
        modifiers = []

    # TODO: Add error handling here
    roll_dict = rDie.match(roll).groupdict()
    roll_dict['modifiers'] = modifiers

    return roll_dict
