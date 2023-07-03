SELECT Autores.Nombre, Prestamos.Fecha
FROM Autores
JOIN AutorrLibro
ON Autores.CodAut = Autorrlibro.Codigo
JOIN Prestamos ON Autorrlibro.ISBN = Prestamos.ISBN
WHERE MONTH(Prestamos.Fecha) = 3 OR MONTH(Prestamos.Fecha) = 6;
