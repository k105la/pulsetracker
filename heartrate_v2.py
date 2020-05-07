#!/usr/bin/python3

import numpy as np
import argparse
import cv2 as cv
import glob
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, argrelmin

class HeartRate:
    def __init__(self):
        self.grayscale = []
        self.avg_red = []
        self.rgb_imgs = []
        self.distance = []
        self.sigmoids = []
        self.path = glob.glob('./images_rgb/*.jpg')
        self.frame_rate = 30
        self.dim = (320, 240)
        self.n = 0

    def video_to_frames(self):
        parser = argparse.ArgumentParser(description='Enter path where video is stored.')
        parser.add_argument('-v', '--video', help='a path to video')
        args = parser.parse_args()
        
        capture = cv.VideoCapture(args.video)
        ret, frame = capture.read()
        ##count = 0
        for count in range(150):
            cv.imwrite(f'./images_rgb/frame{count}.jpg', frame)
            ret, frame = capture.read()
            ##count += 1
            print(f'Number of frames: {count}')    
        print("Frames done.")
        capture.release()
        cv.destroyAllWindows()

    def frame_extraction(self):
        ##self.video_to_frames()      
        for img in self.path:
            rgb_matrix = cv.imread(img, 0)
            resized_matrix = cv.resize(rgb_matrix, self.dim)
            self.grayscale = np.asarray(resized_matrix)
        return self.grayscale

    def signal_differentiation(self):
        gray_imgs = self.frame_extraction()
        for n in range(150):
            self.avg_red.append(int(abs(np.mean(gray_imgs[n] - gray_imgs[n + 1]))))
            avg_red = np.asarray(self.avg_red)
        return avg_red
    
    def get_peaks(self):
        peaks , _ = find_peaks(self.signal_differentiation())
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
#h.video_to_frames()
print(f'Heartrate: {h.bpm()}')
