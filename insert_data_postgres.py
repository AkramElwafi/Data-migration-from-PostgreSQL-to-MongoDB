import psycopg2
import csv
conn = psycopg2.connect(
    host="localhost",
    database="your-db",
    user="your-username",
    password="your-password"
)
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS customers;')
conn.commit()

cursor.execute('''
    CREATE TABLE customers (
        customer_id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        address VARCHAR(255),
        phone VARCHAR(50),  -- Ensure length is large enough
        age INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
''')
conn.commit()
def insert_data_from_csv(csv_file):
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            cursor.execute('''
                INSERT INTO customers (name, email, address, phone, age) 
                VALUES (%s, %s, %s, %s, %s);
            ''', row)
    conn.commit()

CSV_FILE = r'data-migration/data_csv/customers_data.csv'

if __name__ == '__main__':
    insert_data_from_csv(CSV_FILE)
    print(f'Data from {CSV_FILE} has been inserted into the PostgreSQL database')

cursor.close()
conn.close()