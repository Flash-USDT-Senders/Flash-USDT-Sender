# USDT Safety Guardian Agent

import re

# Dictionary of high-risk keywords and their associated risk scores
SCAM_KEYWORDS = {
    "flash usdt": 10,
    "sender tool": 10,
    "unconfirmed transfer": 10,
    "mirroring": 10,
    "fast sender": 8,
    "bypass blockchain": 10,
    "guaranteed profits": 8,
    "activation fee": 7,
    "private keys": 10,
    "seed phrase": 10,
    "unlock tool": 7,
    "disappearing usdt": 10,
    "spendable crypto": 9,
    "cloning balance": 10,
}

def assess_scam_risk(text):
    """
    Analyzes a given text for high-risk keywords and returns a risk assessment.
    """
    if not isinstance(text, str):
        return "Invalid input: Please provide a string."

    text_lower = text.lower()
    total_risk_score = 0
    detected_keywords = []

    for keyword, score in SCAM_KEYWORDS.items():
        if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
            total_risk_score += score
            detected_keywords.append(keyword)

    if total_risk_score >= 10:
        return f"SCAM: Detected high-risk keywords: {', '.join(detected_keywords)}"
    elif total_risk_score >= 7:
        return f"Suspicious: Detected potentially risky keywords: {', '.join(detected_keywords)}"
    else:
        return "Safe: No high-risk keywords detected."

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="USDT Safety Guardian Agent")
    parser.add_argument("text", type=str, help="Text to analyze for scam patterns.")
    args = parser.parse_args()

    risk_assessment = assess_scam_risk(args.text)
    print(risk_assessment)
