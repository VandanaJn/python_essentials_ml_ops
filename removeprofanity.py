import re
banned_word=["badword1", "badword2", "badword3"]
comments = [
    "This is a clean comment.",
    "This comment contains Badword1.",
    "Another clean comment here.",
    "Yet another comment with badword2 and badWord3."]


def clean_comments(comments, banned_word):
    clean_comments=[]    
    for comment in comments:
        sanitized_comment=comment
        for banned in banned_word:
            pattern=re.compile(re.escape(banned),re.IGNORECASE)
            sanitized_comment=pattern.sub("*"*len(banned),sanitized_comment)
                
        clean_comments.append(sanitized_comment)
    return clean_comments

print(clean_comments(comments, banned_word))

    