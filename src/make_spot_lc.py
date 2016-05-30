#! /usr/bin/env python
"""
Produce light curves of spotted stars to use with CHEOPSsim.

Syntax: make_spot_lc Prot SpectralType [simulation_length [sampling_rate [ncurves]]]

Prot: rotational period in days.
simulation_length: length of simulation in days (default 48 days).
sampling_rate: resolution in minutes (default 120 minutes).
"""

import sys
import numpy.random

import spotlc


prot = float(sys.argv[1])
sptype = sys.argv[2]
try:
    totaltime = float(sys.argv[3])
except IndexError:
    totaltime = 48
try:
    samplingrate = float(sys.argv[4])
except IndexError:
    samplingrate = 120
try:
    ncurves = int(sys.argv[5])
except IndexError:
    ncurves = 1
try:
    randomseed = int(sys.argv[6])
except IndexError:
    randomseed = None
    
print('Simulating light curve with parameters')
print('Rotational period: {:.2f} days'.format(prot))
print('Spectral type: {}'.format(sptype))
print('########')
numpy.random.seed(randomseed)
time, flux = spotlc.spot_lc(prot, sptype, totaltime, samplingrate, ncurves,
                            *sys.argv[6:])
