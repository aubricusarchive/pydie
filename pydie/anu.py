from __future__ import division

import urllib
import json

from collections import deque

from pydie.enums import TYPE_UINT8
from pydie.enums import TYPE_UINT16
from pydie.enums import TYPE_HEX16
from pydie.enums import MAX_UINT8
from pydie.enums import MAX_UINT16

ANU_API_URL = 'https://qrng.anu.edu.au/API/jsonI.php'
MAX_BLOCK_SIZE = '1024'  # applies only to hex16
MAX_SET_LENGTH = '1024'

def fetch(uinttype, length=1, size=6):
    """
    Fetch a list of numbers from the ANU api

    Arguments:
    uinttype -- The ANU supported uinttype, see pydie.enums
    length -- The length of the number set you wish to fetch
    size -- The block size 1-1024; only applies to uint type HEX16

    Returns:
    dict

    """
    params = urllib.urlencode(
        {
            'type': uinttype,
            'size': min(int(size), MAX_BLOCK_SIZE),
            'length': min(int(length), MAX_SET_LENGTH)
        }
    )

    url = '?'.join((ANU_API_URL, params))

    response = json.loads(urllib.urlopen(url).read())

    if response['success'] is True:
        return response

    else:
        raise Exception("\n\nError encountered when requesting data: \n- url: {0}\n- response: {1}\n".format(
            url,
            response
        ))

def fetch_uint8(length=1):
    """Fetch list of uint8 (number between 0-255) from the ANU API.
    """
    fetch(TYPE_UINT8, length=length)


def fetch_uint16(length=1):
    """Fetch list of uint16 (number between 0-65535) from ANU API.
    """
    fetch(TYPE_UINT16, length=length)


def fetch_hex16(size=1, length=6):
    """Fetch list of hex16 (number between 0000-ffff) from ANU API.
    """
    fetch(TYPE_HEX16, length=length, size=size)


def rand(min=0, max=1, length=1, uinttype=TYPE_UINT16, size=6):
    """Fetch a list of random uints with in a range from the ANU API

    Keyword Arguments:
    min -- the minimum number of the range
    max -- the maximum number of the range
    length -- the length of the random number set to be returned
    uintype -- any of 3 supported ANU uint types, see fetch methods
    size -- size of hex16 block, hex16 only

    Returns:
    list
    """

    response = fetch(uinttype, length=length, size=size)
    numlist = deque(response['data'])

    # TODO: Revisit, small hack
    # - For whatever reason I need to subtract 1 from max to get numbers
    #   between min and max (w/o -1 it produced number over max)
    # - It "kinda" makes sense, but need to make sure this is
    #   working correctly
    modulus = get_uintmax(uinttype) / float(max-1)

    # flatten raw anu numbers to (min/max) range
    result = [x / modulus + min for x in numlist]

    return result

def randint(min=0, max=1, length=1, uinttype=TYPE_UINT16, size=6):
    """Fetch a list of random uints within a range from the ANU API.

    Wraps rand, but casts results to int.
    """

    return [int(round(x)) for x in rand(**locals())]


def get_uintmax(uinttype):
    """Returns the max int value for uinttype."""

    if uinttype == TYPE_UINT16:
        return MAX_UINT16

    elif uinttype == TYPE_UINT8:
        return MAX_UINT8

    else:
        raise Exception('Unsupported uinttype passed {0}'.format(uinttype))
