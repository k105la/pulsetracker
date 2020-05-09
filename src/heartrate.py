#!/usr/bin/python3

import numpy as np
import cv2 as cv
import glob
from scipy.signal import find_peaks, argrelmin

class HeartRate:
    def __init__(self):
        self.avg_red = []
        self.rgb_imgs = []
        self.distance = []
        self.sigmoids = []
        self.path = glob.glob('../images/*.jpg')
        self.frame_rate = 30
        self.dim = (320, 240)


    def video_to_frames(self, videoPath):
        capture = cv.VideoCapture(videoPath)
        ret, frame = capture.read()
        for count in range(300):
            cv.imwrite(f'../images/frame{count}.jpg', frame)
            ret, frame = capture.read()
            if ret != True:
                break

        capture.release()
        cv.destroyAllWindows()


    def frame_extraction(self):
        cv_img = []
        for img in self.path:
            n = cv.imread(img, 0)
            img_array = cv.resize(n, self.dim)
            cv_img.append(img_array)
            grayscale_imgs = np.asarray(cv_img)
        return grayscale_imgs


    def signal_differentiation(self):
        gray = self.frame_extraction()
        if len(self.avg_red) == 0:
            for i in range(200):
                self.avg_red.append(int(abs(np.mean(gray[i] - gray[i + 1]))))
        red = np.asarray(self.avg_red)
        return red


    def get_peaks(self):
        red = self.signal_differentiation()
        peaks, _ = find_peaks(red, distance=5)
        return peaks
        

    def variance(self):
        peaks = self.get_peaks()
        if len(self.sigmoids) == 0: 
            for i in range(len(peaks) - 1):
                self.distance.append(peaks[i + 1] - peaks[i])
                dist = np.asarray(self.distance)
                self.sigmoids.append(abs(np.square(abs(dist[i] - np.mean(dist)))))
        sig = np.asarray(self.sigmoids)
        return sig


    def bpm(self):
        v = self.variance()
        minima = argrelmin(v)
        minima_mean = np.mean(minima)
        heartrate = self.frame_rate * 60 / minima_mean
        return heartrate
