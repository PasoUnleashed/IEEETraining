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

# numpy and scipy are available for use
import numpy
import scipy

node_count = get_number()
edge_count = get_number()
# Start, Alex, Ben
s,a,b = get_number()-1,get_number()-1,get_number()-1

nodes = [[] for i in range(node_count)]
for i in range(edge_count):
    start,end = get_number(),get_number()
    nodes[start-1].append(end-1)
    nodes[end-1].append(start-1)

class Node:
    def __init__(self,id_,previous,dist):
        self.id = id_
        self.previous = previous
        self.dist = dist
    def get_path(self):
        l = [self.id]
        current = self.previous
        while not current is None:
            l.append(current.id)
            current = current.previous
        return list(reversed(l))
queue = [Node(s,None,0)]
seen = set()
a_paths = []
b_paths = []
min_a = float('inf')
min_b = float('inf')
while len(queue)>0:
    current = queue.pop(0)
    seen.add(current.id)
    if(current.id == a and current.dist<=min_a):
        a_paths.append(current.get_path())
        min_a = min(min_a,current.dist)
    if(current.id == b and current.dist<=min_b):
        b_paths.append(current.get_path())
        min_b = min(min_b,current.dist)
    for i in nodes[current.id]:
        if(i in seen):
            continue
        queue.append(Node(i,current,current.dist+1))

def match(path_a,path_b):
    count = 0
    for i in range(min(len(path_a),len(path_b))-1):
        if(path_a[i]==path_b[i] and path_a[i+1] == path_b[i+1]):
            count+=1
    print(count,"\n",path_a,"\n",path_b)
    return count
max_together =0
for i in range(len(a_paths)):
    for j in range(len(b_paths)):
        max_together = max(max_together,match(a_paths[i],b_paths[j]))
print(max_together)