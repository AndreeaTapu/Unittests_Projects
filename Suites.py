import unittest
import HtmlTestRunner
from Tests_SeleniumWebDriver import Login


class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_de_rulat = unittest.TestSuite()
        test_de_rulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Login)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Test Execution Report",
            report_name="Test Results")

        runner.run(test_de_rulat)
