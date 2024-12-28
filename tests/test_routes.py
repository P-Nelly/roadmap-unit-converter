import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Unit Converter' in response.data

def test_length_conversion_route(client):
    # Test GET request
    response = client.get('/length')
    assert response.status_code == 200
    assert b'Length Converter' in response.data

    # Test POST request
    data = {
        'value': '100',
        'from_unit': 'meter',
        'to_unit': 'kilometer'
    }
    response = client.post('/length', data=data)
    assert response.status_code == 200
    assert b'0.1' in response.data

def test_weight_conversion_route(client):
    # Test POST request
    data = {
        'value': '1000',
        'from_unit': 'gram',
        'to_unit': 'kilogram'
    }
    response = client.post('/weight', data=data)
    assert response.status_code == 200
    assert b'1.0' in response.data

def test_temperature_conversion_route(client):
    # Test POST request
    data = {
        'value': '0',
        'from_unit': 'celsius',
        'to_unit': 'fahrenheit'
    }
    response = client.post('/temperature', data=data)
    assert response.status_code == 200
    assert b'32' in response.data 