def dfs(graph, root, visited=None):
    if None is visited:
        visited = set()

    visited.add(root)

    for next in set(graph[root]) - visited:
        dfs(graph, next, visited)

    return visited

def dfs2(visited, graph, root): 
    if root not in visited: 
        visited.add(root)

    for next in graph[root]:
        dfs2(visited,graph,next)



if __name__ == "__main__":
    __graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }

    visited = set()
    dfs2(visited,__graph, "A")
    print(visited)
