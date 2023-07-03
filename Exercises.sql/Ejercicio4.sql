SELECT Socio, COUNT(ISBN) AS num_libros_prestados
FROM Prestamos
GROUP BY socio
HAVING COUNT(ISBN) = (
  SELECT MAX(num_libros_prestados)
  FROM (
    SELECT COUNT(ISBN) AS num_libros_prestados
    FROM Prestamos
    GROUP BY socio
  ) AS subconsulta_interna
)
