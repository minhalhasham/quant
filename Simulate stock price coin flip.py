import numpy as np 
import matplotlib.pyplot as plt




def sim (start_price, n): 
    ''' Function which, given a starting price and number of times to "flip the coin", returns a dollar more/less than the starting price.
    '''
    emp=[range(n)]
    emp[0]=start_price
    for i in np.random.random(n): 
        if i>0.5:
            start_price+=1  
        else: 
            start_price-=1
        emp.append(start_price)
    return emp


#Jason's solution: 
    
# =============================================================================
# start_price=100
# new_price=start_price + np.cumsum(np.random.choice([-1,1], n, True))
# print(new_price)
# =============================================================================

test=sim(100,100)
plt.plot(test)
plt.xlabel("Step Number", size=26)
plt.ylabel("Price ($)", size=26)
plt.tick_params(axis='both', labelsize=22)
plt.tight_layout()