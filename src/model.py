import batman
import numpy as np


def calculate_period(a, radius_star, mass_star):
    """
        Keppler third law to calculate planet's period 

        T^2 = \ frac{4 pi^2 * a^3}{G (M + m)} 
    """
    G = 6.67408e-11  # m^3 Kg ^-1 s^-2
    M_sun = 132712440018 * 1000 ** 3 / 6.67408e-11  # Kg
    R_sun = 696342e3  # meters

    return np.sqrt(4 * np.pi ** 2 * (a * radius_star * R_sun) ** 3 / (G * mass_star * M_sun)) / (24 * 3600    )

def init_transit_model(transit_params, time, star_params):
    """
    Creates the batman model using the desired values.
    Parameters
    ----------
    transit_params:
        Dictionary with the initial transit parameters
    time:
        array of times
    Returns
    -------
    m:
        Batman's TransitModel object
    params:
        Batman's TransitParams object that can be edited, in a later stage, to accept new values
    """
    params = batman.TransitParams()  # object to store transit parameters
    params.t0 = transit_params["t0"]  # time of inferior conjunction
    params.per = calculate_period(transit_params['a'], radius_star=star_params['star_radius'], mass_star=star_params['star_mass'])  # orbital period
    params.rp = transit_params['rp']  # planet radius (in units of stellar radii)
    params.a = transit_params['a']  # semi-major axis (in units of stellar radii)
    params.inc = transit_params['inc']  # orbital inclination (in degrees)
    params.ecc = 0.  # eccentricity
    params.w = 90.  # longitude of periastron (in degrees)
    params.limb_dark = star_params['limb_type'] # limb darkening model
    params.u = star_params['limb_coefs'] # limb darkening coefficients [u1, u2, u3, u4]

    m = batman.TransitModel(params, time)  # initializes model
    return m, params


def create_transit_model(model, params):
    """
    Creates a light curve array with the model and chosen parameters
    Parameters
    ----------
    model:
        Batman's transit model
    params
        Batman's TransitParams object
    Returns
    -------
    Array with the light curve
    """
    return model.light_curve(params)


def edit_transit_params(params, p, star_radius, star_mass):
    """
    Changes the batman TransitParams that are being fitted for the new parameters
    Parameters
    ----------
    params:
            Batman's TransitParams object
    p:
        Array given by the MCMCa
    Returns
    -------
    """

    params.rp = p['rp']  # planet radius (in units of stellar radii)
    params.a = p['a']  # semi-major axis (in units of stellar radii)
    params.inc = p['inc']  # orbital inclination (in degrees)
    params.t0 = p['t0']   # time of inferior conjunction -> center of lightcurve
    params.per = calculate_period(p['a'], radius_star=star_radius, mass_star=star_mass)
    return params


