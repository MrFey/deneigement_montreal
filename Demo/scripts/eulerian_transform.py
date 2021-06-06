#!/usr/bin/env python
# coding: utf-8

import numpy as np
import importlib as iplib
import fleury as fleury
iplib.reload(fleury)

# transformation du graph vers un graph eulerien
def odd_vertices(n, edges):
    deg = [0] * n
    for (a,b,c) in edges:
        deg[a] += 1
        deg[b] += 1

    return [a for a in range(n) if deg[a] % 2]

def is_edges(n, edges, node1, node2):
    for (a, b, c) in edges:
        if (a == node1 and b == node2) or (a == node2 and b == node1):
            return (a,b,c)
    return None

def list_edges(n, edges, l_vodd):
    res = []
    index = 1
    for a in l_vodd:
        index+=1
        for b in l_vodd:
            if (a == b):
                continue
            tmp = is_edges(n, edges, a, b)
            if (tmp and tmp not in res) :
                #print("MATCH:", a, b)
                res.append(tmp)
    return res

def shortest_edge_idx(l_edges):
    if (len(l_edges) == 0):
        return None
    shortest = l_edges[0][2]
    shortest_index = 0

    index = 1
    for (a,b,c) in l_edges[1:]:
        if (c < shortest):
            shortest = c
            shortest_index = index
        index+=1
    return l_edges[shortest_index]

def transform_to_eulerian(n, edges):
    list_vodd = odd_vertices(n, edges)
    l_edges = list_edges(n, edges, list_vodd)

    len_vodd = len(list_vodd)
    if (len_vodd == 2 or len_vodd == 0): #case is already eulerian
        return edges
    #print(list_vodd)
    #print(l_edges)
    while(len(list_vodd) != 2):
        list_vodd = odd_vertices(n, edges)
        l_edges = list_edges(n, edges, list_vodd)

        shortest_edge = shortest_edge_idx(l_edges)
        #add edge between two
        (a,b,c) = shortest_edge
        new_edge = (b,a,c)
        edges.append(new_edge)

        #delete from vodd
        if (a in list_vodd):
            list_vodd.remove(a)
        if (b in list_vodd):
            list_vodd.remove(b)

        #delete from list_edges
        l_edges.remove(shortest_edge)
    return edges

#adapter le format de notre graph au format dictionnaire de l'algo "fleury"
def to_dict(G):
    dict_graph = {}
    for (a,b) in G:
        dict_graph[a] = []
        dict_graph[b] = []
    for (a,b) in G:
        dict_graph[a].append(b)
        dict_graph[b].append(a)
    return dict_graph


# In[96]:


#On utlise toutes les fonctions précedement définies:

def transform_and_find_eulerian_path(graph, verbose=False):
    if (verbose):
        print("Initial Graph:", graph)
    print("[*] fixing the Graph")
    graph = transform_to_eulerian(len(graph), graph)
    print("[+] Graph fixed")
    graph2 = []
    if (verbose):
        print("To Eulerian Graph:", graph)
    ### on enlève la ponderation
    for (a,b,c) in graph:
        graph2.append((a,b))

    print("[*] Graph to dict")
    dict_graph2 = to_dict(graph2)
    print("[*] Starting Fleury")
    E_path = fleury.fleury(dict_graph2)
    if (verbose):
        print("[!] Eulerian path:", E_path)
    return E_path

