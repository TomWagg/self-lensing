import numpy as np
import astropy.units as u
import astropy.constants as const


"""
    flux.py

    This is where you'll implement the functions that model a lightcurve of a self-lensing binary! You'll want
    to check out the equations from Masuda+19 (https://arxiv.org/pdf/1808.10856.pdf), specifically Eq. 1-7.

    For each of the functions below you'll need to consider what parameters should be used and how to
    calculate the values. Remember to add docstrings to each function!
"""


def ellipsoidal_variation():
    # TODO
    raise NotImplementedError


def doppler_beaming():
    # TODO
    raise NotImplementedError


def self_lensing():
    # TODO
    raise NotImplementedError


def relative_flux():
    return ellipsoidal_variation() + doppler_beaming() + self_lensing()
