import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import main

class TestUsdtSafetyGuardian(unittest.TestCase):

    def test_analyze_text_risk_with_scam_keywords(self):
        """
        Tests that analyze_text_risk correctly identifies multiple scam keywords in a string.
        """
        test_text = "This is a test for flash usdt and guaranteed profit."
        expected_keywords = ["flash usdt", "guaranteed profit"]
        found_keywords = main.analyze_text_risk(test_text)
        self.assertEqual(sorted(found_keywords), sorted(expected_keywords))

    def test_analyze_text_risk_with_no_scam_keywords(self):
        """
        Tests that analyze_text_risk returns an empty list when no scam keywords are present.
        """
        test_text = "This is a safe and legitimate message."
        found_keywords = main.analyze_text_risk(test_text)
        self.assertEqual(found_keywords, [])

    def test_analyze_text_risk_is_case_insensitive(self):
        """
        Tests that keyword detection is case-insensitive.
        """
        test_text = "FLASH USDT and PRIVATE KEY"
        expected_keywords = ["flash usdt", "private key"]
        found_keywords = main.analyze_text_risk(test_text)
        self.assertEqual(sorted(found_keywords), sorted(expected_keywords))

    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_safety_report_for_scam_text(self, mock_stdout):
        """
        Tests that generate_safety_report prints a warning for scam-related text.
        """
        scam_text = "Get our flash usdt tool now for guaranteed profit!"
        main.generate_safety_report(scam_text)
        output = mock_stdout.getvalue()
        self.assertIn("🚨 WARNING: Potential scam-related language detected!", output)
        self.assertIn("- flash usdt", output)
        self.assertIn("- guaranteed profit", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_safety_report_for_safe_text(self, mock_stdout):
        """
        Tests that generate_safety_report prints a safe message for legitimate text.
        """
        safe_text = "This is a legitimate message about USDT."
        main.generate_safety_report(safe_text)
        output = mock_stdout.getvalue()
        self.assertIn("✅ No direct scam-related keywords were found.", output)

if __name__ == '__main__':
    unittest.main()
