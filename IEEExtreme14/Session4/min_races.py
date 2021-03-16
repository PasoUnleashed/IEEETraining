# a simple parser for python. use get_number() and get_word() to read
# https://csacademy.com/contest/archive/task/min-races/
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
k = get_number()
racers = []
for i in range(n):
    classs = get_number()
    pos = get_number()
    racers.append((classs,pos))
racers = sorted(racers,key=lambda x:-x[1])
beaters = dict()
for i in range(n):
    beaters[racers[i]] = set()
    for j in range(i+1,n):
        if(racers[j][0]>=racers[i][0]):
            beaters[racers[i]].add(racers[j])
count = 0
print(beaters)
while(True):
    count+=1
    beat = False
    rem = set()
    for i in list(beaters.keys()):
        ibeat = False
        if(len(beaters[i])==0):
            ibeat = True
            for j in beaters:
                 if i in beaters[j]:
                    beat = True
                    beaters[j].remove(i)
        if(ibeat):
            del beaters[i]
    if(not beat):
        break
print(count)
