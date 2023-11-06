import psycopg2
import random
from datetime import date, timedelta
from faker import Faker

fake = Faker()

def insert_data(func, table_name, num_entries):
    try:
        for _ in range(num_entries):
            cur.execute(*func())
        conn.commit()
        print(f"Successfully inserted {num_entries} rows into {table_name}")
    except Exception as e:
        print(f"Error inserting data into {table_name}: {e}")

# Database connection
def connect_to_db():
    dbname = input("Enter your database name: ")
    user = input("Enter your database user: ")
    password = input("Enter your database password: ")

    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host="localhost",
            port="5432"
        )
        print("Successfully connected to the database")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

conn = connect_to_db()
if conn:
    cur = conn.cursor()

    # Generate example data
    num_clients = 1000
    num_projects = 2000
    num_partners = 100
    num_sales = 1500
    num_finance = 3000
    num_logistics = 2500

    # Insert clients
    insert_data(lambda: (
        "INSERT INTO clients (client_name, contact_name, contact_email, contact_phone, address, country) VALUES (%s, %s, %s, %s, %s, %s)",
        (fake.company(), fake.name(), fake.email(), fake.phone_number()[:20], fake.address(), fake.country())
    ), "clients", num_clients)

    # Insert projects
    insert_data(lambda: (
        "INSERT INTO projects (client_id, project_name, project_description, start_date, end_date, status) VALUES (%s, %s, %s, %s, %s, %s)",
        (random.randint(1, num_clients), fake.bs()[:20], fake.text(max_nb_chars=200), fake.date_between(start_date='-2y', end_date=date.today()), fake.date_between(start_date='-2y', end_date=date.today()) + timedelta(days=random.randint(30, 365)), random.choice(['ongoing', 'completed', 'cancelled']))
    ), "projects", num_projects)

    # Insert partners
    insert_data(lambda: (
        "INSERT INTO partners (partner_name, contact_name, contact_email, contact_phone, address, country, partnership_type) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (fake.company(), fake.name(), fake.email(), fake.phone_number()[:20], fake.address(), fake.country(), random.choice(['hardware', 'software', 'data']))
    ), "partners", num_partners)

    # Insert sales
    insert_data(lambda: (
        "INSERT INTO sales (client_id, project_id, sale_amount, sale_date, payment_status) VALUES (%s, %s, %s, %s, %s)",
        (random.randint(1, num_clients), random.randint(1, num_projects), round(random.uniform(500, 20000), 2), fake.date_between(start_date='-2y', end_date=date.today()), random.choice(['paid', 'pending']))
    ), "sales", num_sales)

  # Insert finance
    insert_data(lambda: (
        "INSERT INTO finance (transaction_type, amount, transaction_date, transaction_category, transaction_description, related_id) VALUES (%s, %s, %s, %s, %s, %s)",
        (random.choice(['income', 'expense']), round(random.uniform(100, 20000), 2), fake.date_between(start_date='-2y', end_date=date.today()), random.choice(['sales', 'partnership', 'operational']), fake.text(max_nb_chars=100), random.randint(1, num_sales))
    ), "finance", num_finance)

    # Insert logistics
    insert_data(lambda: (
        "INSERT INTO logistics (project_id, drone_id, sensor_id, location, data_collection_start, data_collection_end, data_size, transport_method) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (random.randint(1, num_projects), random.randint(1, 100), random.randint(1, 100), fake.address(), fake.date_time_between(start_date='-2y', end_date='now'), fake.date_time_between(start_date='-2y', end_date='now') + timedelta(hours=random.randint(1, 48)), round(random.uniform(0.1, 10), 2), random.choice(['physical', 'cloud']))
    ), "logistics", num_logistics)

    # Close the connection
    cur.close()
    conn.close()