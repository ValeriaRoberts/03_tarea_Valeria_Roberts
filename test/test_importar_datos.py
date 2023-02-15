# test_importar_datos.py

import pytest
import pandas as pd
import logging
"""
Función que queremos importar
"""
def import_data(pth):
    df = pd.read_csv(pth)
    return df

"""
Fixture - La función test_importar_datos() va a utilizar el retorno del path()
como un argumento.
"""
@pytest.fixture(scope="module")
def path():
    return "../data/raw/test.csv"


"""
Test method
"""
def test_importar_datos(path):
    # Cargar datos.
    try:
        df = import_data(path)

    except FileNotFoundError as err:
        logging.error("File not found")
        raise err

    # Verificar que no venga vacio.
    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0

    except AssertionError as err:
        logging.error(
            "Testing importar_datos: El archivo no trae columnas o filas")
        raise err
    return df