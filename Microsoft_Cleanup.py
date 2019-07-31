import pandas as pd

def cast_to_float32(df, col_name):
    df[col_name] = df[col_name].apply(lambda x: x.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')))
    df[col_name] = pd.to_numeric(df[col_name], downcast = 'float', errors = 'coerce')
    pass

def cast_to_str(df, col_name):
    df[col_name] = df[col_name].astype(str)
    pass

def cast_to_int(df, col_name):
    df[col_name] = df[col_name].astype(int)
    pass

def fill_na(df, col_name):
    df[col_name] = df[col_name].fillna('Unknown' or 'Not listed')
    pass

def net_columns(df, col_name1, col_name2):
    df['net'] = list(df.apply(lambda x: x[col_name1] - x[col_name2], axis=1))
    pass

def divide_columns(df, col_name1, col_name2):
    df['ratio'] = list(df.apply(lambda x: x[col_name1] / x[col_name2], axis=1))
    pass

def rename_col(df, col_name, new_name):
    df.rename(columns={col_name: new_name}, inplace=True)
    pass

def cleanup_text(df, col_name):
    years = ['\(2010\)', "\(2011\)",
             "\(2012\)", "\(2013\)", "\(2014\)",
             "\(2015\)", "\(2016\)", "\(2017\)", "\(2018\)"]
    df[col_name] = df[col_name].replace(years, value='', regex=True)
    df[col_name] = df[col_name].str.strip()
    df[col_name] = df[col_name].apply(lambda x: x.lower())
    df[col_name] = df[col_name].\
    apply(lambda x: x.translate(str.maketrans
                                 ('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')))
    df[col_name] = df[col_name].replace(['the', 'and'], value='', regex=True)
    pass

def convert_year(df, col_name):
    df['year'] = list(df[col_name].str[-4:])
    pass

def drop_cols(df, *args):
    foo = []
    for i in args:
        foo.append(i)
    df.drop(columns=foo, inplace=True, axis=1)
    pass

def cutoff_series_at(df, col_name, criteria):
    df = df.loc[df[col_name] >= criteria]
    pass

def subset_series(df, col_name, criteria):
    subset = df.loc[df[col_name] == criteria]
    return subset

def remove_duplicates(df, col_name):
    df.loc[~(df[col_name].duplicated())]
    pass

def left_merge(df1, df2, *args):
    foo = []
    for i in args:
        foo.append(i)
    new = pd.merge(df1, df2, on=foo, how='left')
    return new
