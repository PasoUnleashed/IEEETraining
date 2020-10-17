# a simple parser for python. use get_number() and get_word() to read
# https://csacademy.com/contest/archive/task/shoe-pairs/
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

N = get_number()
ls = [0 for i in range(100)]
rs = [0 for i in range(100)]

for i in range(N):
    size = get_number()
    side = get_word()
    if(side == 'L'):
        ls[size-1] +=1
    else:
        rs[size-1] +=1
        
pairs = 0
for i in range(100):
    pairs+=min(ls[i],rs[i])
print(pairs)