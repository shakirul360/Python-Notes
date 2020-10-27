class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.edges = []
    
    def add_edge(self, edge):
        self.edges.append(edge)
    
class Graph:
    def __init__(self):
        self.nodes = []
        self.criticals = []
        self.edge_values = []
        
    def dfs_critcal_check(self):
        for main in self.connections:
            if main.visited == True:
                pass
            
    def critical_check(self):
        criticals = []
        for node in self.nodes:
            print("current candidate node:", node.value)
            critical_check = 0
            idx = self.nodes.index(node)
            self.nodes.remove(node)
            for edge in node.edges:
                found = False
                edge_value = edge.value
                print("current candidate edge:", edge_value)
                edge_idx = self.edge_values.index(edge_value)
                self.edge_values.remove(edge_value)
                print("Checking if", edge_value, "still in edge values list....")
                if edge_value in self.edge_values:
                    print(edge_value,"found")
                    found = True
                else:
                    print("incrementing to critical_check")
                    critical_check += 1
                self.edge_values.insert(edge_idx,edge_value)
            if critical_check >= 2:
                criticals.append(node.value)
            self.nodes.insert(idx, node)
            
        print(criticals, len(criticals))
    
graph = Graph()
names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen"]
conns = int(input())
for conn in range(conns):
    arr = list(input().split())
    main = arr.pop(0)
    if main == "0":
        break
    name = names[int(main)]
    name = Node(main)
    if name not in graph.nodes:
        graph.nodes.append(name)
        graph.edge_values.append(main)
    for c in arr:
        name = names[int(c)]
        name = Node(c)
        graph.nodes.append()
        head.add_edge(n)
        graph.edge_values.append(c)

graph.critical_check()
