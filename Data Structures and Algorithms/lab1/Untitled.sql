use ycheah;

DROP TABLE IF EXISTS PROTEIN;
CREATE TABLE PROTEIN(
id INT(10)PRIMARY KEY AUTO_INCREMENT,
accessID VARCHAR(6) UNIQUE,
description VARCHAR(255),
sequence VARCHAR(2000)
);