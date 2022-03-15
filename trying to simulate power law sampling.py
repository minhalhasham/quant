import numpy as np 
import matplotlib.pyplot as plt 


def power_law(t,a):
    return t**-a


time=np.arange(10**-4,1,10**-4)

y=power_law(time,1.5)

y_norm=y/sum(y)


print(sum(y_norm))

emp=[]
new=[]
for i in range(len(time)): 
    emp.append(np.random.choice(power_law(time[i],1.5)))


emp2=[]
for i in time: 
    emp2.append(power_law(i,1.5))
plt.loglog(time,emp2)