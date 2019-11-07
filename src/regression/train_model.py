from regression.processing import train_pipeline
from regression.preparation import load_dataset
from configs import config
from sklearn.model_selection import train_test_split
import joblib
import os
import logging
from configs.logging_config import get_handler

# # Create logger
logger = logging.getLogger(__name__)
handler = get_handler(logger)
logger.info('trained model')


def train_model():
    """This function trains the model"""
    data = load_dataset(config.DATA_FILE)

    # Split the data into train and testing datasets

    x = data.iloc[:, :-1]
    y = data['price']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    # Fit the pipeline to training dataset

    model = train_pipeline(config.DATA_FILE)

    model.fit(x_train, y_train)

    # Save the model
    model_name = os.path.join(config.TRAINED_MODEL_DIR, 'model1.pkl')

    joblib.dump(train_pipeline, model_name)


if __name__ == '__main__':
    train_model()

