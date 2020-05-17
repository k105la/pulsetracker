# Extracting ❤️ - rate with mobile phones 

Start here: [`pulse.py`](src/pulse.py)

## 💭 Background
This project applies a simple algorithm to monitor heart rate using a mobile phone with a camera and flash. The goal here is to have a low cost and widely accessible way to measure someones heart rate.

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

### Usage with Docker 
```
$ sudo sh run_docker.sh
```

### Documentation
1. `$ cd docs`
2. `$ make html`
3. `$ open _build/html/index.html`
