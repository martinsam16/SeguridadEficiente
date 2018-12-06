CREATE DATABASE Seguridad_Eficiente char set utf8;
USE Seguridad_Eficiente;

CREATE TABLE USUARIO (
  ID INT  NOT NULL, /*codigo de usuarcio*/
  NomUser VARCHAR(45) NOT NULL, /*nombre del usuario que es gravado o tomado foto*/
  ApellUser VARCHAR(45) NOT  NULL,/*Apellido del usuario que es gravado o tomado foto*/
  DNIUser VARCHAR(8) NOT NULL,/* DNI  del usuario que es gravado o tomado foto*/
  FechNacUSer DATE NULL,/* Fecha de nacimiento del usuario del usuario que es gravado o tomado foto*/
  DirecUser VARCHAR(45) NULL,/*monbre del usuario que es gravado o tomado foto*/
  NroCellUser VARCHAR(9) NULL,/* Celular  del usuario que es gravado o tomado foto*/
  GenrUser boolean NOT NULL,/* Genero  del usuario que es gravado o tomado foto*/
  FotoUser VARCHAR(45) not NULL,/* foto del usuario */
  constraint ID_PK PRIMARY KEY (ID));
