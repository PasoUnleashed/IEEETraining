# a simple parser for python. use get_number() and get_word() to read
# https://csacademy.com/contest/archive/task/consecutive-subsequence/
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

n = get_number()
seq = []
for i in range(n):
    seq.append(get_number())
starts = [(0,seq[0])]
series = []
insquence = set()
while(len(starts)>0):
    start,startv = starts.pop(0)
    strt = start
    s = [start]
    for i in range(start+1,n):
        if(i in insquence):
            continue
        if(seq[i] == startv+1):
            s.append(i)
            insquence.add(i)
            start = i
            startv = seq[i]
        else:
            starts.append((i,seq[i]))
    if(len(s)>1):
        series.append((strt,s))
print(series)