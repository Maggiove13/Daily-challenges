
----Challenge 20 --- THE HUDDLE -JULIO
--Actualizar registros:
-- Escribe una consulta SQL para actualizar el nombre de un usuario específico en la tabla Usuarios.

UPDATE Users
SET 
	Name = 'Penguin'
    WHERE Users.Name = 'Juan'

--Verificar cambios
SELECT * FROM Users
