# Algoritmo de Dijkstra en Python

Implementación con POO (clases `Nodo` y `Grafo`) del algoritmo de Dijkstra.
Calcula la distancia mínima y la ruta completa entre un nodo origen y uno destino.

## Cómo ejecutarlo

```
python dijkstra.py
```

El programa muestra los nodos disponibles (una red de ciudades de ejemplo),
pide origen y destino, e imprime la distancia total y la secuencia de nodos.

Ejemplo:

```
Nodo origen: Guadalajara
Nodo destino: Lagos de Moreno
Distancia total: 160
Ruta: Guadalajara -> Tepatitlán -> Lagos de Moreno
```

## Cómo funciona

1. Inicializar: origen en 0 y los demás en infinito.
2. Seleccionar el nodo no visitado con menor distancia.
3. Relajar las aristas de sus vecinos.
4. Marcar el nodo como visitado.

Se guarda una tabla de distancias, una tabla de nodos anteriores (para reconstruir
la ruta) y un conjunto de visitados.
