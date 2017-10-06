import collections
import sys

class Grafo:
    def __init__(self):
        self.arestas = {}
    
    def arestas_do_vertice(self, id):
        return self.arestas[id]

grafo = Grafo()
grafo.arestas = {
    'S0': ['S1', 'S0', 'S2'],
    # estado inicial, aspirador de pó no piso direito com os 2 pisos sujos
    #S1 caso o aspirador se mova para a esquerda a partir de S0
    #S2 caso o aspirador aspire a sujeira do comodo atual
    #S0 caso mova-se para a direita
    'S1': ['S1', 'S0','S5'],
    #S1 caso o aspirador se mova para o comodo da esquerda
    #S0 caso mova-se para o comodo da direita
    #S5 caso aspire o comodo atual
    'S2': ['S3', 'S2', 'S2'],
    #mover esquerda: S3
    #mover direita: S2
    #aspirar: S2
    'S3': ['S3', 'S2', 'S7'],
    #mover esquerda: S3
    #mover direita: S2
    #aspirar: S7
    'S4': ['S5', 'S4', 'S6'],
    #mover esquerda: S5
    #mover direita: S4
    #aspirar: S6
    'S5': ['S5', 'S4', 'S5'],
    #mover esquerda: S5
    #mover direita: S4
    #aspirar: S5
    'S6': ['S7', 'S6', 'S6'],
    #mover esquerda: S7
    #mover direita: S6
    #aspirar: S6    
    'S7': ['S7', 'S6', 'S7'],
    #mover esquerda: S7
    #mover direita: S6
    #aspirar: S7
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



def busca_largura_IA(grafo, inicio, final):
    buffer = Queue()
    buffer.put(inicio)
    visitados = {}
    visitados[inicio] = True

    while not buffer.empty():
        visitando = buffer.get()
        print("Visitando: " + visitando)
        if visitando == 'S7': 
            sys.exit(1)
        for prox in grafo.arestas_do_vertice(visitando):   
            buffer.put(prox)


