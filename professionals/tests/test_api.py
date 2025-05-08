import pytest
from rest_framework.test import APIClient
from faker import Faker

@pytest.mark.django_db()
def test_register_professional_return_201_created():
    client = APIClient()
    faker = Faker()
    
    name = faker.name()
    profession = faker.job()
    address = faker.address()
    contact = faker.numerify('##########')

    payload = {
        'name' : name,
        'profession' : profession,
        'address' : address,
        'contact' : contact,
    }
    
    response = client.post('/api/professionals/register_professional/', payload, format='json')
    
    assert response.status_code == 201
    assert response.data['name'] == payload['name']
    