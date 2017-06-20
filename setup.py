#!/usr/bin/env python

from __future__ import print_function
from setuptools import setup


setup(
    name="nc",
    version=0.1,
    description="download VIIRS data",
    author="Mitchell Schull",
    author_email="mitch.schull@noaa.gov",
    url="https://github.com/bucricket/nc.git",
    packages = ['nc'],
    py_modules = ['nc.product.viirs_sdr','nc.product.viirs_ipng'],
    platforms='Posix; MacOS X; Windows',
    license='BSD 3-Clause',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        # Uses dictionary comprehensions ==> 2.7 only
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: GIS',
    ]
)

