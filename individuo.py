import comidas


class Individuo:

    def __init__(self, lista_genes, fitness=None):
        """Constructor del Individuo.

        Parameters
        ----------
        lista_genes : list of list
            lista de genes del cromosoma. Cada gen ya fue convertido de binario a decimal.
        fitness : int
            indica el valor fitness del individuo.
        """
        self._raw_gens = lista_genes
        self._invalid_gens = []
        self._frutas = []
        self._verduras = []
        self._carnes_blancas_y_legumbres = []
        self._carnes_rojas = []
        self._lacteos = []
        self._harinas_y_cereales = []
        self._calorias = 0
        self.fitness = fitness
        self._agrupar_genes_por_grupo()
        self._obtener_calorias_y_genes_invalidos()

    def _agrupar_genes_por_grupo(self):
        """Se agrupan los genes por grupo alimenticio siguiendo la estructura
        previamente definida para los cromosomas.

        Harinas y cereales: 1 a 8
        Frutas: 9 a 12
        Verduras: 13 a 17
        Carnes blancas y legumbre: 18 a 20
        Lacteos: 21 a 23
        Carnes rojas: 24
        """
        ultimo = 0
        self._harinas_y_cereales = self._raw_gens[ultimo:ultimo + comidas.PORCION_MAXIMA_HARINAS_Y_CEREALES]
        ultimo += comidas.PORCION_MAXIMA_HARINAS_Y_CEREALES
        self._frutas = self._raw_gens[ultimo:ultimo + comidas.PORCION_MAXIMA_FRUTAS]
        ultimo += comidas.PORCION_MAXIMA_FRUTAS
        self._verduras = self._raw_gens[ultimo:ultimo + comidas.PORCION_MAXIMA_VEGETALES]
        ultimo += comidas.PORCION_MAXIMA_VEGETALES
        self._carnes_blancas_y_legumbres = self._raw_gens[ultimo:ultimo + comidas.PORCION_MAXIMA_CARNES_BLANCAS]
        ultimo += comidas.PORCION_MAXIMA_CARNES_BLANCAS
        self._lacteos = self._raw_gens[ultimo:ultimo + comidas.PORCION_MAXIMA_LACTEOS]
        ultimo += comidas.PORCION_MAXIMA_LACTEOS
        self._carnes_rojas = self._raw_gens[ultimo:ultimo + comidas.PORCION_MAXIMA_CARNES_ROJAS]

    def _obtener_calorias_y_genes_invalidos(self):
        """Se recorren todos los genes (alimentos), contando las calorias
        de cada uno de los alimentos.

        Adicionalmente, se cuentan la cantidad de genes invalidos generados.
        """
        for gen in self._raw_gens:
            if gen in comidas.harines_y_cereales:
                self._calorias += comidas.harines_y_cereales[gen]
                continue
            elif gen in comidas.frutas:
                self._calorias += comidas.frutas[gen]
                continue
            elif gen in comidas.vegetales:
                self._calorias += comidas.vegetales[gen]
                continue
            elif gen in comidas.canres_blancas_y_legumbres:
                self._calorias += comidas.canres_blancas_y_legumbres[gen]
                continue
            elif gen in comidas.lacteos:
                self._calorias += comidas.lacteos[gen]
                continue
            elif gen in comidas.carnes_rojas:
                self._calorias += comidas.carnes_rojas[gen]
                continue
            elif gen != 0:
                self._invalid_gens.append(gen)

    @property
    def calorias(self):
        return self._calorias

    @property
    def genes_invalidos(self):
        return self._invalid_gens

    @property
    def frutas(self):
        return self._frutas

    @property
    def verduras(self):
        return self._verduras

    @property
    def carnes_blancas_y_legumbres(self):
        return self._carnes_blancas_y_legumbres

    @property
    def carnes_rojas(self):
        return self._carnes_rojas

    @property
    def harinas_y_cereales(self):
        return self._harinas_y_cereales

    @property
    def lacteos(self):
        return self._lacteos
