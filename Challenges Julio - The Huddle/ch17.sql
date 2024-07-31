--Challenge 17 --- THE HUDDLE -JULIO
-- Creación de tabla: 
--Escribe una consulta SQL para crear una tabla Usuarios con columnas id y nombre

--Crear una base de datos
CREATE DATABASE NewDB;


--Crear una tabla Users
CREATE TABLE Users (
    id TINYINT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(10)
);