CREATE DATABASE pydb;

CREATE TABLE contacts (
    contact_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20),
    mail_address VARCHAR(100),
    job_title VARCHAR(50)
);
