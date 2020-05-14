from setuptools import setup

setup(
    name='heartrate',
    version='0.0.1',
    description='A simple algorithm to monitor heartrate using any mobile phone with a camera and flash.',
    py_module=['heartrate'],
    package_dir={'': 'src'},
    author='Akil M Hylton',
    author_email='hyltonakil@gmail.com',
    project_urls={
        'CoronaTracker': 'https://coronatrackerbeta.com/',
        'Source Code': 'https://github.com/akilhylton/heartrate',
        },
    install_requires=[
        'numpy', 
        'opencv-python',
        'scipy',
        'setuptools'
    ]
)

