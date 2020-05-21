# Motivation
This project is following the requirement of Data Scientist Nanodegree of Udacity to create a Pypi package.
As a computational chemistry PhD student, the majority of my daily task is to create the input file and run various calculations.

Therefore, I build this project to help me generate the input files for my most frequent calculations: 
1. Single-point calculation 
2. Geometry optimization calculation 
3. NBO calculation
4. NICS calculation

# The Description of Files
a. package: contain the full list of Gaussian_inputfile package files
   
   1. Gaussian_inputfile.egg-info: include the description of package
   2. Gaussian_inputfile: include the code of Gaussian_inputfile package
   3. dist: include the .gz file
   4. setup.py: setup file for the package
   
b. example: showcase the usage of Gaussian_inputfile to generate various inputfile

   1. *.py files: showcase the usage of Gaussian_inputfile to generate sp, opt, nbo, and NICS calculations
   2. *.com file: generated inputfiles

# Required Libaries
This project was written by Python 3, in order to enable the function in example folder, you will need to install the Gaussian_inputfile package by 'pip install Gaussian_inputfile'
