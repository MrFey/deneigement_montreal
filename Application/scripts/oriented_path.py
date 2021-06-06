import networkx as nx
import random
from copy import copy


import sys
sys.path.append("./scripts")

from eulerian_transform import *

def graph_covering(G):
    #copie de G pour pas le modfier
    cp_G = copy(G)
    
    #arretes sans le poid
    edges = [(a,b) for (a,b,c) in cp_G]
    
    #Création du graph orienté et du non-orienté
    d_graph = nx.DiGraph()
    graph = nx.Graph()
    for (a,b,c) in G:
        d_graph.add_edge(a,b,weight=c)
        graph.add_edge(a,b,weight=c)
    
    #On Eulerianise le graph non-orienté (opération impossible avec celui orienté)
    print("[*] Eulerize Graph")
    e_graph = nx.eulerize(graph)
    #print("Added:",[(a,b) for (a,b,c) in e_graph.edges if (a,b) not in edges])
    
    #Calcul du chemin Eulerien
    print("[*] Fleury algorithm")
    e_dict = to_dict([(a,b) for (a,b,c) in e_graph.edges])
    e_path  = fleury.fleury(e_dict)
    
    
    #En se basant sur les noeuds du graphs orienté, toutes arrètes inexistantes
    #- sera remplacée par le plus court chemin pour rejoindre les 2 points
    #- Ainsi, aucun bout de chemin ne passera par une route impossible
    path = []
    visited = []
    print("[+] Adapting path to the Directed Graph")
    for (a,b) in e_path:
        path.append(a)
        # - - Si on ne peut liée 2 points, on fait un détour
        if ((a,b) not in edges):
            # - - Cas spécial:
            # (a,b) n'est pas dans edges mais (b,a) lui y est mais n'a toujours pas été visité
            # Si on applique la suite de l'algo, (b,a ne sera jamais visité)
            # Notre solution est la suivante:
            # Forcer la visite de cette Arrete et ensuite continuer le deroulement de l'algo
            # - - 
            if (b,a) in edges and (b,a) not in visited:
                tmp_path = nx.shortest_path(d_graph, a, b)
                path += tmp_path[1:]
                #- - Ajout aux visited les arretes du détour
                add_visited(visited, tmp_path)
                
                path.append(a)
                visited.append((b,a))
            
            tmp_path = nx.shortest_path(d_graph, a, b)
            #- - Ajout aux visited les arretes du détour
            add_visited(visited, tmp_path)
            path += tmp_path[1:-1]
            
        visited.append((a,b))
    return path
  
def add_visited(visited, path):
    for i in range(len(path) - 1):
        n1 = path[i]
        n2 = path[i+1]
        
        if (n1,n2) not in visited:
            visited.append((n1,n2))
    
def get_best_path(G):
    res = graph_covering(G)
    return res