# En geometría un vector es un segmento de recta orientado que va desde un punto A hasta un punto B. Los vectores en el plano  se  representan mediante  un  par  ordenado de  números  reales  (x,  y)  llamados  componentes.
# Para  representarlos basta con unir el origen de coordenadas con el punto indicado en sus componentes: Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determinarlo basta calcular su producto escalar y verificar si es igual a 0. 
# Ejemplo:A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales

def vectores_ortogonales(vector1, vector2):
    producto_escalar = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    return producto_escalar == 0

vector1 = (2, 3)
vector2 = (-3, 2)
son_ortogonales = vectores_ortogonales(vector1, vector2)
print(son_ortogonales)
