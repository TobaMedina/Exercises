SELECT DISTINCT Prestamos.ISBN
FROM Prestamos
WHERE Prestamos.Estado = 'E'
  AND Prestamos.ISBN IN (
    SELECT AutorrLibro.ISBN
    FROM AutorrLibro
    WHERE AutorrLibro.Codigo IN (
      SELECT Autores.CodAut
      FROM Autores
      WHERE Autores.Pais = 'España'
    )
  );
