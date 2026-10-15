"""Algoritmo de Dijkstra con Programación Orientada a Objetos.

Encuentra la distancia mínima y la ruta completa entre un nodo
origen y un nodo destino en un grafo ponderado no dirigido.
"""


class Nodo:
    """Un vértice del grafo. Guarda sus vecinos y el peso de cada conexión."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}  # {nombre_vecino: peso}


class Grafo:
    """Grafo ponderado usando lista de adyacencia."""

    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nombre):
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodo(nombre)

    def agregar_conexion(self, origen, destino, peso):
        if peso < 0:
            raise ValueError("Dijkstra no funciona con pesos negativos")
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        # Conexión en ambos sentidos (grafo no dirigido)
        self.nodos[origen].vecinos[destino] = peso
        self.nodos[destino].vecinos[origen] = peso

    def dijkstra(self, inicio, destino):
        """Devuelve (distancia_total, camino). Si no hay ruta: (inf, [])."""
        if inicio not in self.nodos or destino not in self.nodos:
            raise ValueError("El origen o el destino no existen en el grafo")

        distancias = {}
        anteriores = {}
        visitados = set()

        # 1. Inicializar: origen en 0 y los demás en infinito
        for nombre in self.nodos:
            distancias[nombre] = float("inf")
            anteriores[nombre] = None
        distancias[inicio] = 0

        while len(visitados) < len(self.nodos):
            # 2. Seleccionar el nodo no visitado con menor distancia
            nodo_actual = None
            menor_distancia = float("inf")
            for nombre in self.nodos:
                if nombre not in visitados and distancias[nombre] < menor_distancia:
                    menor_distancia = distancias[nombre]
                    nodo_actual = nombre

            # Si no queda ninguno alcanzable, terminamos
            if nodo_actual is None:
                break

            # Si llegamos al destino, su costo ya es definitivo
            if nodo_actual == destino:
                break

            # 3. Relajar las aristas de los vecinos
            for vecino, peso in self.nodos[nodo_actual].vecinos.items():
                nueva_distancia = distancias[nodo_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = nodo_actual

            # 4. Marcar como visitado
            visitados.add(nodo_actual)

        # Si el destino sigue en infinito, no hay ruta
        if distancias[destino] == float("inf"):
            return float("inf"), []

        # Reconstruir el camino de atrás hacia adelante
        camino = []
        actual = destino
        while actual is not None:
            camino.append(actual)
            actual = anteriores[actual]
        camino.reverse()

        return distancias[destino], camino


def main():
    # Ejemplo: red de transporte entre ciudades (peso = km)
    grafo = Grafo()
    grafo.agregar_conexion("Guadalajara", "Tepatitlán", 70)
    grafo.agregar_conexion("Guadalajara", "Zapotlanejo", 40)
    grafo.agregar_conexion("Guadalajara", "Tequila", 65)
    grafo.agregar_conexion("Zapotlanejo", "Tepatitlán", 45)
    grafo.agregar_conexion("Tepatitlán", "Lagos de Moreno", 90)
    grafo.agregar_conexion("Zapotlanejo", "Lagos de Moreno", 140)
    grafo.agregar_conexion("Tequila", "Lagos de Moreno", 200)
    grafo.agregar_nodo("Isla Aislada")  # nodo sin conexiones, para probar

    print("Nodos disponibles:", ", ".join(grafo.nodos))
    origen = input("Nodo origen: ").strip()
    destino = input("Nodo destino: ").strip()

    try:
        distancia, camino = grafo.dijkstra(origen, destino)
    except ValueError as error:
        print("Error:", error)
        return

    if not camino:
        print(f"No existe ruta de {origen} a {destino}")
    else:
        print(f"\nDistancia total: {distancia}")
        print("Ruta:", " -> ".join(camino))


if __name__ == "__main__":
    main()
