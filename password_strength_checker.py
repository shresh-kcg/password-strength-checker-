"""
Password Strength Checker
--------------------------
A simple mini-project that asks the user for:
1. The portal/website the password is for
2. The password itself
Then checks it against common strength conditions and gives feedback.
"""

import re
import getpass


def check_password_strength(password: str):
    """
    Checks a password against common strength rules.
    Returns (score, max_score, list_of_failed_conditions)
    """
    conditions = {
        "At least 8 characters long": len(password) >= 8,
        "Contains an uppercase letter (A-Z)": bool(re.search(r"[A-Z]", password)),
        "Contains a lowercase letter (a-z)": bool(re.search(r"[a-z]", password)),
        "Contains a digit (0-9)": bool(re.search(r"[0-9]", password)),
        "Contains a special character (!@#$%^&* etc.)": bool(
            re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=~`\[\];'/\\]", password)
        ),
        "No spaces": " " not in password,
    }

    passed = [rule for rule, ok in conditions.items() if ok]
    failed = [rule for rule, ok in conditions.items() if not ok]

    score = len(passed)
    max_score = len(conditions)
    return score, max_score, failed


def get_strength_label(score: int, max_score: int) -> str:
    ratio = score / max_score
    if ratio == 1.0:
        return "Very Strong 💪"
    elif ratio >= 0.8:
        return "Strong ✅"
    elif ratio >= 0.6:
        return "Moderate ⚠️"
    elif ratio >= 0.4:
        return "Weak ❗"
    else:
        return "Very Weak ❌"


def main():
    print("=" * 50)
    print("        PASSWORD STRENGTH CHECKER")
    print("=" * 50)

    portal = input("Which portal/website is this password for? ").strip()

    # Using getpass hides the password while typing (in a real terminal).
    # If it fails (e.g. some IDEs), it falls back to a normal visible input.
    try:
        password = getpass.getpass("Enter the password to check: ")
    except Exception:
        password = input("Enter the password to check: ")

    if not password:
        print("\nNo password entered. Exiting.")
        return

    score, max_score, failed = check_password_strength(password)
    strength = get_strength_label(score, max_score)

    print("\n" + "-" * 50)
    print(f"Portal      : {portal if portal else 'Not specified'}")
    print(f"Score       : {score}/{max_score}")
    print(f"Strength    : {strength}")
    print("-" * 50)

    if failed:
        print("\nSuggestions to improve your password:")
        for rule in failed:
            print(f"  - {rule}")
    else:
        print("\nGreat job! Your password meets all recommended conditions.")

    print("\nNote: Avoid reusing the same password across multiple portals,")
    print("and never share your real passwords with untrusted programs.")


if __name__ == "__main__":
    while True:
        main()
        again = input("\nCheck another password? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break
