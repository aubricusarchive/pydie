import re
import qrand
from random import shuffle

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


def apply_modifiers(original_result, modifier_str):
    modified_result = original_result
    bonuses = re.findall(rBonuses, modifier_str)
    penalties = re.findall(rPenalties, modifier_str)
    modified_result += sum([int(b) for b in bonuses])
    modified_result -= sum([int(p) for p in penalties])

    return {
        'result': modified_result,
        'bonuses': bonuses,
        'penalties': penalties
    }


# get n-results for n-sides of a die
# get 1 additional result to select roll result
# repeat for each roll
# set_length = n-sides * n-rolls + n-rolls
def roll_new(multiplier, die, modifier_str):

    modifier_str = '' if not modifier_str else modifier_str

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

    max_num = int(re.findall(rDie, die)[0])
    num_bag = range(1, max_num + 1)

    # "shuffle" our numbers before picking out of the "bag"
    shuffle_count = qrand.rand_uint16(50)

    while(shuffle_count):
        shuffle(num_bag)
        shuffle_count -= 1

    # create a n-random choices
    # use these numbers to select a number from our "bag"
    choices = qrand.rand_uint16_list(multiplier, max_num)

    # @todo: -1 here doesn't feel quite right, revisit
    roll_results = [num_bag[x - 1] for x in choices]
    original_result = sum(roll_results)
    modified_result_data = apply_modifiers(original_result, modifier_str)

    # collect results for return
    result['roll_results'] = roll_results
    result['original_result'] = original_result
    result['modified_result'] = modified_result_data['result']
    result['bonuses'] = modified_result_data['bonuses']
    result['penalties'] = modified_result_data['penalties']

    if original_result > 0:
        result['success'] = True

    return result
