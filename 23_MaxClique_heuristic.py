from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus, LpBinary

graph = {
    0: [2, 6, 9],
    1: [4, 5, 9],
    2: [0, 9, 10],
    3: [4, 6, 7, 8, 9, 10],
    4: [1, 3, 5, 6, 7, 8, 9],
    5: [4, 6, 8, 10],
    6: [0, 1, 3, 4, 5],
    7: [3, 4, 9],
    8: [3, 4, 5],
    9: [0, 1, 2, 3, 4, 7],
    10: [2, 3, 5]
}

Clique = []


node_degrees = {node: len(neighbors) for node, neighbors in graph.items()}
ordered_graph_grade = sorted(graph.keys(), key=lambda x: node_degrees[x], reverse=True)

# Start by adding the node with the highest degree to the Clique
Clique.append(ordered_graph_grade[0])
ordered_graph_grade.remove(ordered_graph_grade[0])

# Calculate the next node to add to the clique, the one with the most edges to the already present nodes
while len(ordered_graph_grade) > 0:
    next_node = None
    for node in ordered_graph_grade:

        is_connected_to_all = all(clique_node in graph[node] for clique_node in Clique)
        if is_connected_to_all:
            next_node = node
            break  


    if next_node is None:
        break

    # Add the node to the Clique and remove it from the ordered list
    Clique.append(next_node)
    ordered_graph_grade.remove(next_node)


print(Clique)
