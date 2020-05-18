# Extracting ❤️ - rate with mobile phones 

Start here: [`pulse.py`](src/pulse.py)

## 💭 Background
pulsetracker is an open source tool built for monitoring heart rate. The goal here is to have a low cost and widely accessible way to measure someones heart rate. It uses a touch-based system for generating heart rate values. In contrast to it's counterpart(touchless-based systems) it is a far more accurate and less sensitive to enviornmental conditions.  

### Usage
After cloning this repository and changing directories to it.

#### 1. Install the dependencies
```
$ make install
```
#### 2. Install library
```
$ make
```
See example of usage in examples folder.

### Testing 
```
$ sudo sh run_docker.sh
```

### Documentation
1. `$ cd docs`
2. `$ make html`
3. `$ open _build/html/index.html`
