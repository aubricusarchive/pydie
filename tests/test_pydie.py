from __future__ import absolute_import

import sys
import os
sys.path.insert(0, os.path.abspath('../'))

import unittest
from pydie import exceptions
from pydie import pydie
from pydie import qrand
from pydie import settings


class PyDieTestSuite(unittest.TestCase):

    def test_request_qnum_set_error(self):
        with self.assertRaises(exceptions.AnuApiFailed):
            # raise exceptions.AnuApiFailed()
            qrand.request_qnum_set(settings.MAX_SET_LENGTH + 1)
            pass

    def test_request_qnum_set(self):
        qset_response = qrand.request_qnum_set(10)
        self.assertTrue(qset_response['success'])

    def test_qnum_set_to_ranged_set(self):
        length = 10
        max = 20
        qset_response = qrand.request_qnum_set(length)
        qset = qset_response['data']
        qranged_set = qrand.qnum_set_to_ranged_set(qset, max)

        # we know our set is likely in range if the total of all values
        #   is less than our max value * length of the set
        self.assertTrue(sum(qranged_set) <= length * max)

    def test_d20(self):
        roll_result = pydie.roll(1, "d20")
        modified_result = roll_result['modified_result']

        self.assertTrue(modified_result >= 1 and modified_result <= 20)

    def test_d20_with_modifier(self):
        min = 1
        max = 20
        roll_result = pydie.roll(1, 'd20', '+3-2+5')
        bonuses = roll_result['bonuses']
        penalties = roll_result['penalties']
        modified_result = roll_result['modified_result']

        modified_max = max + sum(bonuses) - sum(penalties)

        self.assertTrue(modified_result >= min and modified_result <= modified_max)
