import urllib
import json
import settings

# import pdb

# see: http://en.wikipedia.org/wiki/65536_(number)
# api example: https://qrng.anu.edu.au/API/api-demo.php


# todo: should error if result is bad
def request_qnum_set(length=1):
    result = [-1]
    url = settings.ANU_API_URL + urllib.urlencode({
        'type': settings.QNUM_TYPE,
        'size': settings.QNUM_SIZE,
        'length': length,
    })

    response = json.loads(urllib.urlopen(url).read())

    if(
        response['success'] is True and
        response['length'] is length
    ):
        result = response['data']

    return result


def qnum_set_to_range(qset, max, min=1):
    qnum_range = max - min
    modulus = settings.MAX_INT / qnum_range

    ranged_set = [(x / modulus) + min for x in qset]
    return ranged_set


def qnum_ranged_set(length, max, min=1):
    qset = request_qnum_set(length)
    ranged_set = qnum_set_to_range(qset, max, min)
    return ranged_set
