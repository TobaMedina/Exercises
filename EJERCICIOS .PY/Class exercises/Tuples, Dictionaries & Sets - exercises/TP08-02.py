# Desarrollar un programa que utilice una función que reciba como parámetro una cadena de caracteres conteniendo una dirección de  correo  electrónico  y  devuelva  una  tupla  con  las  distintas  partes  que  componen  dicha  dirección.  Ejemplo: alguien@uade.edu.ar -> (alguien, uade, edu, ar)

def descomponer_direccion_correo(correo):
    partes = correo.split('@')
    usuario = partes[0]
    dominio = partes[1]
    dominio_partes = dominio.split('.')
    extension = dominio_partes[-1]
    dominio_sin_extension = '.'.join(dominio_partes[:-1])
    return (usuario, dominio_sin_extension, extension)

direccion_correo = 'alguien@uade.edu.ar'
partes_direccion = descomponer_direccion_correo(direccion_correo)
print(partes_direccion)
