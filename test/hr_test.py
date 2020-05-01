import numpy as np
import matplotlib.pyplot as plt
from helper.images_to_array import feature_images_to_array

test_images = "./images_rgb/"

x = feature_images_to_array(test_images)

X = x.copy()
X[:, :, 1] = 0
X[:, :, 2] = 0

print(X.shape)
print(X[0] - X[1])
print(int(abs(np.mean(X[0] - X[1]))))

#plt.imshow(X[0], interpolation='nearest')
#plt.show()
