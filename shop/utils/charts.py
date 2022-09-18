months = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]
colorPalette = ['#55efc4', '#81ecec', '#a29bfe', '#ffeaa7', '#fab1a0', '#ff7675', '#fd79a8']
colorPrimary, colorSuccess, colorDanger = '#79aec8', colorPalette[0], colorPalette[5]

def get_year_dict():
    """Cria um dicionário de meses e valores, 
       que usaremos para adicionar os dados mensais.
    """
    year_dict = dict()

    for month in months:
        year_dict[month] = 0

    return year_dict

def generate_color_palette(amount):
    """ Gera uma paleta de cores repetida que 
        passaremos para nossos gráficos. 
    """
    palette = []

    i = 0
    while i < len(colorPalette) and len(palette) < amount:
        palette.append(colorPalette[i])
        i += 1
        if i == len(colorPalette) and len(palette) < amount:
            i = 0

    return palette
