import numpy as np
A=np.linspace(1,100,100)
B=A.reshape(10,10)
C=B**2
D=C[(C%3)==0]
print('These are the elements divisible by 3 from the matrix of the squares of the first 100 positive integers')
print(D)
np.save('div_by_3', D)