import comidas


class Individuo:

    def __init__(self, lista_genes, fitness=None):
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
        for gen in self._raw_gens:
            if gen in comidas.bread_and_cereals:
                self._calorias += comidas.bread_and_cereals[gen]
                continue
            elif gen in comidas.fruts:
                self._calorias += comidas.fruts[gen]
                continue
            elif gen in comidas.vegetables:
                self._calorias += comidas.vegetables[gen]
                continue
            elif gen in comidas.white_meat_and_legumes:
                self._calorias += comidas.white_meat_and_legumes[gen]
                continue
            elif gen in comidas.dairy_products:
                self._calorias += comidas.dairy_products[gen]
                continue
            elif gen in comidas.red_meat:
                self._calorias += comidas.red_meat[gen]
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
