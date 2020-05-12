# Simple-API-using-Flask
A simple API to create user, update, modify and retrieve user details from a database


To test this API create a database as 'test' (I tested using MariaDB) and create Two Tables user and alternate_email

# Table user
create table user(
id integer PRIMARY KEY AUTO_INCREMENT,
username char(20) NOT NULL,
first_name char(20),
last_name char(20),
password char(20) NOT NULL,
email char(50) UNIQUE
);

# Table alternate_email
create table alternate_email(
id integer NOT NULL,
alter_email char(50),
CONSTRAINT `fk_id` FOREIGN KEY (id) REFERENCES user(id)
);


To create a user throw in a POST request at
http://127.0.0.1/add
with values in body using tags username, first_name, last_name, password, email

To get details of a user throw a GET request at
http://127.0.0.1/user/<int:key>
use id number to get details of the user

To modify a user throw in a POST request at
http://127.0.0.1/modify/user/<int:key>
with values in body using tags username, first_name, last_name, password, email


To update a user throw in a POST request at
http://127.0.0.1/update/user/<int:key>
with values in body using tags username, first_name, last_name, password, email
leave the values blank if don't want to change

To add alternative email throw in a POST request at
http://127.0.0.1/email/add/<int:key>
with values in body using tags email
