"""
search.py: Search algorithms on grid.
"""
import operator
import heapq
from collections import deque

def heuristic(a, b):
    """
    Calculate the heuristic distance between two points.

    For a grid with only up/down/left/right movements, a
    good heuristic is manhattan distance.
    """

    # BEGIN HERE #
    dist=(abs(a[0]-b[0])+abs(a[1]-b[1]))
    

    return dist

    # END HERE #


def searchHillClimbing(graph, start, goal):
    """
    Perform hill climbing search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None
    l_stack=[]
    if start==goal:
        came_from[goal]=start
        return came_from
    visited={}
    for x in range(graph.width):
        for y in range(graph.height):
            if graph.isOOB((x,y)):
                visited[(x,y)]=True
            else:
                visited[(x,y)]=False
    '''for items in visited:
        print(visited[items])'''
    #came_from[start]=start
    l_stack.append(start)
    #visited[start]=True
    parent={}
    parent[start]=start
    while(l_stack):
        cur=l_stack.pop()
        #print (cur)
        #visited[cur]=True
        came_from[cur]=parent[cur]
        if cur==goal:
            break
        neighbors=graph.neighboursOf(cur)
        distances={}
        for n in neighbors:
            distances[n]=heuristic(n,goal)
        sorted_neighbors = sorted(distances.items(), key=operator.itemgetter(1))
        for ((x,y),z) in reversed(sorted_neighbors):
            item=(x,y)
            #print(visited[item])
            if (not(visited[item])):
                parent[item]=cur
                visited[cur]=True
                l_stack.append(item)
                #print(item)           
    
    
    '''for i in came_from:
        print(i+came_from[i])
    # BEGIN HERE #
    print("goal: ",goal)
    print("start:",start)
    #print("goal_parent:",came_from[goal])'''
    path={}
    current=goal
    while(current!=start):
        path[current]=came_from[current]
        current=came_from[current]

    # END HERE #

    return path


def searchBestFirst(graph, start, goal):
    """
    Perform best first search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """


    # Initialise the came_from dictionary
    came_from = {}
    came_from[start] = None
    heap=[]
    if start==goal:
        came_from[goal]=start
        return came_from
    visited={}
    s_dist=heuristic(start,goal)
    heapq.heappush(heap, (s_dist, start))


    # BEGIN HERE #
    for x in range(graph.width):
        for y in range(graph.height):
            if graph.isOOB((x,y)):
                visited[(x,y)]=True
            else:
                visited[(x,y)]=False
    parent={}
    parent[start]=start
    while(heap):
        (z,(x,y))=heapq.heappop(heap)
        cur=(x,y)
        #print(cur)
        #visited[cur]=True
        came_from[cur]=parent[cur]
        if cur==goal:
            break
        neighbors=graph.neighboursOf(cur)
        for n in neighbors:
            parent[n]=cur
            if(not(visited[n])):
                visited[cur]=True
                #parent[n]=cur
                dist=heuristic(n,goal)
                heapq.heappush(heap, (dist, n))        
            

    # END HERE #
    path={}
    current=goal
    while(current!=start):
        path[current]=came_from[current]
        current=came_from[current]

    return path

    #return came_from



def searchBeam(graph, start, goal, beam_length=3):
    """
    Perform beam search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    came_from = {}
    visited={}
    if start==goal:
        came_from[goal]=start
        return came_from
    #came_from[start] = None
    for x in range(graph.width):
        for y in range(graph.height):
            if graph.isOOB((x,y)):
                visited[(x,y)]=True
            else:
                visited[(x,y)]=False

    # BEGIN HERE #
    q=deque([])
    q.append(start)
    parent={}
    parent[start]=start
    while(q):
        cur=q.popleft()
        #visited[cur]=True
        came_from[cur]=parent[cur]
        if cur==goal:
            break
        neighbors=graph.neighboursOf(cur)
        distances={}
        for n in neighbors:
            q.append(n)
        for n in q:
            distances[n]=heuristic(n,goal)
        sorted_neighbors=sorted(distances.items(),key=operator.itemgetter(1))
        i=0
        q=deque([])
        for((x,y),z) in sorted_neighbors:
            item=(x,y)
            if (not(visited[item]) and i<=beam_length):
                visited[cur]=True
                parent[item]=cur
                q.append(item)
                i=i+1
       
            
    path={}
    current=goal
    while(current!=start):
        path[current]=came_from[current]
        current=came_from[current]

    # END HERE #

    return path

    #return came_from


def searchAStar(graph, start, goal):
    """
    Perform A* search on the graph.

    Find the path from start to goal.

    @graph: The graph to search on.
    @start: Start state.
    @goal: Goal state.

    returns: A dictionary which has the information of the path taken.
             Ex. if your path contains and edge from A to B, then in
             that dictionary, d[B] = A. This means that by checking
             d[goal], we obtain the node just before the goal and so on.

             We have called this dictionary, the "came_from" dictionary.
    """

    # Initialise the came_from dictionary
    '''came_from={}
    heap=[]
    visited={}
    str_dist={}
    str_dist[start]=0
    s_dist=heuristic(start,goal)+str_dist[start]
    heapq.heappush(heap, (s_dist, start))
    
    for x in range(graph.width):
        for y in range(graph.height):
            if graph.isOOB((x,y)):
                visited[(x,y)]=True
            else:
                visited[(x,y)]=False
    previous=(-1,-1)
    while(heap):
        (z,(x,y))=heapq.heappop(heap)
        cur=(x,y)
        #print(cur)
        visited[cur]=True
        came_from[cur]=previous
        if cur==goal:
            break
        neighbors=graph.neighboursOf(cur)
        for n in neighbors:
            if(not(visited[n])):
                str_dist[n]=str_dist[cur]+1
                dist=heuristic(n,goal)+str_dist[n]
                heapq.heappush(heap, (dist, n))
        previous=cur'''        
   
    # BEGIN HERE #
    came_from = {}
    came_from[start] = None
    visited_node={}
    visited_node[start]=1
    parent={}
    parent[start]=None
    if(start==goal):
        return came_from
    cur=start
    m_list={}
    dist={}
    dist[start]=0
    m_list[start]=heuristic(start,goal)+dist[start]
    while(1):
        if(len(graph.neighboursOf(cur))!=0):
            l=[]
            del m_list[cur]
            l=graph.neighboursOf(cur)
            for i in l:
                if i not in visited_node:
                    dist[i]=dist[cur]+1
                    visited_node[i]=1
                    parent[i]=cur
                    m_list[i]=heuristic(i,goal)+dist[i]
            s={}   
            s = [(k, m_list[k]) for k in sorted(m_list, key=m_list.get, reverse=False)]
            m_list={}
            c=0
            for i in s:
                if(c==0):
                    cur=i[0]
                    c=1
                m_list[i[0]]=i[1]

            came_from[cur]=parent[cur]
            if(cur==goal):
                break
                return came_from
        else:
            del m_list[cur]
            s={}
            s = [(k, m_list[k]) for k in sorted(m_list, key=m_list.get, reverse=False)]
            
            m_list={}
            c=0
            for i in s:
                if(c==0):
                    cur=s[0]
                    c=1
                m_list[i[0]]=i[1]   
            came_from[cur]=parent[cur]
            if(cur==goal):
                break
                return came_from
    current=goal
    path={}
    while(current!=start):
        path[current]=came_from[current]
        current=came_from[current]
    return path    

    # END HERE #

    return came_from

