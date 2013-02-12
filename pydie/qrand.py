import urllib
import json
import settings
import exceptions


# see: http://en.wikipedia.org/wiki/65536_(number)
# api example: https://qrng.anu.edu.au/API/api-demo.php
def request_uint16_response(length=1):
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


def rand_uint16_list(length, max, min=1):
    uint16_response = request_uint16_response(length)
    uint16_list = uint16_response['data']
    ranged_uint16_list = reduce_uint16_list_to_range(uint16_list, max, min)

    return ranged_uint16_list


def rand_uint16(max, offset=1):
    uint16_response = request_uint16_response(1)
    uint16_list = uint16_response['data']
    ranged_uint16 = reduce_uint16_to_range(uint16_list[0], max)

    return ranged_uint16


def reduce_uint16_to_range(integer, max, offset=1):
    modulus = settings.MAX_INT / max
    ranged_uint16 = integer / modulus + offset

    return ranged_uint16


def reduce_uint16_list_to_range(uint16_list, max, offset=1):
    modulus = settings.MAX_INT / max
    ranged_uint16_list = [(x / modulus) + offset for x in uint16_list]

    return ranged_uint16_list
