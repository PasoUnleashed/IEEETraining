import random
with open('data1.txt','w') as f:
    T = random.randint(1,10)
    f.write(str(T)+'\n')
    for i in range(T):
        N = random.randint(1,10)
        f.write(str(N)+'\n')
        for j in range(N):
            x = 1
            if(random.randint(0,100)<=50):
                x=-1
            end = '\n'
            if(j==N-1 and i == T-1):
                end = ''
            f.write(str(random.randint(-100,100))+" "+str(random.randint(-100,100))+" "+str(x)+end)
