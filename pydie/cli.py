"""Usage:
    pydie roll <multiplier> <die> [<modifier>]
    pydie roll_new <multiplier> <die> [<modifier>]

    pydie [-h | --help]

    Generate a random n-sided dice role.

    Options:
        -h --help  print help information for this program

"""

import sys
from pydie import roll
from pydie import roll_new
from docopt import docopt


def exe_roll(arguments):
    multiplier = int(arguments['<multiplier>'])
    die = arguments['<die>']
    mod_str = arguments['<modifier>']

    print '\nRolling {0} {1}s'.format(multiplier, die)

    result = roll(
        multiplier,
        die,
        mod_str
    )

    if(result['success']):
        print "\nYour result is {0}!\nYour original rolls were {1}\nYour original total was {2}\nYou applied the following modifiers {3}".format(

                result['modified_result'],
                result['roll_results'],
                result['original_result'],
                result['modifier_str']
            )


def exe_roll_new(arguments):
    multiplier = int(arguments['<multiplier>'])
    die = arguments['<die>']
    mod_str = arguments['<modifier>']

    print '\nRolling {0} {1}s'.format(multiplier, die)

    result = roll_new(
        multiplier,
        die,
        mod_str
    )

    print('roll_new: ', result)


def main():
    arguments = docopt(__doc__)
    print(arguments)

    if(arguments['roll']):
        exe_roll(arguments)
        return

    if(arguments['roll_new']):
        exe_roll_new(arguments)
        return


if __name__ == "__main__":
    sys.exit(main())
