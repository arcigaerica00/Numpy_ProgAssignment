import numpy as np
X=np.random.random((5,5))
m=X.mean()
s=X.std()
Normalized_X=(X-m)/(s)
print('Normalized X')
print(Normalized_X)
np.save('X_normalized', Normalized_X)