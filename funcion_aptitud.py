from utils import lista_sin_ceros, cromosoma_binario_a_individuo
import comidas
from comidas import (
    PORCION_MINIMA_FRUTAS,
    PORCION_MAXIMA_FRUTAS,
    PORCION_MAXIMA_CARNES_BLANCAS,
    PORCION_MINIMA_CARNES_BLANCAS,
    PORCION_MAXIMA_VEGETALES,
    PORCION_MINIMA_VEGETALES,
    PORCION_MAXIMA_CARNES_ROJAS,
    PORCION_MINIMA_CARNES_ROJAS,
    PORCION_MINIMA_LACTEOS,
    PORCION_MAXIMA_LACTEOS,
    PORCION_MAXIMA_HARINAS_Y_CEREALES,
    PORCION_MINIMA_HARINAS_Y_CEREALES
)


def funcion_aptitud(cromosoma, calorias_a_consumir):
    valor_fitness = 0

    # Transformo el cromosoma binario en una lista de genes entendibles (lista de decimales)
    individuo = cromosoma_binario_a_individuo(cromosoma)

    # Verifico que todos los genes existan
    valor_fitness += verificar_existencia_de_genes(individuo)

    # Verifico que los grupos alimenticios tengan los genes correctos
    valor_fitness += verificar_genes_correctos_por_grupo(individuo)

    # Verifico que se cumplan las porciones de cada grupo alimenticio
    valor_fitness += verificar_cumplimiento_de_porciones_de_cada_grupo_alimenticio(individuo)

    # Verifico que no haya comidas repetidas dentro de cada grupo
    valor_fitness += verificar_no_repeticion_de_comidas_por_grupo(individuo)

    # Verifico que se cumpla la cantidad de calorias
    valor_fitness += verificar_cumplimiento_de_calorias(individuo, calorias_a_consumir)

    return valor_fitness,


def verificar_existencia_de_genes(individuo):
    """Verifica que existan todos los genes en nuestro diccionario de genes.

    Si no se cumple, se retorna un valor negativo de
    forma de afectar negativamente a la funcion fitness.

    Parameters
    ----------
    individuo : Individuo
        individuo a evaluar.
    """
    if len(individuo.genes_invalidos) > 0:
        return -100 * len(individuo.genes_invalidos)

    return 0


def verificar_genes_correctos_por_grupo(individuo):
    """Verifica que los genes de cada grupo correspondan a ese grupo.

    Se penaliza por cada gen incorrecto en cada grupo.

    Parameters
    ----------
    individuo : Individuo
        individuo a evaluar.
    """
    score = 0

    for gen in individuo.harinas_y_cereales:
        if gen != 0 and gen not in comidas.harines_y_cereales:
            score += -15

    for gen in individuo.frutas:
        if gen != 0 and gen not in comidas.frutas:
            score += -15

    for gen in individuo.verduras:
        if gen != 0 and gen not in comidas.vegetales:
            score += -15

    for gen in individuo.carnes_blancas_y_legumbres:
        if gen != 0 and gen not in comidas.canres_blancas_y_legumbres:
            score += -15

    for gen in individuo.carnes_rojas:
        if gen != 0 and gen not in comidas.carnes_rojas:
            score += -15

    for gen in individuo.lacteos:
        if gen != 0 and gen not in comidas.lacteos:
            score += -15

    return score


def verificar_cumplimiento_de_porciones_de_cada_grupo_alimenticio(individuo):
    """Verifica que existan todos los genes en nuestro diccionario de genes.

    Se penaliza por cada grupo que no se cumplan las porciones adecuadas.

    Parameters
    ----------
    individuo : Individuo
        individuo a evaluar.
    """
    score = 0

    if not (PORCION_MINIMA_FRUTAS <= len(lista_sin_ceros(individuo.frutas)) <= PORCION_MAXIMA_FRUTAS):
        score += -50

    if not (PORCION_MINIMA_VEGETALES <= len(lista_sin_ceros(individuo.verduras)) <= PORCION_MAXIMA_VEGETALES):
        score += -50

    if not PORCION_MINIMA_CARNES_ROJAS <= len(lista_sin_ceros(individuo.carnes_rojas)) <= PORCION_MAXIMA_CARNES_ROJAS:
        score += -50

    if not (PORCION_MINIMA_CARNES_BLANCAS <= len(lista_sin_ceros(individuo.carnes_blancas_y_legumbres)) <= PORCION_MAXIMA_CARNES_BLANCAS):
        score += -50

    if not (PORCION_MINIMA_HARINAS_Y_CEREALES <= len(lista_sin_ceros(individuo.harinas_y_cereales)) <= PORCION_MAXIMA_HARINAS_Y_CEREALES):
        score += -50

    if not (PORCION_MINIMA_LACTEOS <= len(lista_sin_ceros(individuo.lacteos)) <= PORCION_MAXIMA_LACTEOS):
        score += -50

    return score


def verificar_cumplimiento_de_calorias(individuo, calorias_necesarias):
    """Verifica que se cumpla la cantidad de calorias pedidas en la dieta.

    Se penaliza segun la diferencia entra las calorias actuales de la dieta
    y las deseadas.

    Parameters
    ----------
    individuo : Individuo
        individuo a evaluar.
    calorias_necesarias : int
        calorias que necesita tener la dieta.
    """
    diferencia = abs(calorias_necesarias - individuo.calorias)

    if 0 <= diferencia < 100:
        return -diferencia/2
    elif 100 <= diferencia < 200:
        return -50
    elif 200 <= diferencia < 500:
        return -200
    elif 500 <= diferencia <= 1000:
        return -500
    else:
        return -1000


def verificar_no_repeticion_de_comidas_por_grupo(individuo):
    """Verifica que no se repitan comidas dentro de cada grupo alimenticio.

    Se penaliza por cada alimento repetido por grupo. Recordar que los ceros
    no se contabilizan como repetidos ya que el cero indica "no porcion".

    Parameters
    ----------
    individuo : Individuo
        individuo a evaluar.
    """
    score = 0

    grupos = [
        individuo.lacteos,
        individuo.harinas_y_cereales,
        individuo.verduras,
        individuo.carnes_rojas,
        individuo.carnes_blancas_y_legumbres,
        individuo.frutas
    ]

    for grupo in grupos:
        grupo_sin_ceros = lista_sin_ceros(grupo)
        repetidos = abs(len(grupo_sin_ceros) - len(set(grupo_sin_ceros)))
        if repetidos > 0:
            score += -10 * repetidos

    return score












