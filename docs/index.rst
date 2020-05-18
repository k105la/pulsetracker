.. heartrate documentation master file, created by
   sphinx-quickstart on Mon May 11 05:15:24 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PulseTracker
==================================
 
**PulseTracker** is a simple Python library used to monitor heart rate using video from a mobile phone.

-----

**Basic usage of PulseTracker:**

.. code-block:: python
  
  import pulse as p    
  pulse = p.Pulse()
  pulse.video_to_frames('./path/to/video.mp4')
  pulse.bpm()


The User Guide
""""""""""""""
This part of the documentation, which is mostly prose, begins with some background information about PulseTracker, then focuses on step-by-step instructions for getting the most out of this library.

.. toctree::
   :maxdepth: 2

   intro 
   install 
   api


