show databases;
use sql_store;
show tables;
describe customers;
describe jwang1568class;
DROP tables IF EXISTS `JWang1568Class`;
CREATE TABLE JWang1568Class (
	name VARCHAR(50), 
	age smallint UNSIGNED, 
    personID int NOT NULL AUTO_INCREMENT PRIMARY KEY);
show tables;
select * from JWang1568Class;
INSERT INTO JWang1568Class (name, age, PersonID) VALUES ("Felicia", 28, 1002);
INSERT INTO JWang1568Class (name, age) VALUES ("Kenny", 26);
select * from JWang1568Class;

 






