import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np


listaJ = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'A', 'J']
listaA = ['B', 'C', 'D', 'E', 'G', 'H', 'I', 'J']


def caminhosDFS(grafo, inicio, final):
    pilha = [(inicio, [inicio])]
    while pilha:
        (vertice, aresta) = pilha.pop()
        for vizinho in grafo[vertice] - set(aresta):
            if vizinho == final:
                yield aresta + [vizinho]
            else:
                pilha.append((vizinho, aresta + [vizinho]))


def caminhoBFS(grafo, inicio, final):
    pilha = [(inicio, [inicio])]
    while pilha:
        (vertice, caminho) = pilha.pop(0)
        for next in grafo[vertice] - set(caminho):
            if next == final:
                yield caminho + [next]
            else:
                pilha.append((next, caminho + [next]))


def shortest_path(grafo, inicio, final):
    try:
        return next(caminhoBFS(grafo, inicio, final))
    except StopIteration:
        return []


def close_event():
    plt.close()


print("Encontre o menor caminho de A a F")
dificuldade = int(
    input("Dificuldades \n 1: Facil(60 seg) \n 2: Normal(30 seg) \n 3: Dificil(10 seg) \n 4: Expert(5 seg) "))

if dificuldade == 1:
    duracao = 60000
if dificuldade == 2:
    duracao = 30000
if dificuldade == 3:
    duracao = 10000
if dificuldade == 4:
    duracao = 5000


grafo = {'A': set([]),
         'B': set([]),
         'C': set([]),
         'D': set([]),
         'E': set([]),
         'F': set([]),
         'G': set([]),
         'H': set([]),
         'I': set([]),
         'J': set([]),
         }

diff = []
for node in grafo:
    diff.append(node)
    ale = random.randint(1, 3)
    print(diff)
    for i in range(ale):
        if node == 'A':
            grafo[node].add(random.choice(np.setdiff1d(listaA, diff)))
        else:
            grafo[node].add(random.choice(np.setdiff1d(listaJ, diff)))
    diff.remove(node)        


temp = list(shortest_path(grafo, 'A', 'F'))

if temp is None:
    caminhos = []
else:
    caminhos = temp


fig = plt.figure()

timer = fig.canvas.new_timer(interval=duracao)
timer.add_callback(close_event)


G = nx.DiGraph(grafo)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)


timer.start()
plt.show()


lst = []
n = int(input("Entre o numero de nós de A a F: "))
print("Digite os nós em ordem do A ao F com letra maiuscula: ")
for i in range(0, n):
    no = str(input())

    lst.append(no)

print(lst)

if caminhos == lst:
    print("você acertou \o/ ")

else:
    print("você errou ")
