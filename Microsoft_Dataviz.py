import pandas as pd

def take_top_values_descending(df, col_name, slice):
    foo = df.sort_values(by=[col_name], ascending=False)[:slice]
    return foo

def take_top_mean_descending(df, index, col_name, slice1, slice2):
    foo = df.groupby([index])[col_name].mean().sort_values(ascending=False)[slice1:slice2]
    return foo

def cast_to_list(df, col_name):
    foo = list(df[col_name])
    return foo

def two_col_pivot_table_mean_nunique(df, index, col1, col2, slice1, slice2):
    foo = df.groupby([index])[col1, col2].agg({col1: 'mean', col2: 'nunique'})\
    .sort_values(by=[col1], ascending=False)[slice1:slice2].reset_index()
    return foo
