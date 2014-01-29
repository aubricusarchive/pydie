from __future__ import absolute_import

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath('../'))

class TestPydie(unittest.TestCase):

    def setUp(self):
        pass

    # parser tests

    def test_parse_roll(self):
        # test 1d3
        # test 2d8m+1
        # test 3d10m-1
        # test 4d12m+1-1
        # test 5d20+1-2+1 6d20-1+2-3
        pass

    # anu tests

    def test_fetch_uint8(self):
        pass

    def test_fetch_uint16(self):
        pass

    def test_fetch_hex16(self):
        pass

    def test_anu_rand(self):
        pass

    def test_anu_randint(self):
        pass


    # cli tests

    def test_got_roll(self):
        pass
