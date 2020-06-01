from setuptools import setup, find_packages

setup(
    name='pulsetracker',
    version='0.0.1',
    description='A simple algorithm to monitor heartrate using any mobile phone with a camera and flash.',
	package_dir={"": "src"},
	author='Akil M Hylton',
    author_email='hyltonakil@gmail.com',
    project_urls={
        'CoronaTracker': 'https://coronatrackerbeta.com/',
        'Source Code': 'https://github.com/akilhylton/pulsetracker',
        },
    install_requires=[
        'numpy', 
        'opencv-python',
        'scipy',
        'pyrebase',
        'setuptools'
    ]
)
