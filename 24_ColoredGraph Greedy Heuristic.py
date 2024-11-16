colors = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

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


node_colors = {}
for node in graph:
    node_colors[node] = "none"

for node in graph:
    colors_to_chose = colors.copy()
    for adjacent in graph[node]:
        color = node_colors[adjacent]
        if  color != "none" and color in colors_to_chose:
            colors_to_chose.remove(node_colors[adjacent])
    node_colors[node] = colors_to_chose[0]
    print(node_colors[node])
       



# Print the colors assigned to each node
for node in node_colors:
    print(node, node_colors[node])


