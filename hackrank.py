def fizzBuzz(n):
    for i in range(n):
        if i % 2 == 0 :
            n.append(2)  
        else :
            n.append(1)
    return n      
if __name__ ==  '__main__':
    n = list (range(10000))
    fizzBuzz(n)
    