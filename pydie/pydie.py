import re
import qrand

# import pdb


def roll(multiplier, die, modifier_str=''):
    modifier_str = '' if modifier_str is None else modifier_str

    # re will capture the digits from "d20"
    rDie = r'(\d+)'

    # re will match a +n or -n and capture the "n"
    rBonuses = r'\+(\d+)'
    rPenalties = r'-(\d+)'

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
    roll_results = qrand.qnum_ranged_set(multiplier, max_num)

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
