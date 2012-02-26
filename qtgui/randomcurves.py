from pylab import *

x = mgrid[0:200:2]

ion()


ll = []
for k in range(20):
    xx = random() * 200 + x[:-int(80*rand())]
    y = random()*200+100*sin(2*pi*rand() + xx/100 * (1+2*rand()) )
    ll.append(c_[xx,y])


ll= array(ll, dtype=object)


for l in ll:
    plot(l[:,0], l[:,1], 'r-')

savez('edges-%08d'%(int(sys.argv[1])), edges=ll)


axis('equal')

    



