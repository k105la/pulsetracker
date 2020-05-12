.. heartrate documentation master file, created by
   sphinx-quickstart on Mon May 11 05:15:24 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

HeartRate: Touch based monitoring
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


**HeartRate** is a simple Python library used to monitor heartrate using video from a mobile phone.
"""""""""""""""

**Basic usage of HeartRate:**

.. code-block:: python
  
  import heartrate as h    
  heart = h.HeartRate()
  heart.video_to_frames('./path/to/video.mp4')
  heart.bpm()


