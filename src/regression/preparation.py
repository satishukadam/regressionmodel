import pandas as pd
from configs import config


# Function to load dataset csv
def load_dataset(input_file=config.DATA_FILE) -> pd.DataFrame:
    """This function loads the input CSV file into a pandas dataframe"""
    _data = pd.read_csv(input_file)
    return _data


# Function to get numerical and categorical features from a dataframe
def get_features(df):
    """This function gets the numerical and categorical features from the dataframe"""
    num_features = df.select_dtypes(include= ['int64', 'float64']).drop(['price'], axis=1).columns

    cat_features = df.select_dtypes(include=['object']).columns
    return num_features.tolist(), cat_features.tolist()

