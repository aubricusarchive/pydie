
"""Usage:
    pydie roll <multiplier> <die> [<modifier>]
    pydie [-h | --help]

    Generate a random n-sided dice role.

    Options:
        -h --help  print help information for this program

"""

import sys
from pydie import roll
from docopt import docopt


def main():
    arguments = docopt(__doc__)
    print arguments

    if(arguments['roll']):
        multiplier = int(arguments['<multiplier>'])
        die = arguments['<die>']
        mod_str = arguments['<modifier>']

        print '\nRolling {0} {1}s'.format(arguments['<multiplier>'], arguments['<die>'])

        result = roll(
            multiplier,
            die,
            mod_str
        )

    if(result['success']):
        print """\nYour result is {0}!
Your original rolls were {1}
Your original total was {2}
You applied the following modifiers {3}
""".format(result['modified_result'],
                    result['roll_results'],
                    result['original_result'],
                    result['modifier_str']
            )


if __name__ == "__main__":
    sys.exit(main())
