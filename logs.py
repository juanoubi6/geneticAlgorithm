import sys
import codecs
import locale
import utils
import comidas
from comidas import (
    diccionario_comida_gen
)
from matplotlib import pyplot as plt

sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

def crear_logs(mejores_n_individuos_de_entre_todas_las_generaciones, poblacion_final, logbook):
    top_individuos_corrida = utils.lista_cromosomas_a_lista_individuos(mejores_n_individuos_de_entre_todas_las_generaciones.items)
    poblacion_final = utils.lista_cromosomas_a_lista_individuos(poblacion_final)

    print('----------- Mejor individuo de la poblacion final -----------')
    mejor_individuo_de_la_poblacion_final = max(poblacion_final, key=lambda x: x.fitness)
    log_individuo(mejor_individuo_de_la_poblacion_final)
    print('\n')

    print('----------- Mejor individuo de toda la corrida -----------')
    mejor_individuo_de_la_corrida = max(top_individuos_corrida, key=lambda x: x.fitness)
    log_individuo(mejor_individuo_de_la_corrida)
    print('\n')

    # Generar grafico de evolucion del valor fitness de los mejores individuos por generacion
    plt.title('Evolucion del valor fitness de los mejores individuos por generacion')
    plt.ylabel('Valor Fitness')
    plt.xlabel('Generacion')

    eje_y_fitness = []
    eje_x_generacion = []
    generacion = 0
    for log in logbook:
        x = log['gen']
        y = log['max']
        eje_y_fitness.append(y)
        eje_x_generacion.append(x)
        plt.scatter(x, y, s=10)
        generacion += 1

    plt.plot(eje_x_generacion, eje_y_fitness)
    plt.savefig("evolucion_fitness_por_generacion.png")
    plt.clf()

    # Generar grafico de evolucion del promedio del valor fitness de la poblacion por generacion
    plt.title('Evolucion del promedio del valor fitness de la poblacion por generacion')
    plt.ylabel('Valor Fitness promedio')
    plt.xlabel('Generacion')

    eje_y_fitness = []
    eje_x_generacion = []
    generacion = 0
    for log in logbook:
        x = log['gen']
        y = log['avg']
        eje_y_fitness.append(y)
        eje_x_generacion.append(x)
        plt.scatter(x, y, s=10)
        generacion += 1

    plt.plot(eje_x_generacion, eje_y_fitness)
    plt.savefig("evolucion_promedio_fitness_por_generacion.png")


def log_individuo(individuo):
    print("Cromosoma:\t" + str(individuo.genes))
    print("Fitness:\t" + str(individuo.fitness))
    print("Calorias:\t" + str(individuo.calorias))
    print("Lacteos:\t" + u", ".join((map(nombre_comida, individuo.lacteos))))
    print("Harinas:\t" + u", ".join((map(nombre_comida, individuo.harinas_y_cereales))))
    print("Verduras:\t" + u", ".join((map(nombre_comida, individuo.verduras))))
    print("Carnes blancas:\t" + u", ".join((map(nombre_comida, individuo.carnes_blancas_y_legumbres))))
    print("Carnes rojas:\t" + u", ".join((map(nombre_comida, individuo.carnes_rojas))))
    print("Frutas:\t\t" + u", ".join((map(nombre_comida, individuo.frutas))))

def nombre_comida(id_comida):
    if diccionario_comida_gen.has_key(id_comida):
        return diccionario_comida_gen[id_comida]
    else:
        return "N/A"