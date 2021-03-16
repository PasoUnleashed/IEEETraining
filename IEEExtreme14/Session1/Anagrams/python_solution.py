
# a simple parse for python. use get_number() and get_word() to read
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


n = get_number()
d = dict()
for i in range(n):
    s = list(get_word())
    s.sort()
    s = "".join(s)
    if(s in d):
        d[s] +=1
    else:
        d[s] = 1
print(max(d.values()))