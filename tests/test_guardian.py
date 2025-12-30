import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from guardian import assess_scam_risk

class TestGuardian(unittest.TestCase):

    def test_safe_text(self):
        """Tests that a safe text is correctly identified."""
        text = "This is a legitimate message about USDT."
        self.assertEqual(assess_scam_risk(text), "Safe: No high-risk keywords detected.")

    def test_suspicious_text(self):
        """Tests that a suspicious text is correctly identified."""
        text = "You can get guaranteed profits with this tool."
        self.assertIn("Suspicious", assess_scam_risk(text))

    def test_scam_text(self):
        """Tests that a scam text is correctly identified."""
        text = "I have a flash usdt sender tool for sale."
        self.assertIn("SCAM", assess_scam_risk(text))

    def test_invalid_input(self):
        """Tests that a non-string input is handled correctly."""
        text = 123
        self.assertEqual(assess_scam_risk(text), "Invalid input: Please provide a string.")

    def test_empty_string(self):
        """Tests that an empty string is handled correctly."""
        text = ""
        self.assertEqual(assess_scam_risk(text), "Safe: No high-risk keywords detected.")

    def test_mixed_case_keywords(self):
        """Tests that mixed case keywords are detected."""
        text = "I have a FLASH USDT sender tool for sale."
        self.assertIn("SCAM", assess_scam_risk(text))

    def test_multiple_keywords(self):
        """Tests that multiple keywords are detected."""
        text = "This flash usdt sender tool gives guaranteed profits."
        result = assess_scam_risk(text)
        self.assertIn("SCAM", result)
        self.assertIn("flash usdt", result)
        self.assertIn("sender tool", result)
        self.assertIn("guaranteed profits", result)


if __name__ == '__main__':
    unittest.main()
