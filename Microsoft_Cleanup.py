# tn_budget['production_budget'] = tn_budget['production_budget'].apply(lambda x: x.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')))
# tn_budget['production_budget'] = pd.to_numeric(tn_budget.production_budget, downcast = 'float', errors = 'coerce')
import pandas as pd

def cast_to_float32(df, col_name):
    df[col_name] = df[col_name].apply(lambda x: x.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')))
    df[col_name] = pd.to_numeric(df[col_name], downcast = 'float', errors = 'coerce')
    pass
