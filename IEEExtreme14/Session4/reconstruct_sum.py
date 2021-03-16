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

a = get_number()
mask = [get_number() for i in range(len(str(a))-1)]

def get_splits(number):
    for i in range(number+1):
        yield number-i,i

def decimal_addition(a,b):
    a = list(reversed(str(a)))
    b = list(reversed(str(b)))
    r = []
    cr = []
    print(a)
    print(b)
    carry = 0
    for i in range(max(len(a),len(b))):
        if(i<min(len(a),len(b))):
            da = int(a[i])
            db = int(b[i])
            dr = da+db+(carry)
            if(dr>=10):
                carry = 1
                dr = dr-10
            else:    
                carry = 0
            cr.append(carry)
            r.append(dr)
        elif(i<len(a)):
            r.append(int(a[i])+(carry))
            cr.append(carry)
            carry = 0
        elif(i<len(b)):
            r.append(int(b[i])+(carry))
            cr.append(carry)
            carry = 0
    return r,cr
print(decimal_addition(999,1))