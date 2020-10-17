import random
from my_utils import util
size = 7
class State:
    def __init__(self,parent = None):
        self.arr = [i+1 for i in range(size)]
        random.shuffle(self.arr)
        if(parent!=None):
            self.parent =parent
        else:
            self.parent = None
    def get_children(self):
        ret = []
        for i in range(size):
            for j in range(i+1,size):
                newarr = [self.arr[n] for n in range(size)]
                newarr[i],newarr[j] = newarr[j],newarr[i]
                newchild = State(parent=self)
                newchild.arr = newarr
                ret.append(newchild)
        return ret
    def is_goal(self):
        for i in range(size):
            if(self.arr[i]!=i+1):
                return False
        return True
    def heuristic(self):
        n =0
        for i in range(size):
            if(self.arr[i]!=i+1):
                n+=1
        return n
    def get_length(self):
        i = 0
        current = self.parent
        while current!=None:
            i+=1
            current = current.parent
        return i
    def __hash__(self):
        return hash(str(self.arr))
    def __eq__(self, other):
         return (
             self.__class__ == other.__class__ and
             self.__hash__()==other.__hash__() )
def bfs(state):
    seen = set()
    queue = [state]
    max_stack_size = 0
    min_length = float('inf')
    minpath = None
    while len(queue)>0:
        current = queue.pop(0)
        if(current.is_goal()):
            l = current.get_length()
            if(l<min_length):
                min_length = l
                minpath = current
        if(current in seen):
            continue
        #current.print_state()
        max_stack_size = max(len(queue),max_stack_size)
        seen.add(current)
        for i in current.get_children():
            if(not i in seen):
                queue.append(i)
        print('\r'+str(len(seen)).ljust(size),str(max_stack_size).ljust(10),end='')
    return minpath
def dfs(state):
    seen = set()
    stack = [state]
    max_stack_size = 0
    min_length = float('inf')
    minpath = None
    while len(stack)>0:
        current = stack.pop()
        if(current.is_goal()):
            l = current.get_length()
            if(l<min_length):
                min_length = l
                minpath = current
        if(current in seen):
            continue
        #current.print_state()
        max_stack_size = max(len(stack),max_stack_size)
        seen.add(current)
        for i in current.get_children():
            if(not i in seen):
                stack.append(i)
        print('\r'+str(len(seen)).ljust(size),str(max_stack_size).ljust(10),end='')
    return minpath
def ucs(state):
    queue = util.PriorityQueue(evaluator=lambda a,b: a[1]<b[1])
    queue.insert((state,0))
    seen = set()
    while(len(queue.queue)>0):
        current,distance = queue.delete()
        if(current in seen):
            continue
        seen.add(current)
        if(current.is_goal()):
            return current
        for i in current.get_children():
            queue.insert((i,distance+1))
def astar(state):
    queue = util.PriorityQueue(evaluator=lambda a,b: a[1]+a[0].heuristic()<b[1]+b[0].heuristic())
    queue.insert((state,0))
    seen = set()
    while(len(queue.queue)>0):
        current,distance = queue.delete()
        if(current in seen):
            continue
        seen.add(current)
        if(current.is_goal()):
            return current
        for i in current.get_children():
            queue.insert((i,distance+1))

s = State()
sw = util.StopWatch()
sw.start()
ucs(s)
print(sw.mesure_ms())
sw.start()
astar(s)
print(sw.mesure_ms())
