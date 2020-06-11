============
Installation
============

Installing with Docker:

.. code-block:: bash
    
    docker pull docker.pkg.github.com/akilhylton/pulsetracker/pulsetracker:0.3
    docker run -it docker.pkg.github.com/akilhylton/pulsetracker/pulsetracker:0.3


Installing the development version

.. code-block:: bash

    git clone https://github.com/akilhylton/pulsetracker.git
    cd pulsetracker
    pip3 install -r requirements.txt
    sudo pip3 install -e .
