from configs import config
from regression.preparation import load_dataset, get_features


def test_preparation_get_features():
    assert get_features(load_dataset())[0] == config.NUMERICAL_FEATURES, 'test successful'




