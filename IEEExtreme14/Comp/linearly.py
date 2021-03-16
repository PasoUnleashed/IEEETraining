# a simple parser for python. use get_number() and get_word() to read
def parser():
    with open('data1.txt','r') as f:
        while 1:
            data = list(f.readline().split(' '))
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



def side(x,y,slope):
    if y < x*slope:
        return -1
    elif y > x*slope:
        return 1
    else:
        return 0

def test_slope(points,slope,desired_side):
    if desired_side is None:
        return True
    for x,y in points:
        r = side(x,y,slope)
        if(r!=0 and r!=desired_side):
            return False
    return True
def test_case():
    
    size = get_number()

    onpoints = []
    offpoints = []
    for n in range(size):
        try:
            x,y,s = get_number(),get_number(),get_number()
        except:
            x,y,s = 0,0,0
        if(s<0):
            onpoints.append((x,y))
        else:
            offpoints.append((x,y))
    
    slo = -80,80
    add = 1
    steps = int((slo[1]-slo[0])//add)
    steps += 36/(add/20)
    steps = int(steps)
    cslo = slo[0]
    def pickone(pnts,sl):
        if(not pnts):
            return None
        i=0
        o = side(pnts[i][0],pnts[i][1],sl)
        for i in pnts:
            if(o==0):
                o = side(i[0],i[1],sl)
            else:
                return o
        return o
    for j in range(steps):
        
        onside = pickone(onpoints,cslo)
        offside = pickone(offpoints,cslo)
        if(offside == onside and offside!=0):
            continue
        if(test_slope(onpoints,cslo,onside) and test_slope(offpoints,cslo,offside)):
            pass
            #return True
        if(abs(cslo)<18):
            cslo+=(add/20)
        else:
            cslo+=add
        print(cslo)
    return False

a = get_number()
r = ""
for i in range(a):
    if(test_case()):
        r+='YES\n'
    else:
        r+='NO\n'
print(r)
    
    