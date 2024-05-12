from collections import deque


def bfs(graph, root):
    visited = set()
    queue = deque([root])

    visited.add(root)

    while queue:
        next = queue.popleft()
        print(next)

        for neighbor in graph[next]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


if __name__ == "__main__":
    __graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }

    bfs(__graph, "A")
