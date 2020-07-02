from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='pulsetracker',
    version='0.5',
    description='A simple algorithm to monitor heartrate using any mobile phone with a camera and flash.',
    long_description=readme(),
    package_dir={"": "src"},
    author='Akil M Hylton',
    author_email='hyltonakil@gmail.com',
    url='pulsetrackerapp.com'
    project_urls={
        'CoronaTracker': 'https://coronatrackerbeta.com/',
        'Source Code': 'https://github.com/akilhylton/pulsetracker',
        },
    python_requires='>=3',
    install_requires=[
        'numpy', 
        'opencv-python',
        'scipy',
        'pyrebase',
        'setuptools'
    ]
)
