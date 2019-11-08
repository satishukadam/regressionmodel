import os
import pandas as pd
from configs import config
import joblib


def predict_model(model_name, data_file_name):
    """This function predicts house prices based on input data"""
    model_path = os.path.join(config.TRAINED_MODEL_DIR, model_name)
    data_file_path = os.path.join(os.path.join(config.DATA_DIR, data_file_name))
    pipe = joblib.load(model_path)
    data = pd.read_csv(data_file_path)
    prediction = pipe.predict(data)
    return prediction


print(predict_model('model1.pkl', 'predict_house_price.csv'))
