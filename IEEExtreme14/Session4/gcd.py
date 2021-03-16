x,y = 5002,2002

while y>0:
    x,y = y,x%y
    
print(x)