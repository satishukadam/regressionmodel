import os

# Get the root directory of the project 'D:\Study\DataScience\ModelDeployment\machinelearning'
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Get the configuration file path
CONFIG_PATH = os.path.abspath(__file__)


# Get the data folder path
DATA_DIR = os.path.join(ROOT_DIR, 'data')


# Raw File path
DATA_FILE = os.path.join(os.path.join(DATA_DIR, 'house_price.csv'))


# Trained model path
TRAINED_MODEL_DIR = os.path.join(ROOT_DIR, 'models')


# Numerical Features
NUMERICAL_FEATURES = ['id', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
'waterfront', 'view', 'condition', 'grade', 'sqft_above', 'sqft_basement',
'yr_built', 'yr_renovated', 'zipcode', 'lat', 'long',
'sqft_living15', 'sqft_lot15']

# Feature Variables
FEATURE_VARIABLE = ['id', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
'waterfront', 'view', 'condition', 'grade', 'sqft_above', 'sqft_basement',
'yr_built', 'yr_renovated', 'zipcode', 'lat', 'long',
'sqft_living15', 'sqft_lot15']

# target Variable
TARGET_VARIABLE = ['price']

