
 
DROP TABLE IF EXISTS patient;



CREATE TABLE patient(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   Pname TEXT  NOT NULL,
   Age TEXT NOT NULL,
   Gender TEXT NOT NULL,
   DateOfAdm TIMESTAMP NOT NULL default current_timestamp  
);



