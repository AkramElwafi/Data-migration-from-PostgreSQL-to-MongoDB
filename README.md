# Data-migration-from-PostgreSQL-to-MongoDB


# Project Overview
In this project, we will create a dataset using the Faker library in Python to generate customer information such as name, address, email, phone number, etc.

# Steps:

Data Generation: Using the Faker library, we will generate synthetic customer data and store it in a CSV file.

Relational Database (PostgreSQL): Insert the generated data into a PostgreSQL database, which is widely used for managing relational databases.

Migration to NoSQL (MongoDB): Finally, we will migrate the data from PostgreSQL to MongoDB, a NoSQL database, to illustrate how structured relational data can be converted and stored in a NoSQL format.

# Why Migrate from Relational (SQL) to NoSQL?
As businesses grow and data scales, organizations often need to move from traditional relational databases (like PostgreSQL) to NoSQL databases (like MongoDB). Below are some of the reasons for this migration:

# Flexibility & Scalability:
Relational databases are schema-based, meaning the structure of the data is predefined and enforced. If you need to change your schema (add or remove columns), it can be cumbersome.
NoSQL databases like MongoDB, on the other hand, are schema-less and can store diverse types of data, allowing for more flexibility as your data requirements evolve.
MongoDB is designed to handle large, unstructured data sets, and it can horizontally scale across multiple servers, making it ideal for applications with high data volume.
# Performance Optimization:
For applications where high read/write throughput is essential (e.g., web applications, real-time analytics), NoSQL databases often outperform relational databases due to their ability to efficiently distribute data across multiple nodes.
MongoDB’s document-based structure allows for faster access times for large datasets, particularly when querying non-relational data.


