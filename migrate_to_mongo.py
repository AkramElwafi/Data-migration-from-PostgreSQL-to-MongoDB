import psycopg2
from pymongo import MongoClient

pg_conn = psycopg2.connect(
    host="localhost",   
    database="postgres",
    user="postgres",
    password="kraman"
)

pg_cursor = pg_conn.cursor()

mongo_client = MongoClient('your-mongo-client-adress')
mongo_db = mongo_client['your-db-name'] 
mongo_collection = mongo_db['customers']  
pg_cursor.execute('SELECT name, email, address, phone, age, created_at FROM customers')
customers = pg_cursor.fetchall()

for customer in customers:
    customer_doc = {
        "name": customer[0],
        "email": customer[1],
        "address": customer[2],
        "phone": customer[3],
        "age": customer[4],
        "created_at": customer[5]
    }
    mongo_collection.insert_one(customer_doc)

pg_cursor.close()
pg_conn.close()

mongo_client.close()

print("Data migration from PostgreSQL to MongoDB is complete")
