import unittest
import HtmlTestRunner


def runSuite():
    html_report_dir = "./html_report"
    test_suite = unittest.TestSuite()
    all_test_cases = unittest.defaultTestLoader.discover('.', '*.py')
    for test_case in all_test_cases:
        test_suite.addTests(test_case)
    test_runner = HtmlTestRunner.HTMLTestRunner(output=html_report_dir)
    test_runner.run(test_suite)


if __name__ == '__main__':
    runSuite()
