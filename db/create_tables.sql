CREATE TABLE clients (
  client_id SERIAL PRIMARY KEY,
  client_name VARCHAR(255),
  contact_name VARCHAR(255),
  contact_email VARCHAR(255),
  contact_phone VARCHAR(20),
  address VARCHAR(255),
  country VARCHAR(100)
);

CREATE TABLE projects (
  project_id SERIAL PRIMARY KEY,
  client_id INTEGER REFERENCES clients(client_id),
  project_name VARCHAR(255),
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  status VARCHAR(50)
);

CREATE TABLE partners (
  partner_id SERIAL PRIMARY KEY,
  partner_name VARCHAR(255),
  contact_name VARCHAR(255),
  contact_email VARCHAR(255),
  contact_phone VARCHAR(20),
  address VARCHAR(255),
  country VARCHAR(100),
  partnership_type VARCHAR(100)
);

CREATE TABLE sales (
  sale_id SERIAL PRIMARY KEY,
  client_id INTEGER REFERENCES clients(client_id),
  project_id INTEGER REFERENCES projects(project_id),
  sale_amount DECIMAL,
  sale_date DATE,
  payment_status VARCHAR(50)
);

CREATE TABLE finance (
  finance_id SERIAL PRIMARY KEY,
  transaction_type VARCHAR(10) CHECK (transaction_type IN ('income', 'expense')),
  amount DECIMAL,
  transaction_date DATE,
  transaction_category VARCHAR(50) CHECK (transaction_category IN ('sales', 'partnership', 'operational')),
  transaction_description TEXT,
  related_id INTEGER
);

CREATE TABLE logistics (
  logistics_id SERIAL PRIMARY KEY,
  project_id INTEGER REFERENCES projects(project_id),
  drone_id INTEGER,
  sensor_id INTEGER,
  location VARCHAR(255),
  data_collection_start TIMESTAMP,
  data_collection_end TIMESTAMP,
  data_size DECIMAL,
  transport_method VARCHAR(50) CHECK (transport_method IN ('physical', 'cloud'))
);