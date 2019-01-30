''' class Graph defines the bfs and dfs functions that operate on the graph  '''
from collections import deque

class Graph:
    
    def __init__(self, adj):
        n = len(adj)
        self.graph = dict()
        for i in range(n):
            temp = []
            for j in range(n):
                if adj[i][j]:
                    temp.append(j)
            self.graph[i] = set(temp)

    def bfs_paths(self, start, goal):
        '''
        Generate and return any path from start to goal using breadth-first search 
        Input : start node, goal node
        Output : list of nodes from to be traversed to reach from start to goal(the first node in this list will be the start node and 
        the last node will be the goal node)
        '''
        #BEGIN YOUR CODE HERE
        visited_node={}
        '''for n in range(len(self.graph)):
            print(n)
            print("-->")
            for adj in self.graph[n]:
                print(adj)
            print("\n")'''    
        for nodes in range(len(self.graph)):
            visited_node[nodes]=False
    
        path=[]
        parent={}
        parent[start]=-1
        l_queue=deque([])
        visited_node[start]=True
        l_queue.append(start)
        while( l_queue):
            cur=l_queue.popleft()
            #print(cur)
            if cur==goal:
                break
            for items in self.graph[cur]:
                if not(visited_node[items]):
                    parent[items]=cur
                    visited_node[items]=True
                    l_queue.append(items)
                    
        path.append(goal)
        p=parent[goal]
        while(p!=-1):
            path.append(p)
            p=parent[p]
        path=path[::-1]    
        '''for i in path:
            print(i)'''   
        return path    
        
            
          
        #END YOUR CODE HERE


 
    def dfs_paths(self, start, goal):
        '''
        Generate and return any path from start to goal using depth-first search
        Input : start node, goal node
        Output : list of nodes from to be traversed to reach from start to goal(the first node in this list will be the start node and  
        the last node will be the goal node)
        '''
        #BEGIN YOUR CODE HERE
        visited_node={}
        '''print("DFS")
        
        for n in range(len(self.graph)):
            print(n)
            print("-->")
            for adj in self.graph[n]:
                print(adj)
            print("\n")'''
        for nodes in range(len(self.graph)):
            visited_node[nodes]=False
            
            
            
        path=[]
        l_stack=[]
        parent = {}
        parent[start]=-1
        l_stack.append(start)
        while( l_stack):
            cur=l_stack.pop()
            if(not visited_node[cur]):
                visited_node[cur]=True
                if(cur==goal):
                    break
               
            for items in self.graph[cur]:
                if (not visited_node[items]):
                    parent[items]=cur
                    l_stack.append(items)         
               
        path.append(goal)
        p=parent[goal]
        while(p!=-1):
            path.append(p)
            p=parent[p]
        path=path[::-1]    
        '''for i in path:
            print(i)'''
        return path
        
        #END YOUR CODE HERE
