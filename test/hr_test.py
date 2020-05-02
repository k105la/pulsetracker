from tqdm import tqdm
import numpy as np
import glob
import cv2 as cv
import matplotlib.pyplot as plt

# Signal Differentiation 
path = glob.glob("./heartrate/test/images_rgb/*.jpg")
cv_img = []
for img in tqdm(path):
    n = cv.imread(img)
    img_array = cv.resize(n, (320, 240))
    img_array = cv.cvtColor(img_array, cv.COLOR_RGB2GRAY)
    cv_img.append(img_array)

c = np.asarray(cv_img)

print(c.shape)

avg_red = []

plt.figure(figsize=(20,10))

for i in range(614):
    avg_red.append(int(abs(np.mean(c[i] - c[i + 1]))))
    signal = np.asarray(avg_red)

print(signal[0])
