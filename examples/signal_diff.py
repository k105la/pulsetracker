import pulse as p
import matplotlib.pyplot as plt

testing_uid = "1kzd0DmeunLGEeB0nWLFFaIfuFZn"
pulse = p.Pulse()
pulse.pulsebox_to_frames(testing_uid)

new_signal = pulse.frames_to_gray()
plt.imshow(new_signal[0], cmap = plt.cm.gray)
plt.show()
