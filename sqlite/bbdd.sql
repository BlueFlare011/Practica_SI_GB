.\sqlite3.exe PRACTICA1.db

-- Creacion de tablas
DROP TABLE RESPONSIBLES;
CREATE TABLE RESPONSIBLES (
	name varchar(25) PRIMARY KEY,
	phone varchar(25),
	rol varchar(50)
);

DROP TABLE DEVICES;
CREATE TABLE DEVICES (
	id varchar(25) PRIMARY KEY,
	ip varchar(20),
	localization varchar(25),
	rtb_responsible varchar(25),
	services numeric,
	insecures numeric,
	vulnerabilities numeric,
	FOREIGN KEY (rtb_responsible) REFERENCES RESPONSIBLES (name)
);

DROP TABLE PORTS_DEVICE;
CREATE TABLE PORTS_DEVICE (
	rtb_device varchar(25),
	port varchar(20),
	FOREIGN KEY (rtb_device) REFERENCES DEVICES (id)
);

-- Viusalizacion de tablas
.schema

-- Borrado de datos de tablas
DELETE FROM RESPONSIBLES;
DELETE FROM PORTS_DEVICE;
DELETE FROM DEVICES;
