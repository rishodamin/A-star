from collections import deque
from node import Node
import time

def hrstc(p,g):
    return abs(p[0]-g[0])+abs(p[1]-g[1])
        
class FindPath:
    def __init__(self, maze): 
        self.maze = maze        
        self.row = len(maze)
        self.col = len(maze[0])    
        self.path_history = deque()

    def find_path(self,start,goal):
        stack = {}
        root = Node(start,0,hrstc(start,goal))
        looked = set()          
        stack[start] = root
        while stack :
            min_path = min(stack.values(),key=lambda x:x.glob)
            paths = []
            for i in stack.values():
                if i.glob==min_path.glob:
                    paths.append(i)
            path = max(paths,key=lambda x:x.loc)
            curr = path.data
            looked.add(curr)
            del stack[curr]
            if curr == goal:
                while True:
                    if self.path_history[-1]==goal:
                        del self.path_history[-1]
                        break
                    del self.path_history[-1]
                break
            if curr[0]+1<self.row and not self.maze[curr[0]+1][curr[1]] and not (curr[0]+1,curr[1])  in looked :
                if not (curr[0]+1,curr[1]) in stack:
                    stack[(curr[0]+1,curr[1])] = Node((curr[0]+1,curr[1]))
                    self.path_history.append((curr[0]+1,curr[1]))
                if path.loc+1<stack[(curr[0]+1,curr[1])].loc:
                    stack[(curr[0]+1,curr[1])].loc = path.loc+1
                    stack[(curr[0]+1,curr[1])].glob = path.loc+1+hrstc((curr[0]+1,curr[1]),goal)
                    stack[(curr[0]+1,curr[1])].prnt = path
            if curr[0]-1>=0 and not self.maze[curr[0]-1][curr[1]]  and not (curr[0]-1,curr[1])  in looked :
                if not (curr[0]-1,curr[1]) in stack:
                    stack[(curr[0]-1,curr[1])] = Node((curr[0]-1,curr[1]))
                    self.path_history.append((curr[0]-1,curr[1]))
                if path.loc+1<stack[(curr[0]-1,curr[1])].loc:
                    stack[(curr[0]-1,curr[1])].loc = path.loc+1
                    stack[(curr[0]-1,curr[1])].glob = path.loc+1+hrstc((curr[0]-1,curr[1]),goal)
                    stack[(curr[0]-1,curr[1])].prnt = path
            if curr[1]-1>=0 and not self.maze[curr[0]][curr[1]-1] and not (curr[0],curr[1]-1)  in looked :
                if not (curr[0],curr[1]-1) in stack:
                    stack[(curr[0],curr[1]-1)] = Node((curr[0],curr[1]-1))
                    self.path_history.append((curr[0],curr[1]-1))
                if path.loc+1<stack[(curr[0],curr[1]-1)].loc:
                    stack[(curr[0],curr[1]-1)].loc = path.loc+1
                    stack[(curr[0],curr[1]-1)].glob = path.loc+1+hrstc((curr[0],curr[1]-1),goal)
                    stack[(curr[0],curr[1]-1)].prnt = path
            if curr[1]+1<self.col and not self.maze[curr[0]][curr[1]+1] and not (curr[0],curr[1]+1)  in looked :
                if not (curr[0],curr[1]+1) in stack:
                    stack[(curr[0],curr[1]+1)] = Node((curr[0],curr[1]+1))
                    self.path_history.append((curr[0],curr[1]+1))
                if path.loc+1<stack[(curr[0],curr[1]+1)].loc:
                    stack[(curr[0],curr[1]+1)].loc = path.loc+1
                    stack[(curr[0],curr[1]+1)].glob = path.loc+1+hrstc((curr[0],curr[1]+1),goal)
                    stack[(curr[0],curr[1]+1)].prnt = path
        route = []
        while path:
            route.append(path.data)
            path = path.prnt
        return route


