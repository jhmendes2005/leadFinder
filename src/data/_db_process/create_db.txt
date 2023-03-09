""" import connector

#mydb = connector.connect()

#mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE leads_create (id INT AUTO_INCREMENT PRIMARY KEY, id_search INT NOT NULL, name VARCHAR(50) NOT NULL, address VARCHAR(255) NOT NULL, phone VARCHAR(15), website VARCHAR(50), keyword VARCHAR(20) NOT NULL)")

"CREATE TABLE users_ (userid INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(40) NOT NULL, email VARCHAR(50) NOT NULL UNIQUE, password VARCHAR(15) NOT NULL, registertimestamp BIGINT NOT NULL);"

"CREATE TABLE business_ (businessid VARCHAR(16), businessname VARCHAR(40) UNIQUE, businesskey VARCHAR(40), ownerid INT, adminmember INT, membersid INT, registertimestamp BIGINT NOT NULL);"

"CREATE TABLE product_keys (business INT NOT NULL, productkey VARCHAR(32) UNIQUE, registertimestamp BIGINT NOT NULL, validtimestamp BIGINT);"

"CREATE TABLE leads_generated (leadsid INT AUTO_INCREMENT PRIMARY KEY, userid VARCHAR(40) NOT NULL, keywords VARCHAR(60) NOT NULL, createdtimestamp BIGINT);"

"CREATE TABLE lead_generated (leadid INT AUTO_INCREMENT PRIMARY KEY, leadsid INT NOT NULL, keyword VARCHAR(60) NOT NULL, name VARCHAR(50) NOT NULL, address VARCHAR(255) NOT NULL, phone VARCHAR(15), website VARCHAR(50));"


USE cleads_db;
CREATE TABLE users_ (userid INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(40) NOT NULL, email VARCHAR(50) NOT NULL, password VARCHAR(15) NOT NULL, businesskey VARCHAR(40), registertimestamp INT NOT NULL, UNIQUE(username), UNIQUE(email));

CREATE TABLE business_ (businessid INT AUTO_INCREMENT PRIMARY KEY, businessname VARCHAR(40), ownerid INT, registertimestamp INT NOT NULL, FOREIGN KEY (ownerid) REFERENCES users_(userid), UNIQUE(businessname), UNIQUE(ownerid)); """
