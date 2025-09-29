from calificaciones import *

def test_nota_teoria(nota1, nota2):
    print("Probando nota_teoria")
    media = nota_teoria(nota1, nota2)
    print(f"{nota1}, {nota2} ==> {media}")

def test_nota_cuatrimestre(t1, t2, p):
    print("Probando nota_cuatrimestre")
    final = nota_cuatrimestre(t1, t2, p)
    print(f"{t1}, {t2}, {p} ==> {final}")
    
def test_nota_continua(nt, np):
    print("Probando nota_continua")
    continua = nota_continua(nt, np)
    print(f"Notas teoría: {nt}, notas prácica: {np} ==> {continua}")

if __name__ == "__main__":
    # test_nota_teoria(9.1, 7.2)
    # test_nota_teoria(4.0, 6.0)
    # test_nota_teoria(4.0, 3.0)
    # test_nota_teoria(None, 3.0)
    # test_nota_teoria(9.0, None)
    # test_nota_teoria(None, None)

    # test_nota_cuatrimestre(9.1, 7.2, 8.1)
    # test_nota_cuatrimestre(4.0, 6.0, 5.0)
    # test_nota_cuatrimestre(4.0, 3.0, None)
    # test_nota_cuatrimestre(None, 3.0, None)
    # test_nota_cuatrimestre(9.0, None, 4.5)
    # test_nota_cuatrimestre(9.0, None, None)
    # test_nota_cuatrimestre(None, None, None)

    test_nota_continua((9.6, 9.9, 10.0, 9.8), (9.7, 9.5))
    test_nota_continua((4.4, 4.9, 5.1, 4.7), (4.6, 4.8))
    test_nota_continua((9.0, None, 4.0, 3.0), (4.5, None))
    test_nota_continua((9.0, 5.0, 4.0, None), (4.5, None))
