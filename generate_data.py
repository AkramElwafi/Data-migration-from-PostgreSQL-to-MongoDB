import csv
from faker import Faker
import random

CSV_FILE = r'data-migration/data_csv/customers_data.csv'

def generate_data_to_csv(num_records, csv_file):
    fake = Faker()
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'email', 'address', 'phone', 'age'])
        for _ in range(num_records):
            name = fake.name()
            email = fake.email()
            address = fake.address().replace('\n', ', ')
            phone = fake.phone_number()[:50]  
            age = random.randint(18, 80)
            writer.writerow([name, email, address, phone, age])

if __name__ == '__main__':
    generate_data_to_csv(2000, CSV_FILE)  
    print(f'Data has been generated and saved to {CSV_FILE}')
