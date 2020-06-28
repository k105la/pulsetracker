![Imgur](https://i.imgur.com/E3s6RUi.png)

![PulseTracker Tests](https://github.com/akilhylton/pulsetracker/workflows/PulseTracker%20Tests/badge.svg)
![PulseTracker Docs](https://img.shields.io/readthedocs/pulsetracker)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)


## 💭 Background
An open source tool built for monitoring heart rate. The goal here is to have a low cost and widely accessible way to measure someones heart rate. It uses a touch-based system for generating heart rate values. In contrast to it's counterpart(touchless-based systems) it is a far more accurate and less sensitive to enviornmental conditions.  

## Usage
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

## Testing 
#### Local Testing
```
$ sudo sh install.sh && sudo make test
```
#### Testing with Docker
```
$ sudo sh run_docker_test.sh
```

## Documentation
We use [sphinx](https://www.sphinx-doc.org/en/master/) to build our documentation based on rST files and comments in the code, below is a quick guide to getting started. 
``` 
cd docs
make html
```

This will output the documentation to `docs/_build/html`. 
Now to view built documentation run `open _build/html/index.html`.


## Contributing 

Contributions are welcome! Please read our [Code of Conduct](CODE_OF_CONDUCT.md) and [how to contribute](CONTRIBUTING.md) before contributing to help this project stay welcoming.

Directory Structure
------
    .
    ├── docs                # Sphinx documentation folder
    ├── examples            # The example code 
    ├── src                 # The source code for the library
    ├── tests               # Unit tests and system tests
    └── ui                  # The UI

To understand how the library works see [`pulse.py`](src/pulse.py)

## License 

MIT License

Copyright (c) 2020 Akil M Hylton 
