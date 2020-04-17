import comidas
from individuo import Individuo

def cromosoma_binario_a_individuo(cromosoma):
    lista_enteros = []
    numero_de_gen = 0
    gen_binario = ''

    for gen in cromosoma:
        gen_binario += str(gen)
        numero_de_gen += 1

        if numero_de_gen != 0 and numero_de_gen % comidas.BITS_GEN == 0:
            gen_entero = int(gen_binario, 2)
            lista_enteros.append(gen_entero)
            gen_binario = ''

    return Individuo(lista_enteros, cromosoma.fitness)


def mostrar_mejores_individuos(top_individuos):
    individuos_formateados = []

    for individuo in top_individuos:
        individuos_formateados.append(cromosoma_binario_a_individuo(individuo))

    return individuos_formateados


def lista_sin_ceros(lista):
    return list(filter(lambda num: num != 0, lista))
