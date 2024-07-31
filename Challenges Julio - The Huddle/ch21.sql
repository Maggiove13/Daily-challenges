
----Challenge 21 --- THE HUDDLE -JULIO

--Eliminar registros: Escribe una consulta SQL para eliminar un usuario específico de la tabla Usuarios.

DELETE FROM Users
WHERE Users.Name = 'Penguin'

--Verificar cambios
SELECT * FROM Users