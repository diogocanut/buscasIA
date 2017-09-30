import collections

class Grafo:
    def __init__(self):
        self.arestas = {}
    
    def arestas_do_vertice(self, id):
        return self.arestas[id]

grafo = Grafo()
grafo.arestas = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
}

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()

def busca_largura(grafo, inicio):
	buffer = Queue()
	buffer.put(inicio)
	visitados = {}
	visitados[inicio] = True

	while not buffer.empty():
		visitando = buffer.get()
		print("Visitando: " + visitando)
		for prox in grafo.arestas_do_vertice(visitando):
			if prox not in visitados:
				buffer.put(prox)
				visitados[prox] = True





