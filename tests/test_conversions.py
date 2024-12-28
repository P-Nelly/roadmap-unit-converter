import pytest
from app import convert_length, convert_weight, convert_temperature

def test_length_conversion():
    # Test meter to kilometer
    assert convert_length(1000, 'meter', 'kilometer') == 1
    # Test kilometer to mile
    assert round(convert_length(1, 'kilometer', 'mile'), 4) == 0.6214
    # Test inch to centimeter
    assert round(convert_length(1, 'inch', 'centimeter'), 2) == 2.54

def test_weight_conversion():
    # Test kilogram to pound
    assert round(convert_weight(1, 'kilogram', 'pound'), 2) == 2.20
    # Test pound to gram
    assert round(convert_weight(1, 'pound', 'gram'), 2) == 453.59
    # Test ounce to gram
    assert round(convert_weight(1, 'ounce', 'gram'), 2) == 28.35

def test_temperature_conversion():
    # Test Celsius to Fahrenheit
    assert convert_temperature(0, 'celsius', 'fahrenheit') == 32
    assert convert_temperature(100, 'celsius', 'fahrenheit') == 212
    # Test Fahrenheit to Celsius
    assert convert_temperature(32, 'fahrenheit', 'celsius') == 0
    # Test Kelvin to Celsius
    assert convert_temperature(273.15, 'kelvin', 'celsius') == 0

def test_invalid_input():
    with pytest.raises(ValueError):
        convert_length('invalid', 'meter', 'kilometer')
    with pytest.raises(ValueError):
        convert_weight('invalid', 'kilogram', 'pound')
    with pytest.raises(ValueError):
        convert_temperature('invalid', 'celsius', 'fahrenheit') 