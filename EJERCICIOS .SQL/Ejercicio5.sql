SELECT CodSocio, Prestamos.Estado, Socios.Estado 
FROM Prestamos
JOIN Socios
ON Socios.CodSocio = Prestamos.Socio
WHERE Socios.Estado = 'Inhabilitado' AND Prestamos.Estado != 'E'

