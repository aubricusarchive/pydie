import urllib
import json
import settings

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
        response['length'] == length
    ):
        result = response

    return result


def qnum_ranged_set(length, max, min=1):
    qset = request_qnum_set(length)
    return qnum_set_to_range(qset, max, min)


def qnum_set_to_range(qset, max, min=1):
    qnum_range = max - min
    modulus = settings.MAX_INT / qnum_range

    return [(x / modulus) + min for x in qset]
