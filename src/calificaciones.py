def convierte_none(n):
    if n == None:
        n = 0
    return n


def nota_teoria(nota1, nota2):
    nota1 = convierte_none(nota1)
    nota2 = convierte_none(nota2)
    
    return (nota1 + nota2) / 2

def nota_cuatrimestre(t1, t2, p):
    t1 = convierte_none(t1)
    t2 = convierte_none(t2)
    p = convierte_none(p)
    
    teoria = nota_teoria(t1, t2)
    if (t1 + t2) / 2 >= 4:
        nota_final = (teoria * 0.3) + (p * 0.7)
    else:
        nota_final = 0

    return nota_final

def nota_continua(notas_teoria, notas_practica):
    c1 = nota_cuatrimestre(notas_teoria[0], notas_teoria[1], notas_practica[0])
    c2 = nota_cuatrimestre(notas_teoria[2], notas_teoria[3], notas_practica[1])

    media = (c1 + c2) / 2
    
    if c1 >= 5 and c2 >= 5:
        nota_continua = media
    else:
        nota_continua = min(4, media)

    return nota_continua