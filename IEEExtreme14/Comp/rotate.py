# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()
import copy
def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)
        
on,total = get_number(),get_number()
ons = set()
for i in range(on):
    ons.add(get_number())
if(total%2==1):
    print(total-1)
else:
    start = copy.deepcopy(ons)
    i = 1
    nons = set()
    for j in ons:
        nons.add((j+1)%total)
    del ons
    ons=nons
    
    while len(start&ons) != len(ons):
        nons = set()
        for j in ons:
            nons.add((j+1)%total)
        del ons
        ons=nons
        i+=1
    print(i-1)
                
    