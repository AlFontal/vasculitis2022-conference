import pandas as pd


def add_date_columns(df: pd.DataFrame, date_column: str = 'date', index_date: bool = False) -> pd.DataFrame:
    """
    Adds month number (int), month name (str), week day number (int, 0-idx) and week day name (str) to a data frame.
    Parameters
    ----------
    df
        Pandas data frame with at least a datetime column
    date_column
        Name of the column to use as date
    index_date
        If True, will override the `date_column` value and use current index as date column.
        Will fail with MultiIndex.
    Returns
    -------
    pd.DataFrame
        Data Frame with the added `month`, `month_name`, `week_day` and `week_day_name` columns.
    """

    if index_date:
        date_column = df.index.name
        df = df.reset_index()
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    df = df.assign(year=lambda dd: dd[date_column].dt.year,
                   month=lambda dd: dd[date_column].dt.month,
                   month_name=lambda dd: pd.Categorical(dd[date_column].dt.strftime('%b'),
                                                        categories=month_names, ordered=True),
                   week=lambda dd: dd[date_column].dt.isocalendar().week,
                   week_day=lambda dd: dd[date_column].dt.strftime('%w'),
                   week_day_name=lambda dd: pd.Categorical(dd[date_column].dt.strftime('%a'),
                                                           categories=day_names, ordered=True))

    if index_date:
        df = df.set_index(date_column)

    return df