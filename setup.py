# -*- coding: utf-8 -*-
"""setup.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10J5cH29OS8cmzkdSpJOpm9-s37sP4449
"""

from setuptools import setup

with open('README.md','r') as fh:
      long_description=fh.read()

setup(name='disconv',
      version='0.0.3',
      description='basic value datatype conversion module in datastructures',
      py_modules=['disconv'],
      package_dir={'':'src'},
      classifiers=[
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.10",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",

      ],

      long_description=long_description,
      long_description_content_type="text/markdown",
      install_requires=[
            "blessings ~= 1.7",
      ],
      extras_require = {
            "dev": [
                  "pytest>=3.7",
            ],
      },
      url="https://github.com/LeeJSC/disconv",
      author="Lee Johns Shaji",
      author_email="leejohnsdecarmel@gmail.com",
      )