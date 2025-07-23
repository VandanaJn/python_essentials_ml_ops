import click
import pandas as pd


def carriage_returns(df):
    for index, row in df.iterrows():
        for column, field in row.items():
            try:
                if "\r\n" in field:
                    return index, column, field
            except TypeError:
                continue


def unnamed_columns(df):
    bad_columns = []
    for key in df.keys():
        if "Unnamed" in key:
            bad_columns.append(key)
    return len(bad_columns)


def zero_count_columns(df):
    bad_columns = []
    for key in df.keys():
        if df[key].count() == 0:
            bad_columns.append(key)
    return bad_columns


def raw_header_duplicates(filename):
    with open(filename, "r", encoding="utf-8") as f:
        header = f.readline().strip().split(",")
    seen = set()
    duplicates = []
    for col in header:
        if col in seen:
            duplicates.append(col)
        seen.add(col)
    return duplicates


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def main(filename):
    df = pd.read_csv(filename, dtype=str)

    duplicates = raw_header_duplicates(filename)
    if len(duplicates) > 0:
        click.echo(f"Warning: found duplicate columns: {duplicates}")

    for column in zero_count_columns(df):
        click.echo(f"Warning: Column '{column}' has no items in it")
    unnamed = unnamed_columns(df)
    if unnamed:
        click.echo(f"Warning: found {unnamed} columns that are Unnamed")
    carriage_field = carriage_returns(df)
    if carriage_field:
        index, column, field = carriage_field
        click.echo(
            (
                f"Warning: found carriage returns at index {index}"
                f" of column '{column}':"
            )
        )
        click.echo(f"         '{field[:50]}'")


# pylint: disable=no-value-for-parameter
if __name__ == "__main__":
    main()
