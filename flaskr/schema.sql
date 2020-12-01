
 
DROP TABLE IF EXISTS patient;



CREATE TABLE patient(
   pid INTEGER PRIMARY KEY AUTOINCREMENT,
   Pname TEXT  NOT NULL,
   Age TEXT NOT NULL,
   Gender TEXT NOT NULL,
   DateOfAdm TIMESTAMP NOT NULL default current_timestamp,
   BedNo INTEGER NOT NULL,
   diagnosis TEXT NOT NULL,
   docname TEXT NOT NULL,
   surgery TEXT NOT NULL 
);



