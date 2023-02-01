def inc(x):
    return x + 2


def test_answer():
    assert inc(3) == 5


import pandas as pd


def test_dataframe():
    df = pd.DataFrame([1, 2, 3], columns=["colname1"])
    df.to_csv("./tests/test.csv")
