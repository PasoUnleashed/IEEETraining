# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

class PriorityQueue(object): 
    def __init__(self,evaluator = lambda a,b : a>b): 
        self.queue = [] 
        self.evaluator = evaluator
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == 0
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def delete(self): 
        try: 
            max_element = 0
            for i in range(len(self.queue)): 
                if self.evaluator(self.queue[i] , self.queue[max_element]): 
                    max_element = i 
            item = self.queue[max_element] 
            del self.queue[max_element] 
            return item 
        except IndexError: 
            print() 

            exit() 


# numpy and scipy are available for use
import numpy as np
import random
import copy
def range2d(x,y):
    for i in range(x):
        for j in range(y):
            yield i,j
def get_adj(x,y,size):
    ret = []
    for i in range(-1,2):
        for j in range(-1,2):
            if((i==0 and  j!=0) or (j==0 and i!=0)):
                    if(x+i<size and x+i >=0 and y+j < size and y+j>=0):
                        ret.append((x+i,y+j))
    return ret
class Board:
    def __init__(self,size):
        self.board = [[0 for i in range(size)] for j in range(size)]
        self.shape = 1
        self.current_count = 0
        self.size= size
        self.dist = 0
        self.starts = [(0,0)]
    def get_adj_tiles(self,x,y):
        adj_tiles= [self.board[i][j] for i,j in get_adj(x,y,self.size)]
        return adj_tiles
    def get_surround(self,x,y):
        queue = []
        ret = set()
        seed= self.board[x][y]
        seen = set()
        while(len(queue)>0):
            x,y = queue.pop()
            if((x,y)in seen):
                    continue
            else:
                seen.add((x,y))
            adj = get_adj(x,y,self.size)
            for i,j in adj:
                
                if(self.board[i][j]==seed):
                    ret.add((i,j))
                    queue.append((i,j))
        return ret
    def get_children(self):
        ret =[]

        for x,y in self.starts:
            if(self.board[x][y]==0):
                if(self.current_count==0 or self.shape in self.get_adj_tiles(x,y)):
                    nbo = Board(self.size)
                    nbo.shape =self.shape
                    nbo.current_count=self.current_count
                    nbo.board= copy.deepcopy(self.board)
                    nbo.board[x][y] = nbo.shape
                    nbo.current_count+=1
                    nbo.starts = nbo.get_free_adj(x,y)
                    if(nbo.current_count==self.size):
                        nbo.shape+=1
                        nbo.current_count = 0
                   
                        for i in self.get_surround(x,y):
                            nbo.starts+=nbo.get_free_adj(*i)
                    random.shuffle(nbo.starts)
                    nbo.dist= self.dist+1
                    ret.append(nbo)

        #random.shuffle(ret)
        return ret
    def print(self):
        for i in range(self.size):
            p = ""
            for j in range(self.size):
                p+=str(self.board[i][j])
            end = '\n'
            if(i<self.size-1):
                end='\n'
            print(p,end=end)
    def __str__(self):
        t=""
        for i in range(self.size):
            p = ""
            for j in range(self.size):
                p+=str(self.board[i][j])
            end = ''
            if(i<self.size-1):
                end='\n'
            t+=p+end
        return t
    def get_free_adj(self,x,y):
        ret = get_adj(x,y,self.size)
        ret2 = []
        for i,j in ret:
            if(self.board[i][j]==0):
                ret2.append((i,j))
        return ret2
    def is_goal(self):
        return self.shape == self.size+1 or self.shape == self.size and self.current_count==self.size
    def get_heuristic(self):
        total =0
        max_zer = 0
        regions = 0
        zeros = set() 
        for x,y in range2d(self.size,self.size):
            if(self.board[x][y] == 0):
                total+=1
                if((x,y) not in zeros):
                    regions+=1
                    s=self.get_surround(x,y)
                    zeros = zeros.union(s)
                    max_zer = max(max_zer,len(s))
        return self.dist+(total+regions)-max_zer
    
            
def solve(board):
    queue = PriorityQueue(lambda a,b: a.get_heuristic()<b.get_heuristic())
    queue.insert(board)
    current = board
    seen =set()
    while(current.current_count!=current.size or current.shape != current.size):
        current = queue.delete()
        if(str(current)in seen):
            continue
        else:
            seen.add(str(current))
        if(current.is_goal()):
            return current
        for i in current.get_children():
            queue.insert(i)
    return current    
cases = get_number()
for i in range(cases):
    b = Board(get_number())
    b = solve(b)
    b.print()