"""Usage:
    pydie roll [-r|--result-info] <roll>...
    pydie (-v | --version)
    pydie (-h | --help)

    Description:

        Generate a random n-sided for n-die roles.

    Commands:

        roll  Roll any kind of die to receive a randomized dice roll.

              - Roll command format {multiplier}{die}[m{modifiers}]...
              - Multipler is required, min 1; 0 will cause error
              - "m" is required when specifying modifiers
              - "+", plus, or "-", minus, is required before each modifier

    Roll Examples:

        roll 1d3                (single roll no mods)
        roll 2d4m+1             (single roll mod)
        roll 3d6m-1+3           (single roll with multi-mods)
        roll 4d8m+2 5d12m+1-2+3 (multi roll, separated with a space)

    Options:
        -r --result-info    Display full result information (optional)
        -v --version        Display the version number
        -h --help           Display this screen
"""

import sys
from docopt import docopt

from pydie import api
from pydie import rollmethods


def main():
    from pydie import get_version

    arguments = docopt(
        __doc__, version=get_version()
    )

    if arguments['roll']:
        received_command_roll(arguments)
        sys.exit(0)


def received_command_roll(arguments):
    print('\nAlright let\'s do this, querying the cosmos...')

    argv = arguments['<roll>']
    opt_result_info = arguments['--result-info']

    results = api.do_rolls_from_argv(argv, rollmethods.anu_pick_n_shuffle)

    for result in results:
        print(
            '\nFor the roll "{}" you rolled: {}'.format(
                result['argv'],
                ', '.join(str(roll) for roll in result['rolls'])
            )
        )

        if(opt_result_info is True):
            print(
                '\nFull roll result info:\n{0}'.format(
                    '\n'.join(['{0}: {1}'.format(k, result[k]) for k in result])
                ))

    print('')


if __name__ == "__main__":
    sys.exit(main())
