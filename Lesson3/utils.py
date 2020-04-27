import csv
from faker import Faker
import requests


def get_file_content(path: str) -> str:
    file = open(path, "r")
    content = file.read()
    content = content.replace('\n', '<br/>')
    file.close()
    return content


def generate_users(quantity: int) -> str:
    fake = Faker(['en_US', 'ru_RU', 'uk_UA'])
    users = ''
    for _ in range(quantity):
        users = users + '<b>' + fake.first_name() + '</b> ' + fake.ascii_company_email() + '<br/>'
    return users


def get_csv_row_average(path: str, column: int) -> float:
    file = open(path, "r")
    # Skip header
    file.readline()
    row_count = 0
    total = 0.0
    for row in csv.reader(file):
        row_count += 1
        total += float(row[column])
    average = total / row_count
    file.close()
    return average


def get_json_value(url: str, key: str) -> str:
    req = requests.get(url)
    return req.json()[key]
