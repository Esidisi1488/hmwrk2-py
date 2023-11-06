from faker import Faker
import requests

fake = Faker()


def read_requirements():
    f1 = open('requirements.txt')
    result = f1.read()
    return result


def generate_users(quantity: int = 100) -> str:
    result = ''
    for _ in range(quantity):
        result += fake.first_name() + ' ' + fake.ascii_free_email() + '\n'

    return result


def get_astronauts_num():
    r = requests.get('http://api.open-notify.org/astros.json')
    return r.json()["number"]
