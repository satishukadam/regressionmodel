from regression.preparation import get_features, load_dataset
from configs import config
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from configs.logging_config import get_handler
import logging

# Create logger
logger = logging.getLogger(__name__)
handler = get_handler(logger)
logger.info('processing done!!!')


def train_pipeline(file=config.DATA_FILE):
    """This function will read the data and process features using a pipeline"""
    # Loading data
    data = load_dataset(file)

    # Get numerical and categorical features
    numerical_features, categorical_features = get_features(data)

    # Create a pipeline for data pre-processing
    numerical_pipe = Pipeline([('num_imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())])
    categorical_pipe = Pipeline([('cat_imputer', SimpleImputer(missing_values='NaN', strategy='most_frequent')),
                                ('ohe', OneHotEncoder(sparse=False))])

    # Merge two pipelines into a single pipeline
    preprocessor = ColumnTransformer([('num_pipe', numerical_pipe, numerical_features),
                                     ('cat_pipe', categorical_pipe, categorical_features)])

    pipeline = Pipeline([('preprocessor', preprocessor), ('linear_model', LinearRegression())])
    return pipeline


