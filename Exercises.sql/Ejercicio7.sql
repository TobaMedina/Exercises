SELECT Libros.Titulo, COUNT(Prestamos.ISBN) AS num_libros_prestados
FROM Prestamos
JOIN Libros
ON Libros.ISBN = Prestamos.ISBN
GROUP BY Libros.Titulo
HAVING COUNT(Prestamos.ISBN) = (
  SELECT MIN(num_libros_prestados)
  FROM (
    SELECT COUNT(ISBN) AS num_libros_prestados
    FROM Prestamos
    GROUP BY ISBN
  ) AS subconsulta_interna
)
