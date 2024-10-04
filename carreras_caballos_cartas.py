import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Definir la baraja de cartas
palos = ['oro', 'bastos', 'copas', 'espadas']
rangos = ['1', '2', '3', '4', '5', '6', '7', 'sota', 'rey']
baraja = [(rango, palo) for rango in rangos for palo in palos]

# Definir los caballos
caballos = ['oro_caballo', 'copas_caballo', 'espadas_caballo', 'bastos_caballo']

# Definir la pista de carreras
longitud_pista = 3


# Función para repartir una carta
def repartir_carta(baraja):
    if not baraja:
        raise ValueError("No hay mas cartas")
    r_carta = random.sample(baraja, 1)[0]
    print(f"Se muestra la carta de {r_carta[1]}")
    return r_carta

# Función para mostrar la carta
def mostrar_carta(cartas):
    rango, palo = cartas
    img = mpimg.imread(f"{palo}_{rango}.png")
    imgplot = plt.imshow(img)
    plt.show()


# Función para mover un caballo
def mover_caballo(caballo, r_carta):
    print(f"El caballo {caballo} se mueve")


# Función para jugar el juego
def jugar_juego():
    # Barajar la baraja
    random.shuffle(baraja)

    # Inicializar las posiciones de los caballos
    posiciones_caballos1 = {caballo: 0 for caballo in caballos}
    #print(f"Esta es la posición de los caballos antes de comenzar {posiciones_caballos1}")

    # Inicializar el conteo de cada palo
    conteo_palos = {palo: 0 for palo in palos}

    # Jugar el juego
    while True:
        # Repartir una carta a cada caballo
        for i, caballo in enumerate(caballos):
            carta = repartir_carta(baraja)
            baraja.remove(carta)  # Remove the drawn card from the deck
            mostrar_carta(carta)
            # Incrementar el conteo del palo correspondiente
            conteo_palos[carta[1]] += 1
            #print(f"El palo {carta[1]} ha salido {conteo_palos[carta[1]]} veces")
            # Mover el caballo correspondiente
            if carta[1] == 'oro':
                posiciones_caballos1['oro_caballo'] += 1
            elif carta[1] == 'copas':
                posiciones_caballos1['copas_caballo'] += 1
            elif carta[1] == 'espadas':
                posiciones_caballos1['espadas_caballo'] += 1
            elif carta[1] == 'bastos':
                posiciones_caballos1['bastos_caballo'] += 1
            #print(f"La posición actual de los caballos es {posiciones_caballos1}")
            
        # Verificar si un caballo ha llegado a la meta
        if any(posicion >= longitud_pista for posicion in posiciones_caballos1.values()):
            ganador = [caballo for caballo, posicion in posiciones_caballos1.items() if posicion >= longitud_pista][0]
            print(f"La posición actual de los caballos es {posiciones_caballos1}")
            print(f"El caballo {ganador} ha llegado a la meta!")
            return
        
# Jugar el juego
jugar_juego()
