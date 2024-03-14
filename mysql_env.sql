CREATE DATABASE IF NOT EXISTS RecipEase;

CREATE USER IF NOT EXISTS 'dev_aysha'@'localhost' IDENTIFIED BY '1+2=Three';
CREATE USER IF NOT EXISTS 'dev_ehab'@'localhost' IDENTIFIED BY '1+2=Three';

GRANT ALL PRIVILEGES ON *.* TO 'dev_aysha'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'dev_ehab'@'localhost';

FLUSH PRIVILEGES;
