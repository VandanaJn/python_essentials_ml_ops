import re
import click

sample_banned_words = ["badword1", "badword2", "badword3"]
sample_comments = [
    "This is a clean comment.",
    "This comment contains Badword1.",
    "Another clean comment here.",
    "Yet another comment with badword2 and badWord3.",
]


def clean_comments(comments, banned_words):
    cleaned_comments = []
    for comment in comments:
        sanitized_comment = clean_comment_text(comment, banned_words)

        cleaned_comments.append(sanitized_comment)
    return cleaned_comments


@click.command()
@click.argument("comment", type=str)
@click.option("--banned", multiple=True, help="Words to censor")
def clean_comment(comment, banned):
    """
    Sanitize a comment by replacing banned words.

    COMMENT is the input string to be cleaned.
    """

    click.echo(clean_comment_text(comment, banned))


def clean_comment_text(comment, banned):
    sanitized_comment = comment
    for banned_w in banned:
        pattern = re.compile(re.escape(banned_w), re.IGNORECASE)
        sanitized_comment = pattern.sub("*" * len(banned_w), sanitized_comment)
    return sanitized_comment


# pylint: disable=no-value-for-parameter
if __name__ == "__main__":
    clean_comment()
