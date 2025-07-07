import sys
def pwd_checker(pwd:str):
    common_words=["hello","test","password","abcd"]
    lenth=len(pwd)
    if lenth<8:
        return "too short"
    has_digit=any(c.isdigit() for c in pwd)
    has_special_char=any(not c.isalnum() for c in pwd)
    has_upper=any(c.isupper() for c in pwd)
    has_lower=any(c.islower() for c in pwd)
    score= int(has_digit)+int(has_special_char)+int(has_upper)+int(has_lower)
    if any(word in pwd.lower() for word in common_words):
        score-=1

    if score==4:
        return "strong"
    if score==3:
        return "moderate"
    return "weak"

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: password_checker.py <password>")
    else:
        print(f"{sys.argv[1]} is {pwd_checker(sys.argv[1])}")



