import random
import utils
import numpy
import comidas
from funcion_aptitud import funcion_aptitud
from deap import creator, base, tools, algorithms


def main(calorias):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()

    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=comidas.LONGITUD_CROMOSOMA)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", funcion_aptitud, calorias_a_consumir=calorias)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
    toolbox.register("select", tools.selTournament, tournsize=10)

    NGEN = 100
    population = toolbox.population(n=5000)
    fame = tools.HallOfFame(NGEN)

    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("max", numpy.max)
    #stats.register("avg", numpy.average)

    algorithms.eaSimple(
        population,
        toolbox,
        cxpb=1,
        mutpb=0.2,
        ngen=NGEN,
        stats=stats,
        halloffame=fame
    )
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
    main(2800)

