import comidas
from individuo import Individuo


def cromosoma_binario_a_individuo(cromosoma):
    """Se transforma el cromosoma (lista de binarios) en
    un objeto del tipo Individuo.

    Parameters
    ----------
    cromosoma : list of int
        lista de numeros binarios que forman el cromosoma.

    Returns
    -------
    Individuo
        True if successful, False otherwise.
    """
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


def lista_cromosomas_a_lista_individuos(top_individuos):
    """Se obtiene una lista de cromosomas y se la transforma
    en una lista de individuos

    Parameters
    ----------
    lista : list of list
        lista de cromosomas.

    Returns
    -------
    list of Individuo
        lista de cromosomas formateados como Individuos.
    """
    individuos_formateados = []

    for individuo in top_individuos:
        individuos_formateados.append(cromosoma_binario_a_individuo(individuo))

    return individuos_formateados


def lista_sin_ceros(lista):
    """Se obtiene la lista de entrada sin ceros

    Parameters
    ----------
    lista : list of int
        lista de numeros.

    Returns
    -------
    list of int
        lista sin ceros.
    """
    return list(filter(lambda num: num != 0, lista))
