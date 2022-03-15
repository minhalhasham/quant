import numpy as np 
import matplotlib.pyplot as plt 

def power_law(t,a):
    return t**-a


time=np.arange(10**-4,1,10**-4)

emp=[]
for i in range(1000): 
    emp.append(np.random.choice(power_law(time,1.5))






plt.plot(emp)