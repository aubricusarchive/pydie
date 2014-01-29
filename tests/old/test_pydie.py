from __future__ import absolute_import
from __future__ import division

import sys
import os
import unittest
import json
# import pdb

sys.path.insert(0, os.path.abspath('../'))

from pydie.api import anu
from pydie.utils import numbers
from pydie.cli import parse
from pydie.actions import roll


class TestPydie(unittest.TestCase):

    def setUp(self):
        with open('./tests/resources/uint8_mock.json') as json_file:
            uint8_mock = json.load(json_file)

        self.uint8_mock = uint8_mock

        with open('./tests/resources/uint16_mock.json') as json_file:
            uint16_mock = json.load(json_file)

        self.uint16_mock = uint16_mock

    def tearDown(self):
        self.uint8_mock = None
        self.uint16_mock = None

    # api tests
    def test_fetch(self):
        response = anu.fetch_list(anu.TYPE_UINT16, anu.MAX_BLOCK_SIZE, length=10)
        success = response['success']
        data = response['data']
        length = len(data)

        assert success
        assert length == 10

    def test_fetch_uint8(self):
        response = anu.fetch_list(anu.TYPE_UINT8, anu.MAX_BLOCK_SIZE, length=10)
        success = response['success']
        data = response['data']
        length = len(data)

        assert success
        assert length == 10
        assert 0 <= data[0] <= numbers.MAX_UINT8

    def test_fetch_uint16(self):
        response = anu.fetch_list(anu.TYPE_UINT16, anu.MAX_BLOCK_SIZE, length=10)
        success = response['success']
        data = response['data']
        length = len(data)

        assert success
        assert length == 10
        assert 0 <= data[0] <= numbers.MAX_UINT16

    # parsing testing
    def test_parse_multipliers(self):
        paramlist = ['2', '1']
        multipliers = parse.multipliers(paramlist)

        assert len(multipliers) == len(paramlist)
        assert all(isinstance(multiplier, int) for multiplier in multipliers)

    def test_parse_die(self):
        paramlist = ['d6', 'd20']
        die = parse.die(paramlist)

        assert all(isinstance(dice, int) for dice in die)
        assert die[0] == 6
        assert die[1] == 20

    def test_parse_modifiers(self):
        paramlist = ['+1+2-3', '-3-2+1']
        modifiers = parse.modifiers(paramlist)

        bonuses = modifiers['bonuses']
        penalties = modifiers['penalties']

        assert all(
            [
                [isinstance(bonus, int) for bonus in bonus_set]
                for bonus_set in bonuses
            ]
        )

        assert all(
            [
                [isinstance(penalty, int) for penalty in penalty_set]
                for penalty_set in penalties
            ]
        )

        assert sum(bonuses[0]) == 3
        assert sum(bonuses[1]) == 1
        assert sum(penalties[0]) == 3
        assert sum(penalties[1]) == 5

    def test_parse_empty_modifiers(self):
        paramlist = []
        modifiers = parse.modifiers(paramlist)

        assert isinstance(modifiers['bonuses'], list)
        assert isinstance(modifiers['penalties'], list)

    # utils testing
    def test_reduce_uint_list_to_range(self):
        min = 0
        max = 20
        numlist = self.uint8_mock['data']
        ranged = numbers.reduce_uint_list_to_range(
            anu.TYPE_UINT8,
            numlist,
            min=min,
            max=max
        )

        assert all(0 <= x <= max for x in ranged)

    def test_shuffle_for_count(self):
        uint16_data = self.uint16_mock['data']
        mock_len = len(uint16_data)
        numlist = list(uint16_data)
        count = 10
        numbers.shuffle_for_count(numlist, count)

        # create score for non macting indicies
        score = sum([1 for i in range(mock_len - 1) if uint16_data[i] != numlist[i]])
        score = score/mock_len * 100

        assert id(uint16_data) != id(numlist)
        assert score > 0.8

    def test_pick(self):
        uint16_data = self.uint16_mock['data']
        choices = [0, 1, 2, 3, 4]
        picks = numbers.pick(uint16_data, choices)

        assert all(uint16_data[i] == picks[i] for i in range(5))

    # action testing
    def test_action_roll(self):
        raw_multipliers = ['2', '1']
        raw_die = ['d6', 'd20']
        raw_modifiers = ['+1+2-3', '-3-2+1']

        multipliers = parse.multipliers(raw_multipliers)
        die = parse.die(raw_die)
        modifiers = parse.modifiers(raw_modifiers)

        roll_results = roll(multipliers, die, modifiers['bonuses'], modifiers['penalties'])
        print roll_results

    def verify_roll_result(self, result):
        rolls = result['rolls']
        raw_result = result['raw']
        roll_result = result['result']
        bonuses = result['bonuses']
        penalties = result['penalties']
        sides = result['sides']
        multiplier = result['multiplier']

        assert len(rolls) == multiplier
        assert raw_result <= (sides * multiplier)
        assert sum(bonuses) == (2+4)
        assert sum(penalties) == (1+3)
        assert roll_result == (raw_result + sum(bonuses) - sum(penalties))
