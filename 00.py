graph = dict()

graph["A"] = ["B", "C"]
graph["B"] = ["A", "D"]
graph["C"] = ["A", "G", "H", "I"]
graph["D"] = ["B", "E", "F"]
graph["E"] = ["D"]
graph["F"] = ["D"]
graph["G"] = ["C"]
graph["H"] = ["C"]
graph["I"] = ["C", "J"]
graph["J"] = ["I"]


def dfs(graph, start, visited=[]):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

    return visited


print(dfs(graph, "A"))
