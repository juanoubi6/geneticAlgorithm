# 7 es la cantidad de bits minima que necesito para representar mis 77 comidas ya que con 7 bits logro 128 numeros
BITS_GEN = 7

# 22 es la cantidad maxima de porciones (sumando todas las porciones maximas)
LONGITUD_CROMOSOMA = 24 * BITS_GEN

food_gen_dict = {
    1: 'Manzana',
    2: 'Piña',
    3: 'Pera',
    4: 'Plátano',
    5: 'Arándano',
    6: 'Naranja',
    7: 'Moras',
    8: 'Arándano rojo',
    9: 'Fresa',
    10: 'Higo',
    11: 'Pomelo',
    12: 'Melón',
    13: 'Frambuesas',
    14: 'Kiwi',
    15: 'Cerezas',
    16: 'Mandarina',
    17: 'Mango',
    18: 'Maracuyá',
    19: 'Ciruela',
    20: 'Sandía',
    21: 'Uvas',
    22: 'Berenjena',
    23: 'Alcachofa',
    24: 'Aguacate',
    25: 'Coliflor',
    26: 'Brócoli',
    27: 'Champiñones',
    28: 'Lechuga',
    29: 'Pepino',
    30: 'Zanahoria',
    31: 'Papa',
    32: 'Calabaza',
    33: 'Puerro',
    34: 'Maíz',
    35: 'Acelga',
    36: 'Pimiento',
    37: 'Remolacha',
    38: 'Col de Bruselas',
    39: 'Rúcula',
    40: 'Espárrago',
    41: 'Espinaca',
    42: 'Cebolla',
    43: 'Salchicha',
    44: 'Ciervo',
    45: 'Ternera',
    46: 'Cordero',
    47: 'Salami',
    48: 'Jamón',
    49: 'Bacon',
    50: 'Filete de vacuno',
    51: 'Carne picada de vacuno',
    52: 'Filete de nalga de vacuno',
    53: 'Filete de cerdo',
    54: 'Carne grasa de cerdo',
    55: 'Carne magra de cerdo',
    56: 'Pechuga de pollo',
    57: 'Trucha',
    58: 'Salmón',
    59: 'Atún',
    60: 'Huevo',
    61: 'Poroto (Judias)',
    62: 'Arvejas (Guisantes)',
    63: 'Queso cheddar',
    64: 'Queso emmental',
    65: 'Leche de coco',
    66: 'Leche',
    67: 'Yogur natural',
    68: 'Arroz blanco',
    69: 'Arroz integral',
    70: 'Avena',
    71: 'Copos de maíz',
    72: 'Pan de centeno',
    73: 'Pan de trigo blanco',
    74: 'Pan de trigo integral',
    75: 'Pasta al huevo',
    76: 'Pasta de sémola',
    77: 'Polenta',
    78: 'Cereales con chocolate',
    79: 'Canelones',
    80: 'Fideos de soja',
    81: 'Mostachol',
    82: 'Tallarines',
    83: 'Spaguetti'
}

PORCION_MINIMA_FRUTAS=2
PORCION_MAXIMA_FRUTAS=4
fruts = {
    1: 52,
    2: 55,
    3: 55,
    4: 88,
    5: 35,
    6: 45,
    7: 43,
    8: 46,
    9: 32,
    10: 107,
    11: 50,
    12: 54,
    13: 36,
    14: 51,
    15: 50,
    16: 50,
    17: 62,
    18: 97,
    19: 47,
    20: 30,
    21: 70,
}

PORCION_MINIMA_VEGETALES=3
PORCION_MAXIMA_VEGETALES=5
vegetables = {
    22: 24,
    23: 47,
    24: 160,
    25: 25,
    26: 35,
    27: 22,
    28: 14,
    29: 15,
    30: 36,
    31: 86,
    32: 19,
    33: 31,
    34: 108,
    35: 19,
    36: 21,
    37: 43,
    38: 43,
    39: 25,
    40: 18,
    41: 23,
    42: 40,
}

PORCION_MINIMA_CARNES_ROJAS=0
PORCION_MAXIMA_CARNES_ROJAS=1
red_meat = {
    43: 375,
    44: 375,
    45: 94,
    46: 178,
    47: 507,
    48: 335,
    49: 645,
    50: 115,
    51: 212,
    52: 162,
    53: 171,
    54: 311,
    55: 143,
}

PORCION_MINIMA_CARNES_BLANCAS=2
PORCION_MAXIMA_CARNES_BLANCAS=3
white_meat_and_legumes = {
    56: 111,
    57: 50,
    58: 137,
    59: 144,
    60: 155,
    61: 25,
    62: 82,
}

PORCION_MINIMA_LACTEOS=2
PORCION_MAXIMA_LACTEOS=3
dairy_products = {
    63: 403,
    64: 382,
    65: 136,
    66: 47,
    67: 62,
}

PORCION_MINIMA_HARINAS_Y_CEREALES=4
PORCION_MAXIMA_HARINAS_Y_CEREALES=8
bread_and_cereals = {
    68: 354,
    69: 350,
    70: 367,
    71: 350,
    72: 241,
    73: 255,
    74: 239,
    75: 368,
    76: 361,
    77: 358,
    78: 358,
    79: 146,
    80: 216,
    81: 184,
    82: 370,
    83: 370
}











