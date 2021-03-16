def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   
input_parser = parser()
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
def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

def manhattan(p1,p2):
    x1,y1= p1
    x2,y2 = p2
    return abs(x1-x2)+abs(y1-y2)

class Parameters:
    def __init__(self,As,Bs,Cs,At,Bt,Ct,Ak,Bk,Ck):
        self.As=As
        self.Bs=Bs
        self.Cs=Cs
        self.At=At
        self.Bt=Bt
        self.Ct=Ct
        self.Ak=Ak
        self.Bk=Bk
        self.Ck=Ck
    def get_stk(self,q):
        ni = ((self.As*q.previous.s)+(self.Bs*q.previous.previous.s)+(self.Cs))%(N)+1
        ti = ((self.At*q.previous.t)+(self.Bt*q.previous.previous.t)+(self.Ct))%(N)+1
        ki = ((self.Ak*q.previous.k)+(self.Bk*q.previous.previous.k)+(self.Ck))%(mk)
        del q.previous.previous
        return ni,ti,ki
N,q,sq,mk = get_number(),get_number(),get_number(),get_number()
points = []
for i in range(N):
    points.append((get_number(),get_number()))
parameters = Parameters(get_number(),get_number(),get_number(),get_number(),get_number(),get_number(),get_number(),get_number(),get_number())

class Query:
    def __init__(self,i=0,s=0,t=0,k=0,q=None,previous = None):
        self.previous = previous
        if(not (q is None)):
            self.i=previous.i+1
            self.s,self.t,self.k = parameters.get_stk(self)
        else:
            self.i=i
            self.s=s
            self.t=t
            self.k=k
queries = []


for i in range(sq):
    previous = None
    if(i>0):
        previous = queries[-1]
    if(i<sq):
        queries.append(Query(i,get_number(),get_number(),get_number(),q=None,previous=previous))    
    
class State:
    def __init__(self,start,target,query):
        self.query = query
        self.start = start
        self.target = target
        self.ppos = points[start-1]
        self.dist = 0
    def get_children(self):
        ret = []

        for i in points:
            if(i==self.ppos):
                continue
            d=manhattan(self.ppos,i)
 
            if((d-1)<=self.query.k):
                s = State(self.start,self.target,self.query)
                s.ppos = i
                s.dist=self.dist+d
                ret.append(s)
        return ret
    def get_heuristic(self):
        return manhattan(self.ppos,points[self.target-1])
results = []

def can_satisfy(query):
    state= State(query.s,query.t,query)
    queue = PriorityQueue(lambda a,b: a.dist+a.get_heuristic()<b.dist+b.get_heuristic())
    queue.insert(state)
    seen = set()

    while(len(queue.queue)>0):

        current = queue.delete()

        if(current.ppos in seen):
            continue
        else:
            seen.add(current.ppos)
        for i in current.get_children():
            if(i.ppos in seen):
                continue
            queue.insert(i)
        if(current.ppos == points[current.target-1]):
            return True
        
        
    return False
lq = queries[0]
for i in range(1,q+1):
    if(can_satisfy(lq)):
        results.append(1)
    else:
        results.append(0)

    if(i<sq):
        lq = queries[i]
    else:
        lq = Query(q=lq,previous=lq)
        

summ = 0
for i in range(len(results)):
    summ+= (results[i]* (2**(i+1)))
summ = summ % ((10**9)+7)


print(summ)