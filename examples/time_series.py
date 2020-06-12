import pulse as p
import matplotlib.pyplot as plt

pulse = p.Pulse()

testing_uid = "1kzd0DmeunLGEeB0nWLFFaIfuFZn"
pulse.pulsebox_to_frames(testing_uid)

peaks = pulse.get_peaks()
reds = pulse.signal_diff()

plt.figure(figsize=(15,5))
plt.title("Signal Differentiation")
plt.ylabel("average red constant value")
plt.xlabel("frame number")
plt.plot(reds)
plt.plot(peaks[:200], reds[peaks[:200]], 'x')
plt.show()
