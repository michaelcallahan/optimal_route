from setuptools import setup, find_packages

setup(
    name='optimal_route',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'geopy',
        'folium',
    ],
    entry_points={
        'console_scripts': [
            'optimal_route=optimal_route.main:main',
        ],
    },
    author='Michael Callahan',
    description='A module to find the optimal route with minimal gas station stops.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/michaelcallahan/optimal_route',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
