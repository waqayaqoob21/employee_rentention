import pandas as pd
import numpy as np

# Helper to clean numeric columns
def clean_numeric_column(df, column_name):
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    df[column_name] = df[column_name].fillna(df[column_name].median())
    return df

# Helper to standardize text columns
def standardize_text_column(df, column_name, fillna_value='Unknown'):
    df[column_name] = df[column_name].str.title()
    df[column_name] = df[column_name].fillna(fillna_value)
    return df

# Handle email validity
def filter_valid_emails(df, email_column='Email'):
    df['Email_Valid'] = df[email_column].apply(lambda x: isinstance(x, str) and '@' in x and '.' in x)
    df = df[df['Email_Valid']].drop('Email_Valid', axis=1)
    return df

# Engineer tenure
def engineer_tenure(df):
    df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce', dayfirst=True)
    df['Leave_Date'] = pd.to_datetime(df['Leave_Date'], errors='coerce', dayfirst=True)
    df['Leave_Date'] = df['Leave_Date'].fillna(pd.Timestamp('today'))
    df['Tenure_Days'] = (df['Leave_Date'] - df['Join_Date']).dt.days
    df['Tenure_Years'] = df['Tenure_Days'] / 365.0
    return df