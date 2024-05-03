def read_graph(file_name):
    graph = {}
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            graph[parts[0]] = parts[1:]
    return graph

def dfs_recursive(graph, stack, visited=None):
    if visited is None:
        visited = []
    if not stack:
        return
    vertex=stack.pop()
    visited.append(vertex)
    print(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited and neighbor not in stack:
            stack.append(neighbor)
    
    dfs_recursive(graph, stack, visited)

def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = []
    if not queue:
        return
    vertex = queue.pop(0)
    visited.append(vertex)
    print(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)

    bfs_recursive(graph, queue, visited)

graph = read_graph('graph.txt')
print("DFS starting from node 'A':")
dfs_recursive(graph, ['0'])
print("BFS starting from node 'A':")
bfs_recursive(graph, ['0'])
/*
0 1 2 
1 3 0
2 0 4 
3 1 5
4 2 5 
5 3 4
*/