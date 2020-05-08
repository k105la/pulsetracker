#!/usr/bin/python3

import numpy as np
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
        self.path = glob.glob('./images/*.jpg')
        self.frame_rate = 30
        self.dim = (320, 240)
        
    def video_to_frames(self):
        capture = cv.VideoCapture("../data/hr_test.mp4")
        ret, frame = capture.read()
        for count in range(300):
            cv.imwrite(f'./images/frame{count}.jpg', frame)
            ret, frame = capture.read()
            print(f'Number of frames: {count}')
            if ret != True:    
                break
            
        capture.release()
        cv.destroyAllWindows()
    
    def frame_extraction(self):
        cv_img = []
        for img in self.path:
            n = cv.imread(img, 0)
            img_array = cv.resize(n, self.dim)
            ##img_array = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            cv_img.append(img_array)
            grayscale_imgs = np.asarray(cv_img)
        plt.imshow(grayscale_imgs[0], cmap = plt.cm.gray )
        plt.imshow(grayscale_imgs[0] - grayscale_imgs[1], cmap = plt.cm.gray )
        plt.show()
        print(f'Grayscale image shape: {grayscale_imgs.shape}')
        return grayscale_imgs
    

    # Step 1 - Signal Diff
    def signal_differentiation(self):
        gray = self.frame_extraction()

        for i in range(200):
            self.avg_red.append(int(abs(np.mean(gray[i] - gray[i + 1]))))
            red = np.asarray(self.avg_red)
    
        peaks, _ = find_peaks(red, distance=5)
        plt.figure(figsize=(20,10))
        plt.title("Signal Differentiation")
        plt.ylabel("average red constant value")
        plt.xlabel("frame number")
        plt.plot(red[:200])
        plt.plot(peaks[:200], red[peaks[:200]], "x")
        plt.show()
        return peaks
    
    def v(self):
        peaks = self.signal_differentiation()
        
        for i in range(len(peaks) - 1):
            self.distance.append(peaks[i + 1] - peaks[i])
            dist = np.asarray(self.distance)
            print(dist)
            self.sigmoids.append(abs(np.square(abs(dist[i] - np.mean(dist)))))
            sig = np.asarray(self.sigmoids)
            print(sig)
        return sig
    
    def bpm(self):
        vari = self.v()
        minima = argrelmin(vari)
        minima_mean = np.mean(minima)
        heartrate = self.frame_rate * 60 / minima_mean
        print(f'Current heartrate: {heartrate}')
        return heartrate
