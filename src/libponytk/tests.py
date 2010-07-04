# -*- encoding: utf-8 -*-
import unittest

from .core import utils


class UtilsTest(unittest.TestCase):
    def testSlug(self):
        valid_slug = 'ab-._c'
        invalid_slug = '_-.0'
        self.assertEqual(True, utils.is_valid_slug(valid_slug))
        self.assertEqual(False, utils.is_valid_slug(invalid_slug))
        pass

def test_all():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(UtilsTest))
    return suite
