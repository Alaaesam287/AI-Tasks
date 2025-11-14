def dfs(graph, start):
    visited = {node: False for node in graph}
    stack = [start]
    parent = {start: None} 

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            print(f"Path to {current}: {path}")

            for neighbor in graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    parent[neighbor] = current  
                    

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

dfs(graph, 0)
