"""Usage:
    pydie roll <multiplier> <die> [--mod=<modifier>]

    pydie [-h | --help]

    Generate a random n-sided dice role.

    Options:
        -h --help  print help information for this program

"""

import sys
from pydie import roll
from docopt import docopt


def exe_roll(arguments):
    multiplier = int(arguments['<multiplier>'])
    die = arguments['<die>']
    # mod_str = arguments['<modifier>']
    mod = arguments['--mod']

    #todo need to look at docopt default vals
    mod = '' if not mod else mod

    print '\nRolling {0} {1}s'.format(multiplier, die)

    result = roll(
        multiplier,
        die,
        mod
    )

    print('roll: ', result)


def main():
    arguments = docopt(__doc__)
    print arguments
    if(arguments['roll']):
        exe_roll(arguments)
        return


if __name__ == "__main__":
    sys.exit(main())
