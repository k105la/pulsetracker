import numpy as np
import cv2 as cv
import os
from tqdm import tqdm

def feature_images_to_array(folder):
    images = [os.path.join(root, filename)
             for root, dirs, files in os.walk(folder)
             for filename in files
             if [filename]]
    ic = []
    for img in tqdm(images):
        img_array = cv.imread(img)
        size_array = cv.resize(img_array, (320, 240), interpolation = cv.INTER_NEAREST)
        ic.append(size_array)
    X = np.asarray(ic)
    return X
