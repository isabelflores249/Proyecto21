# Simulador simple de Blackjack, los participantes serian el/la jugador(a).

import random

# Base de datos
cartas = [
    {'palo': 'corazones', 'nombre': '2', 'valor': 2},
    {'palo': 'corazones', 'nombre': '3', 'valor': 3},
    {'palo': 'corazones', 'nombre': '4', 'valor': 4},
    {'palo': 'corazones', 'nombre': '5', 'valor': 5},
    {'palo': 'corazones', 'nombre': '6', 'valor': 6},
    {'palo': 'corazones', 'nombre': '7', 'valor': 7},
    {'palo': 'corazones', 'nombre': '8', 'valor': 8},
    {'palo': 'corazones', 'nombre': '9', 'valor': 9},
    {'palo': 'corazones', 'nombre': '10', 'valor': 10},
    {'palo': 'corazones', 'nombre': 'J', 'valor': 10},
    {'palo': 'corazones', 'nombre': 'Q', 'valor': 10},
    {'palo': 'corazones', 'nombre': 'K', 'valor': 10},
    {'palo': 'corazones', 'nombre': 'As', 'valor': 11},
    {'palo': 'diamantes', 'nombre': '2', 'valor': 2},
    {'palo': 'diamantes', 'nombre': '3', 'valor': 3},
    {'palo': 'diamantes', 'nombre': '4', 'valor': 4},
    {'palo': 'diamantes', 'nombre': '5', 'valor': 5},
    {'palo': 'diamantes', 'nombre': '6', 'valor': 6},
    {'palo': 'diamantes', 'nombre': '7', 'valor': 7},
    {'palo': 'diamantes', 'nombre': '8', 'valor': 8},
    {'palo': 'diamantes', 'nombre': '9', 'valor': 9},
    {'palo': 'diamantes', 'nombre': '10', 'valor': 10},
    {'palo': 'diamantes', 'nombre': 'J', 'valor': 10},
    {'palo': 'diamantes', 'nombre': 'Q', 'valor': 10},
    {'palo': 'diamantes', 'nombre': 'K', 'valor': 10},
    {'palo': 'diamantes', 'nombre': 'As', 'valor': 11},
    {'palo': 'tréboles', 'nombre': '2', 'valor': 2},
    {'palo': 'tréboles', 'nombre': '3', 'valor': 3},
    {'palo': 'tréboles', 'nombre': '4', 'valor': 4},
    {'palo': 'tréboles', 'nombre': '5', 'valor': 5},
    {'palo': 'tréboles', 'nombre': '6', 'valor': 6},
    {'palo': 'tréboles', 'nombre': '7', 'valor': 7},
    {'palo': 'tréboles', 'nombre': '8', 'valor': 8},
    {'palo': 'tréboles', 'nombre': '9', 'valor': 9},
    {'palo': 'tréboles', 'nombre': '10', 'valor': 10},
    {'palo': 'tréboles', 'nombre': 'J', 'valor': 10},
    {'palo': 'tréboles', 'nombre': 'Q', 'valor': 10},
    {'palo': 'tréboles', 'nombre': 'K', 'valor': 10},
    {'palo': 'tréboles', 'nombre': 'As', 'valor': 11},
    {'palo': 'picas', 'nombre': '2', 'valor': 2},
    {'palo': 'picas', 'nombre': '3', 'valor': 3},
    {'palo': 'picas', 'nombre': '4', 'valor': 4},
    {'palo': 'picas', 'nombre': '5', 'valor': 5},
    {'palo': 'picas', 'nombre': '6', 'valor': 6},
    {'palo': 'picas', 'nombre': '7', 'valor': 7},
    {'palo': 'picas', 'nombre': '8', 'valor': 8},
    {'palo': 'picas', 'nombre': '9', 'valor': 9},
    {'palo': 'picas', 'nombre': '10', 'valor': 10},
    {'palo': 'picas', 'nombre': 'J', 'valor': 10},
    {'palo': 'picas', 'nombre': 'Q', 'valor': 10},
    {'palo': 'picas', 'nombre': 'K', 'valor': 10},
    {'palo': 'picas', 'nombre': 'As', 'valor': 11}
]

# Diccionario 
# Queremos ver como corre el programa, por ende debemos incluir una simulación de ejemplo dentro del main que debemos hacer

valores_por_nombre = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'As': 11
}

# Clase de cartas, baraja y jugador

class Carta:
    def __init__(self, palo: str, nombre: str, valor: int): # trabajamos con los atributos de la clase carta ("palo", "nombre", "valor"). Se nombran igual que las llaves de los diccionarios de la base de datos.
        self.palo = palo
        self.nombre = nombre
        self.valor = valor

    def __str__(self):
        return f"{self.nombre} de {self.palo}"

    def as_tuple(self): # queremos que devuelva una tupla ("palo" y "nombre") 
        return (self.palo, self.nombre)

class Baraja:
    def __init__(self, cartas_data): # cartas_data es la lista de diccionarios de la base de datos
        self.cartas = [Carta(c['palo'], c['nombre'], c['valor']) for c in cartas_data]  # aquí convertimos cada diccionario en un objeto "Carta" 

    def barajar(self): # random.shuffle va a ser usado para reordenar aleatoriamente los elementos de la lista en su lugar, despues de barajar las cartas van a ordenarse de manera distinta cada vez, aun asi no crea cartas nuevas.
        random.shuffle(self.cartas)

    def repartir(self):
        if not self.cartas:
            return None
        return self.cartas.pop()  # pop() lo estamos usando para que reparta las cartas del mazo al jugador.

    def tamaño(self):
        return len(self.cartas)

class Jugador:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.mano = []  # Lista de objetos "Carta"

    def recibir_carta(self, carta: Carta): # Cuando el jugador recibe una carta, se agrega a la lista "mano".
        if carta:
            self.mano.append(carta)

    def mostrar_mano(self, ocultar_primera=False): # Devuelve la mano de cartas en texto legible. Si es de la computadora, oculta la primera carta para no mostrarla. Por ejemplo: muestra "As de corazones, 10 de picas" en vez de {'palo': 'corazones', 'nombre': 'As', 'valor': 11}.
        if ocultar_primera and self.mano:
            visibles = [str(self.mano[i]) for i in range(1, len(self.mano))]
            return "[carta oculta], " + ", ".join(visibles) if visibles else "[carta oculta]"
        return ", ".join(str(c) for c in self.mano)

    def calcular_puntos(self): # Suma los valores; ajusta los As (11->1) si se pasa de 21
        total = sum(carta.valor for carta in self.mano)
        ases = sum(1 for carta in self.mano if carta.nombre == "As")
        while total > 21 and ases > 0:
            total -= 10  # convierte un As de 11 a 1
            ases -= 1
        return total

    def tiene_duplicados(self): # Comprobar si hay cartas duplicadas en la mano con un ejemplo.
        tuplas = [c.as_tuple() for c in self.mano]          # lista de tuplas
        return len(set(tuplas)) != len(tuplas)              # True si había duplicados


def repartir_inicial(baraja: Baraja, jugadores: list, n_cartas=2): # Reparte n_cartas a cada jugador (uso de bucle for anidado).
    for _ in range(n_cartas):
        for jugador in jugadores:
            jugador.recibir_carta(baraja.repartir())


def verificar_sin_duplicados(jugadores: list): # Verifica que entre todas las "manos" no se repita una misma carta, usamos un conjunto de tuplas ("palo", "nombre")
    conjunto = set()
    for j in jugadores:
        for carta in j.mano:
            key = carta.as_tuple()         # tupla ("palo" y "nombre")
            if key in conjunto:
                return False, key          # hubo duplicado, entonces..
            conjunto.add(key)
    return True, None


def decidir_ganador(jugador: Jugador, compu: Jugador): # Reglas de Blackjack:
    pj = jugador.calcular_puntos()
    pc = compu.calcular_puntos()

    # 1. Si alguno se pasa (>21) pierde:
    if pj > 21 and pc > 21:
        return "empate", "ambos se pasaron"
    if pj > 21:
        return "computadora", "te pasaste"
    if pc > 21:
        return "jugador", "computadora se pasó"

    # 2. Quien tiene puntos más altos gana:
    if pj > pc:
        return "jugador", f"{pj} vs {pc}"
    if pc > pj:
        return "computadora", f"{pj} vs {pc}"
    return "empate", f"{pj} vs {pc}"

# Main()

def jugar():
    print("Simulador Blackjack (Jugador vs Computadora)") # Creamos la baraja usando exactamente la base "Cartas" que diste.
    baraja = Baraja(cartas)                         # Llamamos directamente la base de datos
    baraja.barajar()                                # Mezclamos

    jugador = Jugador("Tú")
    computadora = Jugador("Computadora")

    # Reparto inicial (2 cartas cada uno, computadora y jugador).
    repartir_inicial(baraja, [jugador, computadora], n_cartas=2)

    # Verificación con conjuntos: aseguramos que no haya duplicados.
    ok, clave = verificar_sin_duplicados([jugador, computadora])
    if not ok:
        print("ERROR: Se encontró una carta duplicada:", clave)
        return

    # Turno del jugador
    
    while True:
        puntos = jugador.calcular_puntos()
        print("Tu mano: {jugador.mostrar_mano()}  (Puntos: {puntos})")
        if puntos > 21:
            print("Te pasaste de 21. Fin del juego.")
            break
        opcion = input("¿Quieres otra carta? (si/no): ").strip().lower()
        if opcion == "s":
            carta = baraja.repartir()
            if carta:
                jugador.recibir_carta(carta)
                print("Recibiste:", carta)
            else:
                print("No quedan cartas en la baraja.")
                break
        else:
            break

    # Turno de la computadora
    
    print("Turno de la computadora...")
    print("Computadora muestra:", computadora.mostrar_mano(ocultar_primera=True))
    while computadora.calcular_puntos() < 17:
        carta = baraja.repartir()
        if carta:
            computadora.recibir_carta(carta)
            # no hay que mostrar las cartas de la computadora, como es siempre el rival no tendria sentido que nos la muestre.
        else:
            break

    # Resultados 
    
    print("Resultados finales")
    print("Tu mano final: ", jugador.mostrar_mano(), "(Puntos:", jugador.calcular_puntos(), ")")
    print("Mano de computadora:", computadora.mostrar_mano(), "(Puntos:", computadora.calcular_puntos(), ")")

    ganador, motivo = decidir_ganador(jugador, computadora)
    if ganador == "jugador":
        print("Ganaste (", motivo, ")")
    elif ganador == "computadora":
        print("Ganó la computadora. (", motivo, ")")
    else:
        print("Empate. (", motivo, ")")

    # Comprobación final de duplicados en todas las cartas repartidas.
    ok2, clave2 = verificar_sin_duplicados([jugador, computadora])
    if not ok2:
        print("ADVERTENCIA: carta duplicada:", clave2)


def main():
    jugar()


if __name__ == "__main__":
    main()

#Como se juega:

#se reparten 2 cartas a cada jugador usando la funcion "repartir_inicial"
#mientras el jugador no se pase de 21 puntos, se repite
#el jugador decide si quiere otra carta o no
#si el jugador supera 21, pierde el turno automaticamente
#la compu muestra su mano parcialmente, es decir, su primera carta se mantiene oculta
#la computadora sigue sacando cartas mientras su total sea menor que 17
#para determinar el jugador, se calculan los puntos finales de ambos jugadores
#se decide segun, si alguien supera 21 pierde, si nadie se pasa, gana quien se acerca mas a 21, si ambos tienen el mismo puntaje es empate 
#Inicio, Crear baraja, Barajar, Repartir, Turno jugador, Turno computadora, Calcular puntos, Mostrar ganador.
