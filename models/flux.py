import numpy as np
import astropy.units as u
import astropy.constants as const
import matplotlib.pyplot as plt


"""
    flux.py

    This is where you'll implement the functions that model a lightcurve of a self-lensing binary! You'll want
    to check out the equations from Masuda+19 (https://arxiv.org/pdf/1808.10856.pdf), specifically Eq. 1-7.

    For each of the functions below you'll need to consider what parameters should be used and how to
    calculate the values. Remember to add docstrings to each function!
"""


def ellipsoidal_variation(phase, M_bh, M_star, inc, R_star, period):
    # time =[1, 2 , 10] * u.day
    # phase = [0, pi, 2pi]
    
    sep = keplers_third_law(M_bh=M_bh, M_star=M_star, period=period)
    
    ev = -np.cos(phase * 2)
    amplitude = M_bh * np.sin(inc) / M_star * (R_star / sep)**3 * np.sin(inc)
    return amplitude.decompose() * ev
    # TODO


def keplers_third_law(period, M_bh, M_star):
    sep = (const.G * (M_star + M_bh)*period**2 / (4 * np.pi**2))**(1/3)
    return sep.to(u.AU)

def doppler_beaming(phase, period, inc, M_bh, M_star):
    amplitude = 2.8e-3 * np.sin(inc) * (period / (1 * u.day))**(-1/3)*((M_bh + M_star) / u.solMass)**(-2/3) * (M_bh / u.solMass) 
    db = np.sin(phase)
    return amplitude.decompose() * db


def self_lensing(phase, M_bh, R_star, ):
    # TODO
    raise NotImplementedError


def relative_flux():
    return ellipsoidal_variation() + doppler_beaming() + self_lensing()


print(ellipsoidal_variation(phase=0, M_bh=9 * u.Msun, M_star=600 * u.Msun, inc=np.pi/2, R_star=20 * u.Rsun, sep=6 * u.AU))

x_vals = np.linspace(0, 2 * np.pi, 1000)
y_vals = ellipsoidal_variation(phase=x_vals, M_bh=9 * u.Msun, M_star=600 * u.Msun, inc=np.pi/2, R_star=20 * u.Rsun, sep=6 * u.AU)

plt.plot(x_vals, y_vals)
plt.show()