#!/usr/bin/env python2

import sys
import unittest
from tests.tests import Tests
from tests.suites.tests_send_document import TestsSendDocuments


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(Tests),
    ))
    suite1 = unittest.TestSuite((
        unittest.makeSuite(TestsSendDocuments),
    ))
    result = unittest.TextTestRunner().run(suite)
    result1 = unittest.TextTestRunner().run(suite1)
    sys.exit(not result.wasSuccessful() or not result.wasSuccessful())

