"""Usage: pydie.py roll <multiplier> <die> [<modifier>]
          pydie.py [-h | --help]

Generate a random n-sided dice role.

Options:
    -h --help        print help information for this program

"""
from docopt import docopt
import urllib
import json
import re

URL = 'https://qrng.anu.edu.au/API/jsonI.php'
MAX_RESULTS = 1024  # api example: https://qrng.anu.edu.au/API/api-demo.php
MAX_INT = 65536  # see: http://en.wikipedia.org/wiki/65536_(number)

def get_nums(num_results=MAX_RESULTS):
    url = URL + '?' + urllib.urlencode({
        'type': 'uint16',
        'length': num_results,
        'size': 1024,
    })
    # print url

    result = json.loads(urllib.urlopen(url).read())
    assert result['success'] is True, result
    assert result['length'] == num_results, result

    # print 'success!'
    return result['data']


def rand_int_list(max, min=1, num_results=1):
    range = max - min
    mod = MAX_INT / range
    nums = get_nums(num_results)
    results = []

    for x in nums:
        results.append(x / mod + min)

    # print results
    return results

def rand_int(max, min=1):
    range   = max-min
    modulus = MAX_INT / range
    num     = get_nums(1)[0]
    result  = num / modulus + min

    return result

def roll(multi, die, mod='0'):
    print 'rolling!', multi, die

    sides = die.split('d')[1]

    rolls = rand_int_list(int(sides), 1, int(multi))
    total = sum(rolls)

    print 'rolls:', rolls;
    print 'total before mod:', total

    bonuses = re.findall(r'\+[0-9]+', mod)
    penalties = re.findall(r'-[0-9]+', mod)

    print 'bonuses:', bonuses
    for b in bonuses:
        bonus = int(b.split('+')[1])
        total = total + bonus
        # print 'bonus', bonus

    print 'penalties:', penalties
    for p in penalties:
        penalty = int(p.split('-')[1])
        total = total - penalty
        # print 'penalty', penalty

    print 'total: ', total;

if __name__ == '__main__':
    arguments = docopt(__doc__)
    # print(arguments)

    if(arguments['roll']):
        multi = arguments['<multiplier>']
        die   = arguments['<die>']
        mod   = '0' if not arguments['<modifier>'] else arguments['<modifier>']

        roll(multi, die, mod)
