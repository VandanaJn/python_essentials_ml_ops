# import sys
import argparse


def pwd_checker(pwd: str, check_common_word=True):
    common_words = ["hello", "test", "password", "abcd"]
    lenth = len(pwd)
    if lenth < 8:
        return "too short"
    has_digit = any(c.isdigit() for c in pwd)
    has_special_char = any(not c.isalnum() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    score = int(has_digit) + int(has_special_char) + int(has_upper) + int(has_lower)
    if check_common_word and any(word in pwd.lower() for word in common_words):
        score -= 1

    if score == 4:
        return "strong"
    if score == 3:
        return "moderate"
    return "weak"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a passwordchecker")
    parser.add_argument("--password", help="password to evaluate")
    parser.add_argument(
        "--chk_cmn_wrd", action="store_true", help="flag for checking common words"
    )
    args = parser.parse_args()
    print(args.chk_cmn_wrd)
    print(f"{args.password} is {pwd_checker(args.password, args.chk_cmn_wrd)}")

