import urllib
import json
from .settings import Settings


class QRand(object):

    def __init__(self):
        super(QRand, self).__init__()

        # see: http://en.wikipedia.org/wiki/65536_(number)
        # api example: https://qrng.anu.edu.au/API/api-demo.php

    @staticmethod
    # todo: should error if result is bad
    def request_qnum_set(length=1):
        result = [-1]
        url = Settings.ANU_API_URL + urllib.urlencode({
            'type': Settings.QNUM_TYPE,
            'size': Settings.QNUM_SIZE,
            'length': length,
        })

        response = json.loads(urllib.urlopen(url).read())

        if(
            response['success'] is True and
            response['length'] == length
        ):
            result = response

        return result

    @staticmethod
    def qnum_ranged_set(length, max, min=1):
        qset = QRand.request_qnum_set(length)
        return QRand.qnum_set_to_range(qset, max, min)

    @staticmethod
    def qnum_set_to_range(qset, max, min=1):
        qnum_range = max - min
        modulus = Settings.MAX_INT / qnum_range

        return [(x / modulus) + min for x in qset]
