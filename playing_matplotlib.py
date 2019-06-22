import numpy as np     #use numpy for whenever you dealing with arrays
import matplotlib.pyplot as plt



#drawing graphs

#drawing cos graph

#x = np.linspace(0,4*np.pi,100)
#y = np.cos(x)

#plt.plot(x,y)
#plt.title('cos graph')
#plt.xlabel('time')
#plt.ylabel('pressure')
#plt.show()


#drawing supply and demand graphs

sprice = np.array([10,15,18,23,28])
dprice = np.array([26,21,17,14,11])

quantity = np.array([5,8,11,18,23])


plt.plot(quantity,sprice)
plt.plot(quantity,dprice)
plt.xlabel('quantity')
plt.ylabel('price')
plt.title('supply and demand curves')
#plt.savefig('supply and demand.png')
plt.show()







#price = np.array([0,5,8,12,18,22,40])
#time = np.array([0,5,10,15,20,25,30])

#plt.scatter(price,time)
#plt.title('trade quotes')
#plt.xlabel('time')
#plt.ylabel('price')
#plt.savefig('prices_graph.png')  #this line saves the graph in the same place as the code
#plt.show()