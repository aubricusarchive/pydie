from __future__ import absolute_import

import sys
import os
sys.path.insert(0, os.path.abspath('../'))

import unittest
from pydie import exceptions
# from pydie import pydie
from pydie import qrand
from pydie import settings


class PyDieTestSuite(unittest.TestCase):

    def setUp(self):
        self.min_uint = 1
        self.max_uint = 20
        self.qset_length = 100
        self.qresponse = qrand.request_uint16_response(self.qset_length)

    def test_request_uint16_response_failure(self):
        with self.assertRaises(exceptions.AnuApiFailed):

            # raise exceptions.AnuApiFailed()
            qrand.request_uint16_response(settings.MAX_SET_LENGTH + 1)

    def test_request_uint16_response(self):

        success = self.qresponse['success']
        length_match = len(self.qresponse['data'])

        self.assertTrue(success and length_match)

    def test_uint16_to_range(self):
        quint = self.qresponse['data'][0]
        quint_ranged = qrand.reduce_uint16_to_range(quint, self.max_uint, self.min_uint)
        is_in_range = (quint_ranged >= self.min_uint and quint_ranged <= self.max_uint)

        self.assertTrue(is_in_range)

    def test_reduce_uint16_list_to_range(self):
        quint_list = self.qresponse['data']
        quint_list_ranged = qrand.reduce_uint16_list_to_range(quint_list, self.max_uint, self.min_uint)
        quint_list_sum = sum(quint_list_ranged)
        quint_list_max_sum = self.max_uint * self.qset_length

        # List is likely full of correctly ranged numbers if the sum of the list
        # is not greater than the length of the set * the max value.
        is_in_range = quint_list_sum <= quint_list_max_sum

        self.assertTrue(is_in_range)
