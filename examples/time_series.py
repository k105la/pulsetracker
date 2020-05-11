import heartrate as h
import matplotlib.pyplot as plt

heart = h.HeartRate()

heart.video_to_frames('./data/hr_test.mp4')

peaks = heart.get_peaks()
reds = heart.signal_diff()

plt.figure(figsize=(20,10))
plt.title("Signal Differentiation")
plt.ylabel("average red constant value")
plt.xlabel("frame number")
plt.plot(reds)
plt.plot(peaks[:200], reds[peaks[:200]], 'x')
plt.show()

