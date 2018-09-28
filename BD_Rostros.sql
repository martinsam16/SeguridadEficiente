SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema PROYECTO
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `PROYECTO` ;

-- -----------------------------------------------------
-- Schema PROYECTO
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `PROYECTO` DEFAULT CHARACTER SET utf8 ;
USE `PROYECTO` ;

-- -----------------------------------------------------
-- Table `PROYECTO`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO`.`user` (
  `username` VARCHAR(16) NOT NULL,  
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(32) NOT NULL);


-- -----------------------------------------------------
-- Table `PROYECTO`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PROYECTO`.`Usuario` (
  `idUsuario` INT NOT NULL, /*codigo de usuario*/
  `NomUser` VARCHAR(45) NOT NULL, /*nombre del usuario que es gravado o tomado foto*/
  `ApellUser` VARCHAR(45) NOT  NULL,/*Apellido del usuario que es gravado o tomado foto*/
  `DNIUser` VARCHAR(8) NOT NULL,/* DNI  del usuario que es gravado o tomado foto*/
  `FechNacUSer` VARCHAR(45) NULL,/* Fecha de nacimiento del usuario del usuario que es gravado o tomado foto*/
  `DirecUser` VARCHAR(45) NULL,/*monbre del usuario que es gravado o tomado foto*/
  `NroCellUser` VARCHAR(9) NULL,/* Celular  del usuario que es gravado o tomado foto*/
  `GenrUser` VARCHAR(1) NOT NULL,/* Genero  del usuario que es gravado o tomado foto*/
  `FotoUser` VARCHAR(45) NULL,/* foto del usuario */
  `PuntoFacialUser` VARCHAR(45) NULL, /*los punto facial */
  constraint idusuario_PK PRIMARY KEY (`idUsuario`)) 
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
