# cmd line usage: 
# python rec_monthlytable_wide2long.py path/to/monthly_table.csv

import pandas as pd
import argparse


def monthlytable_wide2long(monthly_table_path):
    """Transform the monthly pud table from wide to long format, facilitating groupbys, etc
    Input: 
        monthly_table_path(string): file path to the table, usually called 'monthly_table.csv'
        
    Output:
        'monthlytable_long.csv':
        with columns ['year', 'month', 'poly_id', 'total_pud']
    """
    dat = pd.read_csv(monthly_table_path)
    datlong = pd.melt(frame=dat, id_vars='poly_id')
    datlong['year'], datlong['month'] = datlong['variable'].str.split('-', 1).str
    datlong.drop(axis=1, labels='variable', inplace=True)
    datlong.rename(columns={'value':'total_pud'}, inplace=True)
    out = datlong[['year', 'month', 'poly_id', 'total_pud']]
    out.to_csv('monthlytable_long.csv', index=False)
    return None


parser = argparse.ArgumentParser()
parser.add_argument('table_path')
args = parser.parse_args()
monthlytable_wide2long(args.table_path)

