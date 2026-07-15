"""
password_checker.py
Week 2 - VortexTech Cyber Security Internship
"""

# a small list of really common passwords that people still use
# if the input matches any of these, we fail it immediately no matter what
common_passwords = [
    "123456", "password", "123456789", "12345678", "12345",
    "1234567", "qwerty", "abc123", "111111", "password1",
    "iloveyou", "admin", "letmein", "monkey", "dragon",
    "master", "sunshine", "princess", "welcome", "shadow",
    "superman", "michael", "football", "123123", "654321"
]


def check_password(password):
    score = 0
    tips = []

    # first check - is this a super common password?
    if password.lower() in common_passwords:
        print(f"  --> VERY WEAK: This is one of the most common passwords out there. Instant crack.")
        print("-" * 55)
        return

    # length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        tips.append("Could be longer (12+ chars is safer)")
    else:
        tips.append("Too short, needs at least 8 characters")

    # uppercase check
    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Missing uppercase letters")

    # lowercase check
    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Missing lowercase letters")

    # number check
    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Missing numbers")

    # special character check - worth 2 points because it really does help a lot
    special_chars = "!@#$%^&*()_-+=[]{}|;:,.<>?"
    if any(c in special_chars for c in password):
        score += 2
    else:
        tips.append("Missing special characters (!@#$ etc.)")

    # decide rating
    if score >= 6:
        rating = "STRONG"
    elif score >= 4:
        rating = "MEDIUM"
    else:
        rating = "WEAK"

    print(f"  --> {rating} (Score: {score}/7)")
    if tips:
        print(f"  Feedback:")
        for t in tips:
            print(f"    - {t}")
    else:
        print(f"  All checks passed!")
    print("-" * 55)


# test passwords
test_list = [
    "123456",
    "hello",
    "Hello123",
    "P@ssw0rd!",
    "Secure#Pass99",
    "X9!mK@2vLq#Z",
    "password",
    "sunflower2024",
]

print("Checking passwords...")
print()
for i, pwd in enumerate(test_list, 1):
    print(f"[{i}] Testing: '{pwd}'")
    check_password(pwd)

print(f"\nDone. {len(test_list)} passwords tested.")
