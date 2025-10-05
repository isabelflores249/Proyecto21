# Simulador simple de Blackjack, los participantes serian el/la jugador(a).

import random

# Base de datos
cartas = [
    {'figura': 'corazones', 'nombre': '2', 'valor': 2},
    {'figura': 'corazones', 'nombre': '3', 'valor': 3},
    {'figura': 'corazones', 'nombre': '4', 'valor': 4},
    {'figura': 'corazones', 'nombre': '5', 'valor': 5},
    {'figura': 'corazones', 'nombre': '6', 'valor': 6},
    {'figura': 'corazones', 'nombre': '7', 'valor': 7},
    {'figura': 'corazones', 'nombre': '8', 'valor': 8},
    {'figura': 'corazones', 'nombre': '9', 'valor': 9},
    {'figura': 'corazones', 'nombre': '10', 'valor': 10},
    {'figura': 'corazones', 'nombre': 'J', 'valor': 10},
    {'figura': 'corazones', 'nombre': 'Q', 'valor': 10},
    {'figura': 'corazones', 'nombre': 'K', 'valor': 10},
    {'figura': 'corazones', 'nombre': 'As', 'valor': 11},
    {'figura': 'diamantes', 'nombre': '2', 'valor': 2},
    {'figura': 'diamantes', 'nombre': '3', 'valor': 3},
    {'figura': 'diamantes', 'nombre': '4', 'valor': 4},
    {'figura': 'diamantes', 'nombre': '5', 'valor': 5},
    {'figura': 'diamantes', 'nombre': '6', 'valor': 6},
    {'figura': 'diamantes', 'nombre': '7', 'valor': 7},
    {'figura': 'diamantes', 'nombre': '8', 'valor': 8},
    {'figura': 'diamantes', 'nombre': '9', 'valor': 9},
    {'figura': 'diamantes', 'nombre': '10', 'valor': 10},
    {'figura': 'diamantes', 'nombre': 'J', 'valor': 10},
    {'figura': 'diamantes', 'nombre': 'Q', 'valor': 10},
    {'figura': 'diamantes', 'nombre': 'K', 'valor': 10},
    {'figura': 'diamantes', 'nombre': 'As', 'valor': 11},
    {'figura': 'tréboles', 'nombre': '2', 'valor': 2},
    {'figura': 'tréboles', 'nombre': '3', 'valor': 3},
    {'figura': 'tréboles', 'nombre': '4', 'valor': 4},
    {'figura': 'tréboles', 'nombre': '5', 'valor': 5},
    {'figura': 'tréboles', 'nombre': '6', 'valor': 6},
    {'figura': 'tréboles', 'nombre': '7', 'valor': 7},
    {'figura': 'tréboles', 'nombre': '8', 'valor': 8},
    {'figura': 'tréboles', 'nombre': '9', 'valor': 9},
    {'figura': 'tréboles', 'nombre': '10', 'valor': 10},
    {'figura': 'tréboles', 'nombre': 'J', 'valor': 10},
    {'figura': 'tréboles', 'nombre': 'Q', 'valor': 10},
    {'figura': 'tréboles', 'nombre': 'K', 'valor': 10},
    {'figura': 'tréboles', 'nombre': 'As', 'valor': 11},
    {'figura': 'picas', 'nombre': '2', 'valor': 2},
    {'figura': 'picas', 'nombre': '3', 'valor': 3},
    {'figura': 'picas', 'nombre': '4', 'valor': 4},
    {'figura': 'picas', 'nombre': '5', 'valor': 5},
    {'figura': 'picas', 'nombre': '6', 'valor': 6},
    {'figura': 'picas', 'nombre': '7', 'valor': 7},
    {'figura': 'picas', 'nombre': '8', 'valor': 8},
    {'figura': 'picas', 'nombre': '9', 'valor': 9},
    {'figura': 'picas', 'nombre': '10', 'valor': 10},
    {'figura': 'picas', 'nombre': 'J', 'valor': 10},
    {'figura': 'picas', 'nombre': 'Q', 'valor': 10},
    {'figura': 'picas', 'nombre': 'K', 'valor': 10},
    {'figura': 'picas', 'nombre': 'As', 'valor': 11}
]


# Clase de cartas, baraja y jugador

class Carta:
    def __init__(self, figura, nombre, valor): # trabajamos con los atributos de la clase carta ("figura", "nombre", "valor"). Se nombran igual que las llaves de los diccionarios de la base de datos.
        self.figura = figura
        self.nombre = nombre
        self.valor = valor

    def __str__(self):
        return f"{self.nombre} de {self.figura}"

    def as_tuple(self): # queremos que devuelva una tupla ("figura" y "nombre") 
        return (self.figura, self.nombre)

class Baraja:
    def __init__(self, cartas_data): # cartas_data es la lista de diccionarios de la base de datos
        self.cartas = [Carta(c['figura'], c['nombre'], c['valor']) for c in cartas_data]  # aquí convertimos cada atributo del diccionario en un objeto: "Carta" 

    def barajar(self): # random.shuffle va a ser usado para reordenar aleatoriamente los elementos de la lista en su lugar, despues de barajar las cartas, van a ordenarse de manera distinta cada vez.
        random.shuffle(self.cartas)

    def repartir(self):
        if not self.cartas:
            return None
        return self.cartas.pop()  # pop() lo estamos usando para que reparta las cartas del mazo al jugador.

    def tamaño(self):
        return len(self.cartas)
        
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []  # Lista de objetos "Carta"

    def recibir_carta(self, carta): # Cuando el jugador recibe una carta, se agrega a la lista "mano".
        if carta:
            self.mano.append(carta)

    def mostrar_mano(self): # Muestra la mano de cartas.
        return ", ".join(str(c) for c in self.mano)

    def calcular_puntos(self): # Suma los valores, ajusta los As, si se pasa de 21.
        total = sum(carta.valor for carta in self.mano)
        ases = sum(1 for carta in self.mano if carta.nombre == "As")
        while total > 21 and ases > 0:
            total -= 10  # convierte un As de 11 a 1
            ases -= 1 #  (-= resta el valor de la derecha a la variable de la izquierda)
        return total

    def tiene_duplicados(self): # Comprueba si hay cartas duplicadas en la mano.
        tuplas = [c.as_tuple() for c in self.mano]
        return len(set(tuplas)) != len(tuplas) # diferente de


def repartir_inicial(baraja, jugadores, n_cartas=2): # Reparte n_cartas a cada jugador (mostrando la ronda)
    for ronda in range(n_cartas):
        print("Ronda {ronda + 1}")
        for jugador in jugadores:
            carta = baraja.repartir()
            jugador.recibir_carta(carta)
            print("{jugador.nombre} recibe {carta}")

def verificar_sin_duplicados(jugadores): # Verifica que entre todas las manos no se repita una misma carta.
    conjunto = set()
    for j in jugadores:
        for carta in j.mano:
            key = carta.as_tuple()  # tupla ("figura", "nombre")
            if key in conjunto:
                return False, key   # hubo duplicado
            conjunto.add(key)
    return True, None


def decidir_ganador(jugador, compu):
    # Reglas de Blackjack:
    jugador = jugador.calcular_puntos()
    compu = compu.calcular_puntos()

    # 1. Si ambos se pasan (>21), empate.
    if jugador > 21 and compu > 21:
        return "empate", "ambos se pasaron"
    # 2. Si uno se pasa, el otro gana.
    if jugador > 21:
        return "computadora", "te pasaste"
    if compu > 21:
        return "jugador", "computadora se pasó"
    # 3. Si ninguno se pasa, gana el de más puntos.
    if jugador > compu:
        return "jugador", f"{jugador} vs {compu}"
    if compu > jugador:
        return "computadora", f"{jugador} vs {compu}"
    # 4. Si tienen lo mismo, empate.
    return "empate", f"{jugador} vs {compu}"

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
        print(f"Tu mano: {jugador.mostrar_mano()}  (Puntos: {puntos})")
        if puntos > 21:
            print("Te pasaste de 21. Fin del juego.")
            break
        opcion = input("¿Quieres otra carta? (si/no): ").strip().lower()
        if opcion == "si":
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
