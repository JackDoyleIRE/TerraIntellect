import psycopg2
import random
from datetime import date, timedelta
from faker import Faker

fake = Faker()

# Prompt user for database connection details
dbname = input("Enter your database name: ")
user = input("Enter your database user: ")
password = input("Enter your database password: ")

# Database connection
conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Generate example data
num_clients = 1000
num_projects = 2000
num_partners = 100
num_sales = 1500
num_finance = 3000
num_logistics = 2500

# Insert clients
for _ in range(num_clients):
    cur.execute(
        "INSERT INTO clients (client_name, contact_name, contact_email, contact_phone, address, country) VALUES (%s, %s, %s, %s, %s, %s)",
        (fake.company(), fake.name(), fake.email(), fake.phone_number()[:20], fake.address(), fake.country())
    )

# Insert projects
for _ in range(num_projects):
    start_date = fake.date_between(start_date='-2y', end_date=date.today())
    end_date = start_date + timedelta(days=random.randint(30, 365))
    status = random.choice(['ongoing', 'completed', 'cancelled'])

    cur.execute(
        "INSERT INTO projects (client_id, project_name, project_description, start_date, end_date, status) VALUES (%s, %s, %s, %s, %s, %s)",
        (random.randint(1, num_clients), fake.bs()[:20], fake.text(max_nb_chars=200), start_date, end_date, status)
    )

# Insert partners
for _ in range(num_partners):
    cur.execute(
        "INSERT INTO partners (partner_name, contact_name, contact_email, contact_phone, address, country, partnership_type) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (fake.company(), fake.name(), fake.email(), fake.phone_number()[:20], fake.address(), fake.country(), random.choice(['hardware', 'software', 'data']))
    )

# Insert sales
for _ in range(num_sales):
    cur.execute(
        "INSERT INTO sales (client_id, project_id, sale_amount, sale_date, payment_status) VALUES (%s, %s, %s, %s, %s)",
        (random.randint(1, num_clients), random.randint(1, num_projects), round(random.uniform(500, 20000), 2), fake.date_between(start_date='-2y', end_date=date.today()), random.choice(['paid', 'pending']))
    )

# Insert finance
for _ in range(num_finance):
    cur.execute(
        "INSERT INTO finance (transaction_type, amount, transaction_date, transaction_category, transaction_description, related_id) VALUES (%s, %s, %s, %s, %s, %s)",
        (random.choice(['income', 'expense']), round(random.uniform(100, 20000), 2), fake.date_between(start_date='-2y', end_date=date.today()), random.choice(['sales', 'partnership', 'operational']), fake.text(max_nb_chars=100), random.randint(1, num_sales))
    )

# Insert logistics
for _ in range(num_logistics):
    data_collection_start = fake.date_between(start_date='-2y', end_date=date.today())
    data_collection_end = data_collection
