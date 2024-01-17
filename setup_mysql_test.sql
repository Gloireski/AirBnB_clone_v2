--  A script that prepares a MySQL server for the project.

-- Create a database named hbnb_test_db

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user named hbnb_test (in localhost) with the password hbnb_test_pwd

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to the user hbnb_test on the database hbnb_test_db

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege to the user hbnb_test on the database performance_schema

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges and apply changes

FLUSH PRIVILEGES;

