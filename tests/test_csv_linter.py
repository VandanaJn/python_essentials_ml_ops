from csv_linter import raw_header_duplicates, carriage_returns, unnamed_columns, \
    zero_count_columns, main
import pandas as pd
from click.testing import CliRunner

def test_raw_header_duplicates():
    l=raw_header_duplicates("carriage.csv")
    assert l==['notes']

def test_raw_header_duplicates():
    df = pd.read_csv("carriage.csv", dtype=str)
    fields=carriage_returns(df)
    assert fields==(0, 'notes','Aged in French, Hungarian, and American Oak barrels, this is a big voluptuous wine made in Bordeaux style that will age for years. ,kjhh,abc\r\nAromas of cherry, cedar, cassis, and chocolate, coupled with a velvety finish, give this wine a smooth, mouth filling memory of Cabernet Sauvignon.' )

def test_zero_count_columns():
    df = pd.read_csv("carriage.csv", dtype=str)
    l=zero_count_columns(df)
    assert l==['grape', 'notes.1']

def test_unnamed_columns():
    df = pd.read_csv("carriage.csv", dtype=str)
    no=unnamed_columns(df)
    assert no==1

def test_main():
    runner=CliRunner()
    result = runner.invoke(main, ["carriage.csv"])
    assert result.exit_code == 0
    r= result.output.strip() 
    assert "Warning: found duplicate columns: ['notes']" in r
    assert "Warning: Column 'grape' has no items in it" in r
    assert "Warning: Column 'notes.1' has no items in it" in r
    assert "Warning: found 1 columns that are Unnamed" in r
    assert "Warning: found carriage returns at index 0 of column 'notes':\n         'Aged in French, Hungarian, and American Oak barrel'" in r
    

