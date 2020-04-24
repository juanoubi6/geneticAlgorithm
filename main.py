import random
import utils
import numpy
import comidas
from funcion_aptitud import funcion_aptitud
from deap import creator, base, tools, algorithms


def algortimo_genetico(calorias):

    # Se indica como se va a evaluar los pesos de la funcion (en este caso, a mayor valor mejor es la funcion)
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    # Se crea la herramienta que va a registrar los individuos y las estrategias de seleccion, cruzamiento y mutacion
    toolbox = base.Toolbox()

    # Se indica como se va a crear cada individuo de la poblacion. En este caso, cada individuo esta formado por
    # n digitos binarios, siendo N el valor de comidas.LONGITUD_CROMOSOMA
    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=comidas.LONGITUD_CROMOSOMA)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Se indica cual sera la funcion aptitud a evaluar para cada individuo
    toolbox.register("evaluate", funcion_aptitud, calorias_a_consumir=calorias)

    # Se indica cuales seran las estrategias de seleccion (select), cruzamiento (mate) y mutacion (mutate)
    toolbox.register("select", tools.selTournament, tournsize=10)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)

    # Se indica la cantidad de generaciones
    NGEN = 50

    # Se indica el numero de individuos que tendra la poblacion inicial, que sera constante durante toda la corrida.
    population = toolbox.population(n=5000)

    # El HallOfFame se utiliza para almacenar el individuo mas fit de cada generacion
    fame = tools.HallOfFame(NGEN)

    # Se crean estadisticas para analizar cada ciclo. En este caso, las estadisticas registradas son
    #   -max = devuelve el valor de la funcion fitness del mejor individuo del ciclo
    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("max", numpy.max)

    # Es el metodo que realiza la simulacion en si. Los parametros mas importantes son:
    #   -population --> Poblacion inicial
    #   -toolbox    --> Contiene la informacion de los metodos de seleccion, mutacion y cruzamiento que se va a usar
    #   -cxpb       --> Probabilidad de cruzamiento
    #   -mutpb      --> Probabilidad de mutacion
    #   -ngen       --> Numero de generaciones
    #   -stats      --> Estadisticas que cada ciclo debe registrar
    #   -halloffame --> Objeto que almacena el mejor individuo de cada ciclo
    algorithms.eaSimple(
        population,
        toolbox,
        cxpb=1,
        mutpb=0.2,
        ngen=NGEN,
        stats=stats,
        halloffame=fame
    )

    #TODO: dejar esto mas lindo para tener unos logs no tan cabeza
    top = utils.mostrar_mejores_individuos(fame.items)
    best = max(top, key=lambda x: x.fitness)
    print(best.fitness)
    print("Calorias " + str(best.calorias))
    print("Lacteos:" + str(best.lacteos))
    print("Harinas:" + str(best.harinas_y_cereales))
    print("Verduras:" + str(best.verduras))
    print("Carnes blancas:" + str(best.carnes_blancas_y_legumbres))
    print("Carnes rojas:" + str(best.carnes_rojas))
    print("Frutas:" + str(best.frutas))


if __name__ == "__main__":
    algortimo_genetico(2000)

