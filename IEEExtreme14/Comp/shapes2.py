# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()
import random
def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
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
def get_adj_tiles(self,x,y):
        adj_tiles= [self.board[i][j] for i,j in get_adj(x,y,self.size)]
        return adj_tiles
class Board:
    def __init__(self,size):
        self.board = [[0 for i in range(size)] for j in range(size)]
        places = [(i,j) for i,j in range2d(size,size)]
        self.pieces = [[places.pop(random.randint(0,len(places)-1))] for i in range(size)]
        for i in range(len(self.pieces)):
            for x,y in self.pieces[i]:
                self.board[x][y]=i+1
        self.current = 0
        self.size=size
    def get_adj_tiles(self,x,y):
        adj_tiles= [self.board[i][j] for i,j in get_adj(x,y,self.size)]
        return adj_tiles
    def get_free_adj(self,x,y):
        ret = get_adj(x,y,self.size)
        ret2 = []
        for i,j in ret:
            if(self.board[i][j]==0):
                ret2.append((i,j))
        return ret2
    def shuffle_0(self):
            x,y = random.randint(0,self.size-1),random.randint(0,self.size-1)
            if(self.board[x][y]==self.board[x][y]):
                adj = sorted(self.get_adj_tiles(x,y))
                max_count=0
                max_element =0
                for i in adj:
                    if(adj.count(i)>max_count):
                        max_count = adj.count(i)
                        max_element = i
                if(max_count>=2):
                    adj = get_adj(x,y,self.size)
                    for i,j in adj:
                        if(self.board[i][j] == max_element):
                            self.board[i][j]=0
                            self.board[x][y]=max_element
                            return    
                     
    def create(self):
        placed = 0
        shape =0
        while(placed<self.size**2):
            if(placed >= self.size):
                placed=0
                shape+=1
            choices = set()
            for i in self.pieces[shape]:
                for j in self.get_free_adj(i[0],i[1]):
                    choices.add(j)
            if(len(choices)==0):
                continue
            else:
                choice = random.choice(list(choices))
                self.pieces[shape].append(choice)
                self.board[choice[0]][choice[1]]=shape+1
                placed+=1
            print(placed)
            self.print()
            
    def print(self):
        for j in range(self.size):
            p = ""
            for i in range(self.size):
                p+=str(self.board[i][(self.size-1)-j])
            print(p)

b= Board(5)
b.create()
b.print()