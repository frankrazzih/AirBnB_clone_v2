-- creating new database and user
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost' WITH GRANT OPTION;

-- creating new database
CREATE DATABASE IF NOT EXISTS performance_schema;
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';