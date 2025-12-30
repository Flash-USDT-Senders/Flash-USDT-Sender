import argparse
import re

# Keywords and patterns associated with scams
SCAM_KEYWORDS = [
    "flash usdt", "fast sender", "unconfirmed transfer", "disappearing usdt",
    "bypass blockchain", "mirroring balance", "cloning balance", "activation fee",
    "guaranteed profit", "private key", "seed phrase"
]

def analyze_text_risk(text):
    """
    Analyzes text for keywords and patterns associated with common crypto scams.
    """
    found_keywords = []
    for keyword in SCAM_KEYWORDS:
        if re.search(r'\b' + re.escape(keyword) + r'\b', text, re.IGNORECASE):
            found_keywords.append(keyword)
    return found_keywords

def generate_safety_report(text):
    """
    Generates a safety report based on the analysis of the provided text.
    """
    found_keywords = analyze_text_risk(text)

    print("--- USDT Safety Guardian Report ---")
    print(f"\nAnalyzing the following text: \"{text[:100]}...\"")

    if not found_keywords:
        print("\n✅ No direct scam-related keywords were found.")
        print("However, always remain cautious and follow best practices.")
    else:
        print("\n🚨 WARNING: Potential scam-related language detected!")
        print("The following keywords, commonly used in scams, were found:")
        for keyword in found_keywords:
            print(f"  - {keyword}")

    print("\n--- 🛡️ Safety Checklist ---")
    print("- [ ] Have you verified the identity of the person or service?")
    print("- [ ] Are they making promises that sound too good to be true (e.g., guaranteed profits)?")
    print("- [ ] Are they pressuring you to act quickly?")
    print("- [ ] Are they asking for an 'activation fee' or other upfront payment?")
    print("- [ ] MOST IMPORTANTLY: Have they asked for your private keys or seed phrase?")
    print("\nNEVER share your private keys or seed phrase with anyone.")
    print("\n--- End of Report ---")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="USDT Safety Guardian: Analyze text for common crypto scam language.",
        epilog="Stay safe and protect your assets. Never share your private keys."
    )
    parser.add_argument(
        "text",
        type=str,
        help="The text to analyze (e.g., a message, an advertisement, a website's text)."
    )

    args = parser.parse_args()

    generate_safety_report(args.text)
