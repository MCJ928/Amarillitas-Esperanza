-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema amarillitas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema amarillitas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `amarillitas` DEFAULT CHARACTER SET utf8 ;
USE `amarillitas` ;

-- -----------------------------------------------------
-- Table `amarillitas`.`companies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `amarillitas`.`companies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL,
  `cuit` VARCHAR(45) NULL,
  `adress` VARCHAR(255) NULL,
  `description` TEXT NULL,
  `phone` VARCHAR(45) NULL,
  `category` VARCHAR(100) NULL,
  `email` VARCHAR(100) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `amarillitas`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `amarillitas`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email_u` VARCHAR(255) NULL,
  `password_u` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `upated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `amarillitas`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `amarillitas`.`products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `description` TEXT NULL,
  `photo_url` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `company_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_products_companies_idx` (`company_id` ASC) VISIBLE,
  CONSTRAINT `fk_products_companies`
    FOREIGN KEY (`company_id`)
    REFERENCES `amarillitas`.`companies` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `amarillitas`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `amarillitas`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `text` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `company_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_companies1_idx` (`company_id` ASC) VISIBLE,
  INDEX `fk_comments_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_companies1`
    FOREIGN KEY (`company_id`)
    REFERENCES `amarillitas`.`companies` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `amarillitas`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `amarillitas`.`stars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `amarillitas`.`stars` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `company_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_stars_companies1_idx` (`company_id` ASC) VISIBLE,
  INDEX `fk_stars_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_stars_companies1`
    FOREIGN KEY (`company_id`)
    REFERENCES `amarillitas`.`companies` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_stars_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `amarillitas`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- -----------------------------------------------------
-- Ariel Avila - 29-04-2024 FIX: Agregamos al script las categoriaS
-- -----------------------------------------------------

INSERT INTO categories (name) VALUES ("Ferretería");
INSERT INTO categories (name) VALUES ("Heladerías");
INSERT INTO categories (name) VALUES ("Indumentaria");
INSERT INTO categories (name) VALUES ("Minimercados");
INSERT INTO categories (name) VALUES ("Zapaterías");
INSERT INTO categories (name) VALUES ("Abogados");
INSERT INTO categories (name) VALUES ("Gasistas");
INSERT INTO categories (name) VALUES ("Mecánicos");
INSERT INTO categories (name) VALUES ("Médicos");
INSERT INTO categories (name) VALUES ("Psicólogos");