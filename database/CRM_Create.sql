-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema crmdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema crmdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `crmdb` DEFAULT CHARACTER SET utf8 ;
USE `crmdb` ;

-- -----------------------------------------------------
-- Table `crmdb`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `crmdb`.`Usuario` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(150) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `telefone` VARCHAR(25) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `crmdb`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `crmdb`.`Cliente` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(150) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `telefone` VARCHAR(25) NULL,
  `cep` VARCHAR(30) NOT NULL,
  `rua` VARCHAR(150) NOT NULL,
  `numero` INT NOT NULL,
  `bairro` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `crmdb`.`Registro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `crmdb`.`Registro` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `dt_registro` DATE NOT NULL,
  `observacao` VARCHAR(300) NULL,
  `Usuario_codigo` BIGINT NOT NULL,
  `Cliente_codigo` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Registro_Usuario1_idx` (`Usuario_codigo` ASC),
  INDEX `fk_Registro_Cliente1_idx` (`Cliente_codigo` ASC),
  CONSTRAINT `fk_Registro_Usuario1`
    FOREIGN KEY (`Usuario_codigo`)
    REFERENCES `crmdb`.`Usuario` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Registro_Cliente1`
    FOREIGN KEY (`Cliente_codigo`)
    REFERENCES `crmdb`.`Cliente` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `crmdb`.`Produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `crmdb`.`Produto` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(150) NOT NULL,
  `fabricante` VARCHAR(150) NOT NULL,
  `qt_estoque` INT NOT NULL,
  `preco` INT(11) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `crmdb`.`Registro_Produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `crmdb`.`Registro_Produto` (
  `Registro_id` BIGINT NOT NULL,
  `Produto_id` BIGINT NOT NULL,
  `qtd` INT NOT NULL,
  PRIMARY KEY (`Registro_id`, `Produto_id`),
  INDEX `fk_Registro_has_Produto_Produto1_idx` (`Produto_id` ASC),
  INDEX `fk_Registro_has_Produto_Registro1_idx` (`Registro_id` ASC),
  CONSTRAINT `fk_Registro_has_Produto_Registro1`
    FOREIGN KEY (`Registro_id`)
    REFERENCES `crmdb`.`Registro` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Registro_has_Produto_Produto1`
    FOREIGN KEY (`Produto_id`)
    REFERENCES `crmdb`.`Produto` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
