import urllib
import json
import settings

import exceptions
# import pdb

# see: http://en.wikipedia.org/wiki/65536_(number)
# api example: https://qrng.anu.edu.au/API/api-demo.php


# todo: should error if result is bad
def request_qnum_set(length=1):
    result = None
    url = settings.ANU_API_URL + urllib.urlencode({
        'type': settings.QNUM_TYPE,
        'size': settings.QNUM_SIZE,
        'length': length,
    })

    response = json.loads(urllib.urlopen(url).read())

    if(
        response['success'] is True
    ):
        result = response
    else:
        raise exceptions.AnuApiFailed(length)

    return result


def qnum_set_to_ranged_set(qset, max, min=1):
    # qnums range from 0 to our MAX_INT
    # factor by which to divide our resulting qnum
    # qnum / modulus will reduce the original numbe (0 - MAX_INT)
    #   to our range (0 - max)
    modulus = settings.MAX_INT / max

    # + min, typically 1 offsets our values by one because most d & d die
    #   do not have a zero value
    ranged_set = [(x / modulus) + min for x in qset]
    return ranged_set


def qnum_ranged_set(length, max, min=1):
    qset_response = request_qnum_set(length)
    qset = qset_response['data']
    ranged_set = qnum_set_to_ranged_set(qset, max, min)
    return ranged_set
