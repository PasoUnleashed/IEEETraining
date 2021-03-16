from my_utils import games , xo


def dfs(state):
    seen = set()
    stack = [state]
    max_stack_size = 0
    while len(stack)>0:
        current = stack.pop()
        if(current.evaluate_status()!=None):
            print('Found end state',current.evaluate_status().signal,current.evaluate_status().players)
            current.print_state()
            
        if(current in seen):
            continue
        #current.print_state()
        max_stack_size = max(len(stack),max_stack_size)
        seen.add(current)
        for i in current.get_children():
            if(not i in seen):
                stack.append(i)
        print(str(len(seen)).ljust(6),str(max_stack_size).ljust(10),end='\r')
        
def bfs(state):
    seen = set()
    queue = [state]
    max_stack_size = 0
    while len(queue)>0:
        current = queue.pop(0)
        if(current.evaluate_status()!=None):
            print('Found end state',current.evaluate_status().signal,current.evaluate_status().players)
            current.print_state()
            input()
        if(current in seen):
            continue
        #current.print_state()
        max_stack_size = max(len(queue),max_stack_size)
        seen.add(current)
        for i in current.get_children():
            if(not i in seen):
                queue.append(i)
        print('\r'+str(len(seen)).ljust(6),str(max_stack_size).ljust(10),end='')
s = xo.XOState(3)
bfs(s)
print()