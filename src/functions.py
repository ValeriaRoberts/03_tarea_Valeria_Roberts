# Functions

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import logging
from pandas import DataFrame


def load_data(file_path):
    '''Def to read data

    Params:
        data file_path

    Returns:
        read function
    '''
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Data from {file_path} was successfully imported")
        return df
    except FileNotFoundError:
        logging.error(f"El archivo no está en este path: {file_path}")
        print(f"El archivo no está en este path: {file_path}")
        print(f"Busca en otro lugar, por lo pronto no podemos proceder.")

def fill_all_missing_values(data):
    '''Def to fill all missing values
    
    Params:
        data train

    Returns:
        DataFrame with all missing values filled in
    '''
    for col in data.columns:
        if data[col].dtype in ('int64','float64'):
            data[col].fillna(data[col].mean(), inplace=True)
        else:
            data[col].fillna(data[col].mode()[0], inplace=True)



def encode_catagorical_columns(train, test, Level_col):
    '''Def to encode catagorical columns
    
    Params:
        train: train data
        test: test data

    Returns:
        DataFrame with encode catagorical columns
    '''
    encoder = LabelEncoder()
    for col in Level_col:
        train[col] = encoder.fit_transform(train[col])
        test[col]  = encoder.transform(test[col])