# Extracting ❤️ - rate with mobile phones 

Start here: [`heartrate.py`](src/heartrate.py)

## 💭 Background
This project applies a simple algorithm to monitor heartrate using a mobile phone with a camera and flash. The goal here is to have a low cost and widely accessible way to measure someones heartrate.

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
$ sh run_docker.sh
```

### Documentation
1. `$ cd docs`
2. `$ make html`
3. `$ open _build/html/index.html`
