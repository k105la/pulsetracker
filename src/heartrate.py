#!/usr/bin/python3
import numpy as np
import cv2 as cv
from scipy.signal import find_peaks, argrelmin
import glob, os


class HeartRate:
    """
    This is the main class of the heartrate module.
    """
    def __init__(self, fr=30):
        """
        Initialise the HeartRate class. It takes one argument fr(frame rate) 
        which defaults to 30.
        """
        self.avg_red = []
        self.rgb_imgs = []
        self.distance = []
        self.sigmoids = []
        self.frame_rate = fr
        self.dim = (320, 240)


    def remove_frames(self):
        """
        Removes all frames from images folder. 
        """
        imgPath = glob.glob('./images/*.jpg')
        for img in imgPath:
            os.remove(img)

    # TODO: Improve and clean up video_to_frames() with print statements.
    ## Test with different video lengths must be over 10 seconds long
    def video_to_frames(self, videoPath):
        """
        Converts input videoPath to frames.
        """
        capture = cv.VideoCapture(videoPath)
        ret, frame = capture.read()

        if not os.path.exists('./images/'):
            os.makedirs('./images/')
        else:
            self.remove_frames()

        for count in range(300):
            cv.imwrite('./images/frame{}.jpg'.format(count), frame)
            ret, frame = capture.read()
            if ret != True:
                if ((count / self.frame_rate) < 10):
                    self.remove_frames()
                    print('Your video was {} seconds but video length must be 10 seconds long.'.format(count / self.frame_rate))
                    print('Try Again. Please use a video that is 10 seconds or longer.')
                break

        capture.release()
        cv.destroyAllWindows()


    def frames_to_gray(self):
        """
        Converts RGB input frames to grayscale.
        """
        try:
            imgPath = glob.glob('./images/*.jpg')
            cv_img = []
    
            for img in imgPath:
                n = cv.imread(img, 0)
                img_array = cv.resize(n, self.dim)
                cv_img.append(img_array)
                grayscale_imgs = np.asarray(cv_img)
            return grayscale_imgs
        
        except:
            print('The images directory is empty, you must first run video_to_frames()')


    def signal_diff(self):
        """
        Subtracts one frame from the subsequent frame.
        """
        try:
            gray = self.frame_to_gray()
           
            if len(self.avg_red) == 0: # Will only run loop if avg_red list is empty
                for i in range(200):
                    self.avg_red.append(int(abs(np.mean(gray[i] - gray[i + 1]))))
            red = np.asarray(self.avg_red)
            return red
        
        except:
            pass 

    def get_peaks(self, dist=5):
        """
        Takes a one-dimensional array and finds all local maxima
        by simple comparison of neighbouring values.
        """
        try:
            red = self.signal_diff()
            peaks, _ = find_peaks(red, distance=dist)
            return peaks
        
        except:
            pass 


    def variances(self):
        """
        Calculates the how far the peaks are
        spread out from their average value.
        """
        try:
            peaks = self.get_peaks()
            if len(self.sigmoids) == 0: # Will only run loop if sigmoids list is empty
                for i in range(len(peaks) - 1):
                    self.distance.append(peaks[i + 1] - peaks[i])
                    dist = np.asarray(self.distance)
                    self.sigmoids.append(abs(np.square(abs(dist[i] - np.mean(dist)))))
            sig = np.asarray(self.sigmoids)
            return sig
        
        except:
            pass


    def bpm(self):
        """
        Calculates the heart rate value. 
        """
        try:
            v = self.variances()
            minima = argrelmin(v)
            minima = np.asarray(minima)
            m = minima[( minima > self.frame_rate * 60 / 200 )] # Filters values less than 9
            minima_mean = np.mean(m)
            heartrate = self.frame_rate * 60 / minima_mean
            return heartrate

        except:
            pass
