import heapq

def dijkstra(graph, source):
    # Initialize distance dictionary
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    
    # Initialize previous node dictionary
    prev = {node: None for node in graph}
    
    # Priority queue to hold nodes with their distances
    priority_queue = []
    heapq.heappush(priority_queue, (0, source))
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If current distance is greater than already known distance, skip
        if current_distance > dist[current_node]:
            continue
        
        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If found shorter path to neighbor, update and push to priority queue
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return dist, prev

def reconstruct_shortest_path(prev, target):
    path = []
    step = target
    
    # Backtrack from target to source using prev dictionary
    while step is not None:
        path.append(step)
        step = prev[step]
    
    # Reverse path to get source to target path
    return path[::-1]

# Example usage:
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 3, 'B': 1, 'D': 2},
    'D': {'B': 3, 'C': 2}
}

source_node = 'A'
target_node = 'D'

# Run Dijkstra's algorithm
shortest_distances, previous_nodes = dijkstra(graph, source_node)

# Reconstruct the shortest path from source to target
shortest_path = reconstruct_shortest_path(previous_nodes, target_node)

print("Shortest distances:", shortest_distances)
print("Shortest path from", source_node, "to", target_node, ":", shortest_path)
