import re
import qrand
from random import shuffle

# import pdb

# re will capture the digits from "d20"
rDie = r'(\d+)'

# re will match a +n or -n and capture the "n"
rBonuses = r'\+(\d+)'
rPenalties = r'-(\d+)'


def roll(multiplier, die, modifier_str=''):
    modifier_str = '' if modifier_str is None else modifier_str

    result = {
        'multiplier': multiplier,
        'die': die,
        'modifier_str': modifier_str,
        'roll_results': [],
        'original_result': -1,
        'modified_result': -1,
        'bonuses': [],
        'penalties': [],
        'success': False
    }

    # number proceeding the d is our number of sides or "max_num"
    max_num = int(re.findall(rDie, die)[0])

    # get random number set from qrand
    roll_results = qrand.rand_uint16_list(multiplier, max_num)

    # store original result
    original_result = sum(roll_results)

    # apply modifiers to result and store modified result
    # list comp is, for all captured matches in modified_str
    #   convert to int and sum
    modified_result = original_result
    bonuses = re.findall(rBonuses, modifier_str)
    penalties = re.findall(rPenalties, modifier_str)
    modified_result += sum([int(b) for b in bonuses])
    modified_result -= sum([int(p) for p in penalties])

    # update result
    result['roll_results'] = roll_results
    result['original_result'] = original_result
    result['bonuses'] = [int(b) for b in bonuses]
    result['penalties'] = [int(p) for p in penalties]
    result['modified_result'] = modified_result

    if original_result != -1:
        result["success"] = True

    return result


# get n-results for n-sides of a die
# get 1 additional result to select roll result
# repeat for each roll
# set_length = n-sides * n-rolls + n-rolls
def roll_new(multiplier, die, modifier_str):
    max_num = int(re.findall(rDie, die)[0])
    num_bag = range(1, max_num + 1)

    shuffle_count = qrand.rand_uint16(50)
    print('shuffle_count', shuffle_count)
    while(shuffle_count):
        shuffle(num_bag)
        print('shuflz', num_bag)
        shuffle_count -= 1

    choices = qrand.rand_uint16_list(multiplier, max_num)
    roll_results = [num_bag[x - 1] for x in choices]

    print('num_bag', num_bag, 'choices', choices)

    return roll_results
