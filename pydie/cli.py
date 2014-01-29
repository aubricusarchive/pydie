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

    Examples:

        1d3                (single roll no mods)
        2d4m+1             (single roll mod)
        3d6m-1+3           (single roll with multi-mods)
        4d8m+2 5d12m+1-2+3 (multi roll, separated with a space)

    Options:
        -r --result-info    Display full result information (optional)
        -v --version        Display the version number
        -h --help           Display this screen
"""

import sys
from docopt import docopt


def main():
    from pydie import get_version
    arguments = docopt(
        __doc__, version=get_version()
    )

    if arguments['roll']:
        exit_value = got_roll(arguments);
        print('')
        sys.exit(exit_value)


def got_roll(arguments):
    rolls = arguments['<roll>']

    print('\nOk! I see you want me to do {roll_count} rolls!'.format(
        roll_count=len(rolls)
    ))

    for roll in rolls:
        try:
            result = do_roll(roll)
            roll_results = [str(roll) for roll in result['roll_results']]

            print('BAM! You rolled: {0}'.format(', '.join(roll_results)))

            if arguments['--result-info'] is True:
                print('\nFull roll result info:\n{0}'.format(
                    '\n'.join(['{0}: {1}'.format(k, result[k]) for k in result])
                ))

        except:
            return 1

    return 0

def do_roll(roll_arg):
    from pydie import parser

    roll_info = parser.parse_roll(roll_arg)

    print("\nRad, I'm about to roll {0} d{1} with these modifiers: {2}".format(
        roll_info['multiplier'],
        roll_info['die'],
        ', '.join(roll_info['modifiers'])
    ))

    print("\nQuerying the cosmos...\n")

    return get_roll_result(roll_info)

def get_roll_result(roll_info):

    # extract roll info
    multiplier = int(roll_info['multiplier'])
    die = int(roll_info['die'])
    modifiers = [int(x) for x in roll_info['modifiers']]

    # Query ANU API
    from pydie import anu
    import random

    # Generate results by putting "n-balls"
    # into a bag with values between min and max,
    # mix it up thoroughly, pick out a ball,
    # and record result. Repeat this process m times.
    #
    # You might notice I use ANU numbers to pick figurative balls
    # out of the figurative bag. Doing this not only stays true
    # to the exercise above but also produces, in my experience,
    # more 'natural' results overall.

    # +1 compensates for range min at 1
    balls = range(1, die+1)

    # picks = [int(round(pick)) for pick in anu.rand(min=0, max=die, length=multiplier)]
    picks = anu.randint(min=0, max=die, length=multiplier)

    # shuffle-lufogus!
    for x in range(10, random.randint(10, 100)):
        random.shuffle(balls)

    # pick values from balls and don't forget to add modifiers
    # an empty list is safe, sum will return 0, e.g. +0
    raw = [balls[x] for x in picks]
    roll_results = [x + sum(modifiers) for x in raw]

    results = {
        'roll_results': roll_results,
        'raw': raw
    }

    results.update(roll_info)

    return results


if __name__ == "__main__":
    sys.exit(main())
