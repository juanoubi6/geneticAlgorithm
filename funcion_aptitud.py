import utils
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

    # Transformo el cromosoma binario en una lista de genes entendibles
    individuo = utils.cromosoma_binario_a_individuo(cromosoma)

    # Verifico que todos los genes existan
    valor_fitness += verificar_existencia_de_genes(individuo)

    # Verifico que los grupos tengan los genes correctos
    valor_fitness += verificar_genes_correctos_por_grupo(individuo)

    # Verifico que se cumplan las porciones de cada grupo alimenticio
    valor_fitness += verificar_cumplimiento_de_porciones_de_cada_grupo_alimenticio(individuo)

    # Verifico que no haya comidas repetidas dentro de cada grupo
    valor_fitness += verificar_no_repeticion_de_comidas_por_grupo(individuo)

    # Verifico que se cumpla la cantidad de calorias
    valor_fitness += verificar_cumplimiento_de_calorias(individuo, calorias_a_consumir)

    return valor_fitness,


# Verifica que existan todos los genes en nuestro diccionario de genes. Si no se cumple, se retorna un valor
# negativo de forma de afectar negativamente a la funcion fitness.
def verificar_existencia_de_genes(individuo):
    if len(individuo.genes_invalidos) > 0:
        return -100 * len(individuo.genes_invalidos)

    return 0

def verificar_genes_correctos_por_grupo(individuo):
    score = 0

    for gen in individuo.harinas_y_cereales:
        if gen != 0 and gen not in comidas.bread_and_cereals:
            score += -15

    for gen in individuo.frutas:
        if gen != 0 and gen not in comidas.fruts:
            score += -15

    for gen in individuo.verduras:
        if gen != 0 and gen not in comidas.vegetables:
            score += -15

    for gen in individuo.carnes_blancas_y_legumbres:
        if gen != 0 and gen not in comidas.white_meat_and_legumes:
            score += -15

    for gen in individuo.carnes_rojas:
        if gen != 0 and gen not in comidas.red_meat:
            score += -15

    for gen in individuo.lacteos:
        if gen != 0 and gen not in comidas.dairy_products:
            score += -15

    return score


# Verifica que existan todos los genes en nuestro diccionario de genes. Si no se cumple, se retorna un valor
# negativo de forma de afectar negativamente a la funcion fitness.
def verificar_cumplimiento_de_porciones_de_cada_grupo_alimenticio(individuo):
    score = 0

    # Verifico que cada grupo tenga la cantidad adecuada de porciones. Caso contrario, penalizo.
    if not (PORCION_MINIMA_FRUTAS <= len(list(filter(lambda num: num != 0, individuo.frutas))) <= PORCION_MAXIMA_FRUTAS):
        score += -50

    if not (PORCION_MINIMA_VEGETALES <= len(list(filter(lambda num: num != 0, individuo.verduras))) <= PORCION_MAXIMA_VEGETALES):
        score += -50

    if not PORCION_MINIMA_CARNES_ROJAS <= len(list(filter(lambda num: num != 0, individuo.carnes_rojas))) <= PORCION_MAXIMA_CARNES_ROJAS:
        score += -50

    if not (PORCION_MINIMA_CARNES_BLANCAS <= len(list(filter(lambda num: num != 0, individuo.carnes_blancas_y_legumbres))) <= PORCION_MAXIMA_CARNES_BLANCAS):
        score += -50

    if not (PORCION_MINIMA_HARINAS_Y_CEREALES <= len(list(filter(lambda num: num != 0, individuo.harinas_y_cereales))) <= PORCION_MAXIMA_HARINAS_Y_CEREALES):
        score += -50

    if not (PORCION_MINIMA_LACTEOS <= len(list(filter(lambda num: num != 0, individuo.lacteos))) <= PORCION_MAXIMA_LACTEOS):
        score += -50

    return score


def verificar_cumplimiento_de_calorias(individuo, calorias_necesarias):
    #return -abs(calorias_necesarias - individuo.calorias)
    diferencia = abs(calorias_necesarias - individuo.calorias)

    if 0 <= diferencia < 100:
        return -0
    elif 100 <= diferencia < 200:
        return -50
    elif 200 <= diferencia < 500:
        return -200
    elif 500 <= diferencia <= 1000:
        return -500
    else:
        return -1000


def verificar_no_repeticion_de_comidas_por_grupo(individuo):
    score = 0

    grupos = [
        individuo.lacteos,
        individuo.harinas_y_cereales,
        individuo.verduras,
        individuo.carnes_rojas,
        individuo.carnes_blancas_y_legumbres,
        individuo.frutas
    ]

    # Verifico que cada grupo tenga la cantidad adecuada de porciones. Caso contrario, penalizo.
    for grupo in grupos:
        repetidos = abs(len(grupo) - len(set(grupo)))
        if repetidos > 0:
            score += -10 * repetidos

    return score












