#main idea
#run Bellman ford to detect if there is a negative weight cycyle and if there is one the return list[1:n-1]
#if we have any negative cycle we can gain as much time to cross with all the bunnies.
#
#rewrite negative weighted edges to positive
#run dijkastra as we no longer have negative edges
#run Johnson algo to find all pair shortest paths
#do a bfs to construct orignal path for finding orignal weight
#keep a count of maximum number of visited nodes from source to target

#using a heap for simulating dijkastra
from heapq import heappush, heappop
import sys

#max_int
inf = sys.maxint
#min_int
neg_inf = -(inf - 1)
#extra [0,0,......] row to use as source
def create_empty_source(times, n):
    source_vertex = [0 for i in range(n)]
    times.append(source_vertex)
    return times

#typical implementation of bellman_ford algo, checks for negative cycles.
def simulate_bellman_ford(times, n):
    source_index = n
    distance = [inf for i in range(n + 1)] 
    predecessor = [None for i in range(n + 1)] 
    distance[source_index] = 0
    for k in range(n + 1):
        for u in range(n + 1):
            for v in range(n):
                w = times[u][v]
                if w != inf and distance[u] != inf and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u

    negative_cycle = False
    # check if there is any negative cycle
    for u in range(n):
        for v in range(n):
            w = times[u][v]
            if w != inf and distance[u] != inf and distance[u] + w < distance[v]:
                negative_cycle = True

    return negative_cycle, distance, predecessor

#reweight the graph to orignal weight
def construct_orignal(temp_graph, distance, n):
    weighted_g = []
    for i in range(n):
        temp = []
        for j in range(n):
            new_weight = temp_graph[i][j] + distance[i] - distance[j]
            temp.append(new_weight)
        weighted_g.append(temp)
    return weighted_g

#typical implementation of dijkastra to find shortest path: No negative weight.
def simulate_dijkastra(weighted_g, src, n):
    visited = [False for i in range(n)]
    distance = {i: inf for i in range(n)}
    path = {src: None}
    nodes = []
    for i in range(n): heappush(nodes, (0 if i == src else inf, i))
    while nodes:
        current = heappop(nodes)
        current_distance, curr_node = current

        distance[curr_node] = current_distance
        visited[curr_node] = True

        new_set = []
        for node_distance, node_key in nodes:
            if not visited[node_key]:
                w = weighted_g[curr_node][node_key]
                if w != inf and current_distance + w < distance[node_key]:
                    distance[node_key] = current_distance + w
                    path[node_key] = curr_node
                heappush(new_set, (distance[node_key], node_key))
        nodes = new_set
    return distance, path
#utility function to reconstruct orginal path to find orignal weight
def reconstruct_orignal_path(paths, times, curr_node, branch_node, n):
    path = paths[curr_node]
    full_path = [False for i in range(n)]
    cost = 0
    while path[branch_node] != None:
        full_path[branch_node] = True
        cost += times[path[branch_node]][branch_node]
        branch_node = path[branch_node]
    return full_path, cost


def answer(times, time_limit):
    n = len(times[0])
    #return [] if there are no bunnies to carry
    if n <= 2: return []
    #add empty source
    temp_graph = create_empty_source(times, n)
    #check for negative cycle--> bellman_ford
    negative_cycle, distance, predecessor = simulate_bellman_ford(temp_graph, n)

    #if it has negative cycle the return[1:n-1]
    if negative_cycle: return [i-1 for i in range(1, n-1)]

    weighted_g = construct_orignal(temp_graph, distance, n)
    #print(weighted_g)
    distances = []
    paths = []

    for i in range(n):
        distance, path = simulate_dijkastra(weighted_g, i, n)
        distances.append(distance)
        paths.append(path)

    q = [{'curr_node': 0, 'distance': 0, 'finalised': [i == 0 or i == n-1 for i in range(n)]}]
    i = 0

    best_cost = neg_inf
    best_finalised = []

    #BFS
    while i != len(q):
        front = q[i]
        #print(front)
        curr_node = front['curr_node']

        new_items = []

        for j in range(1, n - 1):
            if not front['finalised'][j]:
                new_path, new_cost = reconstruct_orignal_path(paths, times, curr_node, j, n)
                finalised = [front['finalised'][k] or new_path[k] for k in range(n)]
                new_item = {'curr_node': j, 'distance': front['distance'] + new_cost, 'finalised': finalised}
                new_items.append(new_item)
        new_items.sort(key=lambda x: x['distance'])
        for item in new_items:
            q.append(item)

        new_path, new_cost = reconstruct_orignal_path(paths, times, curr_node, n - 1, n)
        finalised = [front['finalised'][k] or new_path[k] for k in range(n)]
        new_count = 0
        for j in finalised: 
            if j: new_count += 1

        if front['distance'] + new_cost <= time_limit and new_count > best_cost:
            best_finalised = finalised
            best_cost = new_count

        i += 1
    return [i - 1 for i in range(n) if i != 0 and i != n-1 and best_finalised[i]]

#given_times = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
#given_time_limit = 1
#print("ans",answer(given_times,given_time_limit))
