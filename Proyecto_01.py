cartas=[]


#Diccionario con valores numéricos de las cartas (para comparar jugadas después)
valores_cartas = {
"2": 2,
"3": 3,
"4": 4, "5": 5, "6": 6,
"7": 7,
"8": 8,
"9": 9,
"10": 10,
"]": 11, "Q": 12, "K": 13, "A": 14
# Palos o colores (con simbolos Unicode)
palos = (
"Corazones":
"op"
"Diamantes":
"*",
"Tréboles":
"+",
"Picas": "*"
# Lista de símbolos de cartas
simbolos = list(valores_cartas.keys())
# Generar La baraja completa con listas y tuplas
# Cada carta será representada como una tupla (simbolo, palo, valor)
baraja = [(s, P, valores_cartas[s]) for s in simbolos for p in palos
# Mostrar cuántas cartas tiene y un ejemplo print (f"Número total de cartas: (len (baraja))")
print ("Ejemplos de cartas:", barajal:5])
Número total de cartas: 52
Ejemplos de cartas: [('2',
'Corazones', 2), ('2', 'Diamantes', 2), ('2', 'Tréboles', 2), ('2', 'Picas', 2), ['3', "Corazones', 3)]