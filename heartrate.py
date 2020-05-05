#!/usr/bin/python3

import numpy as np
import argparse
import cv2 as cv
import glob
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, argrelmin

class HeartRate:
    def __init__(self):
        self.avg_red = []
        self.rgb_imgs = []
        self.distance = []
        self.sigmoids = []
        self.path = glob.glob("./test/images_rgb/*.jpg")
        self.frame_rate = 60
        self.dim = (320, 240)
        self.n = 0
    
    def frame_extraction(self):
        for img in self.path:
            rgb_matrix = cv.imread(img, 0)
            resized_matrix = cv.resize(rgb_matrix, self.dim)
            grayscale_imgs = np.asarray(resized_matrix)
        return grayscale_imgs

    def signal_differentaion(self):
        gray_imgs = self.frame_extraction()
        for n in range(99):
            self.avg_red.append(int(abs(np.mean(gray_imgs[n] - gray_imgs[n + 1]))))
            avg_red = np.asarray(self.avg_red)
        return avg_red
    
    def get_peaks(self):
        peaks , _ = find_peaks(self.signal_differentaion())
        return peaks

    def variances(self):
        for i in range(len(self.get_peaks()) - 1):
            p = self.get_peaks()
            self.distance.append(p[i + 1] - p[i])
            self.dist = np.asarray(self.distance)
            self.sigmoids.append(abs(np.square(abs(self.dist[i] - np.mean(self.dist)))))
            self.sig = np.asarray(self.sigmoids)
        return self.sig
    
    def bpm(self):
        v = self.variances()
        minima = argrelmin(v) 
        minima_mean = np.mean(minima)
        heartrate = self.frame_rate * 60 / minima_mean
        return heartrate

h = HeartRate()
print(f'Heartrate: {h.bpm()}')
