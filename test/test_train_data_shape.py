# test_train_data_shape.py
from house_prices import train_data_shape

def test_train_data_shape():
    assert train_data_shape == (1460, 36)
