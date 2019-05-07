# ------------- Visualization parameters ------------

DRAW_PHYLO_TREE = 0

DRAW_PARETO_FRONT = 1

DRAW_CUMULATIVE_YES_VOTES = 2

VISUALIZATION_TYPES = 3

# ------------- Visual parameters -------------------

colors = ['r', 'g', 'b', 'y', 'o', 'p', 'w', 'j', 'c', 's']

colorsUppercase = ['R', 'G', 'B', 'Y', 'O', 'P', 'W', 'J', 'C', 'S']

upperToLowerCaseColors = {
    'R': 'r',
    'G': 'g',
    'B': 'b',
    'Y': 'y',
    'O': 'o',
    'P': 'p',
    'W': 'w',
    'J': 'j',
    'C': 'c',
    'S': 's'
}

upperToLowerCaseReinforcements = {'Y': 'y', 'N': 'n'}

reinforcements = ['y', 'n']
reinforcementsUppercase = ['Y', 'N']


colorNames = [
    '[r]ed   ',
    '[g]reen ',
    '[b]lue  ',
    '[y]ellow',
    '[o]range',
    '[p]urple',
    '[w]hite ',
    '[j]ade  ',
    '[c]yan  ',
    '[s]ilver'
]

colorNamesNoParens = [
    'red',
    'green',
    'blue',
    'yellow',
    'orange',
    'purple',
    'white',
    'jade',
    'cyan',
    'silver'
]

colorNameDict = {
    'r': 'red',
    'g': 'green',
    'b': 'blue',
    'y': 'yellow',
    'o': 'orange',
    'p': 'purple',
    'w': 'white',
    'j': 'jade',
    'c': 'cyan',
    's': 'silver'
}

colorRGBs = [
    [1, 0, 0],  # red
    [0, 1, 0],  # green
    [0, 0, 1],  # blue
    [1, 1, 0],  # yellow
    [1, 0.65, 0],  # orange
    [0.5, 0, 0.5],  # purple
    [1, 1, 1],  # white
    [0.5, 1, 0.5],  # light green
    [0, 1, 1],  # cyan
    [0.5, 0.5, 0.5]  # silver
]

colorRGBsPygame = colorRGBs
for i in range(0, len(colorRGBsPygame)): 
    for j in range(0, len(colorRGBsPygame[i])): 
        colorRGBsPygame[i][j] = colorRGBsPygame[i][j] * 255

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 1000

MARKER_SIZE = 24 
PRIMARY_MARKER_SIZE = MARKER_SIZE * 2

FPS = 60
popSize = len(colors)
