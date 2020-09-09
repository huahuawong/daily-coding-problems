# 4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.

# We can use either BFS or DFS for this problem. But we'll demonstrate BFS for this problem

def isReachable(self, s, d): 
      # Mark all the vertices as not visited 
      visited =[False]*(self.V) 

      # Create a queue for BFS 
      queue=[] 

      # Mark the source node as visited and enqueue it 
      queue.append(s) 
      visited[s] = True

      while queue: 

          #Dequeue a vertex from queue  
          n = queue.pop(0) 

          # If this adjacent node is the destination node, 
          # then return true 
           if n == d: 
               return True

          #  Else, continue to do BFS 
          for i in self.graph[n]: 
              if visited[i] == False: 
                  queue.append(i) 
                  visited[i] = True
       # If BFS is complete without visited d 
       return False
