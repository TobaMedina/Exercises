SELECT AutorrLibro.ISBN, Autores.Nombre
FROM AutorrLibro
INNER JOIN Autores ON AutorrLibro.Codigo = Autores.CodAut
WHERE AutorrLibro.ISBN = '789-444-419-2'