total=14763911
d=611322
r=8338996

k='%'

c=total-d-r
print(' Total :  %d  cas  =>  %.2f %s'%(total,total*100/total,k))
print(' conta :  %d  cas  =>  %.2f  %s'%(c,c*100.00/total,k))
print(' Recov :  %d   cas  =>  %.2f  %s'%(r,r*100.00/total,k))
print(' Death :  %d   cas  =>  %.2f   %s'%(d,d*100.00/total,k))
#(total-d-r)*100/total)


