import heapq
import sys
 
class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
    
    def shortest_path(self, start, finish):
        distance = {} 
        previous = {}
        node = [] 
        
        for item in self.vertices: 
          if item == start:
            distance[item] = 0 
          else: 
            distance[item] = sys.maxsize 
          heapq.heappush(node, [distance[item],item])
          previous[item] = None 
        

        while node: 
          smallest = heapq.heappop(node)[1]
          if smallest == finish: 
            path = []
            while previous[smallest]:
              path.append(smallest)
              smallest = previous[smallest]
            path.append(smallest)
            path.reverse()
            return path 
          
          if distance[smallest] == sys.maxsize:
            break 
          
          for neighbor in self.vertices[smallest]:
            temp = self.vertices[smallest][neighbor] + distance[smallest]
            if temp < distance[neighbor]: 
              previous[neighbor] = smallest
              distance[neighbor] = temp
              for idx in node: 
                if idx[1] == neighbor:
                  idx[0] = temp
              heapq.heapify(node)
                
        return distance
                
          
        
    def __str__(self):
        return str(self.vertices)
        
g = Graph()
g.add_vertex('A', {'B': 7, 'C': 8})
g.add_vertex('B', {'A': 7, 'F': 2})
g.add_vertex('C', {'A': 8, 'F': 6, 'G': 4})
g.add_vertex('D', {'F': 8})
g.add_vertex('E', {'H': 1})
g.add_vertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
g.add_vertex('G', {'C': 4, 'F': 9})
g.add_vertex('H', {'E': 1, 'F': 3})
print(g.shortest_path('A', 'H'))
