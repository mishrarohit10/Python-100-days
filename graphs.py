class Graph:  
    def __init__(self):
        self.graph = dict()

    def addEdge(self,node1,node2,cost):
        # create an empty list for key node
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        
        # append neighbour to its corresponding node
        # graph[node1].append(node2)
        # graph[node2].append(node1)
        self.graph[node1].append((node2,int(cost)))
        # in case of undirected graph
        # self.graph[node2].append((node1,int(cost)))

    def printGraph(self):
        for key, value in self.graph.items():
            print(f"{key}-->{value}")

# addEdge('A', 'B')
# addEdge('A', 'C')
# addEdge('B', 'D')
# addEdge('B', 'E')
# addEdge('C', 'D')
# addEdge('D', 'A')
# addEdge('D', 'E')

# g = Graph()
# print("Enter nodes and edges")
# nodes, edges = input().split()

# for _ in range(int(edges)):
#     node1, node2, cost = input().split()
#     g.addEdge(node1,node2, cost)

# g.printGraph()


# def main():
#     g = Graph()

#     with open("input.txt") as f:
#         lines = f.readlines()

#     nodes, edges = lines[0].split()        

#     for i in range(1, len(lines)):
#         node1,node2,cost = lines[i].split()
#         g.addEdge(node1,node2,int(cost))
    
#     g.printGraph()

# if __name__=="__main__":
#     main()


def bfs(graph,source):
    visited = set() # to keep track of visited nodes
    bfs_traversal = list() # result list
    queue = list()

    queue.append(source)
    visited.add(source)

    # LOOP while queue is empty
    while queue:
        # pop the front and add it to bfs result
        curr = queue.pop(0)
        bfs_traversal.append(curr)

        # check neighbour of current node
        for neighbour in graph[curr]:
            # if neighbour not visited mark and add to bfs
            if neighbour not in visited:
                visited.add(neighbour)
                bfs_traversal.append(neighbour)
    return bfs_traversal


