#! /usr/bin/env python3
#-- all rights: @fey --#
#-- py-version: 3.*  --#

from copy import copy
'''
    is_connected - Checks if a graph in the form of a dictionary is
    connected or not, using Breadth-First Search Algorithm (BFS)
'''
def is_connected(G):
    start_node = list(G)[0]
    color = {v: 'white' for v in G}
    color[start_node] = 'gray'
    S = [start_node]
    while len(S) != 0:
        u = S.pop()
        for v in G[u]:
            if color[v] == 'white':
                color[v] = 'gray'
                S.append(v)
            color[u] = 'black'
    return list(color.values()).count('black') == len(G)

'''
    odd_degree_nodes - returns a list of all G odd degrees nodes
'''
def odd_degree_nodes(G):
    odd_degree_nodes = []
    for u in G:
        if len(G[u]) % 2 != 0:
            odd_degree_nodes.append(u)
    return odd_degree_nodes

'''
    from_dict - return a list of tuples links from a graph G in a
    dictionary format
'''
def from_dict(G):
    links = []
    for u in G:
        for v in G[u]:
            links.append((u,v))
    return links

'''
    fleury(G) - return eulerian trail from graph G or a
    string 'Not Eulerian Graph' if it's not possible to trail a path
'''
def fleury(G):
    '''
        checks if G has eulerian cycle or trail
    '''
    odn = odd_degree_nodes(G)
    #print(odn)
    if len(odn) > 2 or len(odn) == 1:
        return 'Not Eulerian Graph'
    else:
        g = copy(G)
        trail = []
        if len(odn) == 2:
            u = odn[0]
        else:
            u = list(g)[0]

        # - - - 
        init = len(from_dict(g)) + 0.0
        old_pourcentage = -1
        # - - -
        
        while len(from_dict(g)) > 0:
            
            # - - - - Affichage du % - - - - -
            pourcentage = round((init - len(from_dict(g)) )*100.0/init, 1)
            if pourcentage > old_pourcentage:
                len_to_clear = len(str(old_pourcentage))+1
                clear = '\x08' * (len_to_clear + 2)
                old_pourcentage = pourcentage
                print(clear,end="")
                print("\r[*] Compute Eulerian path:", pourcentage, "%", end='', flush=True)
                print(clear,end="")
            # - - - - - - - - - - - - - - - - -
            
            current_vertex = u
            for u in g[current_vertex]:
                g[current_vertex].remove(u)
                g[u].remove(current_vertex)
                bridge = not is_connected(g)
                if bridge:
                    g[current_vertex].append(u)
                    g[u].append(current_vertex)
                else:
                    break
            if bridge:
                g[current_vertex].remove(u)
                g[u].remove(current_vertex)
                g.pop(current_vertex)
            trail.append((current_vertex, u))
    print("\r[*] Compute Eulerian path:", "100", "%", end='', flush=True)
    print("\n[+] Euleriand Path Found !")
    return trail



