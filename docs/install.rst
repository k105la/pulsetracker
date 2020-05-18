============
Installation
============

Installing with Docker:

.. code-block:: bash
    
    docker pull docker.pkg.github.com/akilhylton/pulsetracker/pulsetracker:0.1
    docker run -it docker.pkg.github.com/akilhylton/pulsetracker/pulsetracker:0.1


Installing the development version

.. code-block:: bash

    git clone https://github.com/akilhylton/pulsetracker
    cd pulsetracker
    pip install -r requirements.txt
    sudo pip install -e .
