import timeit as t
import time as v
import matplotlib.pyplot as plt

liste = []
m = "moha"
c = 5

print("taper le mot ",m," ",c,"fois aprés le signale dans :",end=" ")

for i in range(3,0,-1):
    print(i," seconde")
    v.sleep(1)

print("Go")

i=0
total =0
h=0

for i in range(c) : 
    
    start = t.default_timer()
    mot = input(" => ")
    end = t.default_timer()
    tee = end-start
    
    if mot != m :
        h +=1 
    
    liste.append(tee)
    total+=round(tee,5)
    print(total)


print("total : ",total)
print("with ",h," mistakes.")

X=range(1,6)
Y= liste

plt.plot(X,Y)
plt.show()