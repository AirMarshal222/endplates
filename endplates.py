import math
### Defining functions for endplate drag calculations

def reynolds(v, l, nu):
    """Calculate Reynolds number."""
    return (v * l) / nu

def cf_calc(reynolds):
    """Calculate the skin friction coefficient based on Reynolds number."""
    if reynolds < 5e5:
        # Laminar flow
        cf = 1.328 / (reynolds ** 0.5)
    else:
        # Turbulent flow
        cf = 0.455 / (math.log10(reynolds) ** 2.58)
    return cf

def wing_formfactor(tc, sweep):
    """Calculate the form factor based on thickness-to-chord ratio and sweep"""
    return (1 + tc*((1/math.cos(math.radians(sweep)))**2))

def wing_cd0(reynolds, tc, sweep):
    """Calculate the wing contribution to zero-lift drag coefficient"""
    cf = cf_calc(reynolds)
    form_factor = wing_formfactor(tc, sweep)
    cd0_wing = cf * form_factor * 1.66 # 1.66 is empirical approx of Swet/Sref for subsonic low reynolds aircraft
    return cd0_wing

def endplate_cd0(height, v, l, Sref):
    """Calculate the endplate conribution to zero-lift drag coefficient"""
    # Zero lift drag is same as skin friction coefficient for flat plate, reynolds varys with height
    cf = cf_calc(reynolds(v, l, 1.46e-5))
    Swet = 2 * height * l  # both sides of the endplate
    cd0e = cf * (Swet / Sref) * 2.59 # 2.59 is empirical approx of form factor for a flat plate
    return cd0e

def eff_AR1(geo_AR, height, b):
    """Calculate the effective aspect ratio with endplates based on Hoerner"""
    return geo_AR * (1 + 1.9 * (height / b))

def eff_AR2(geo_AR, height, chorde, chordw):
    """Calculate the effective aspect ratio with endplates with endplate chord also as a variable"""
    return geo_AR * (1 + 0.5 * (height / chorde * (chorde / chordw)**2))

def total_cd_end_1(height, cd0w, cl, e, geo_AR, b, v, chordw, Sref):
    """Calculate the total drag coefficient with endplate height as variable"""
    eff_ar = eff_AR1(geo_AR, height, b)
    cd0e = endplate_cd0(height, v, chordw, Sref)
    cd_tot = cd0w + cd0e + (cl ** 2) / (math.pi * eff_ar * e)
    return cd_tot

def total_cd_end_2(x, cd0w, cl, e, geo_AR, b, v, chordw, Sref):
    """Calculate the total drag coefficient with endplate height and chord as variable"""
    height, chorde = x
    eff_ar = eff_AR2(geo_AR, height, chorde, chordw)
    cd0e = endplate_cd0(height, v, chorde, Sref)
    cd_tot = cd0w + cd0e + (cl ** 2) / (math.pi * eff_ar * e)
    return cd_tot

def total_cd(cd0w, cl, e, geo_AR):
    """Calculate the total drag coefficient without endplates"""
    cd_tot = cd0w + (cl ** 2) / (math.pi * geo_AR * e)
    return cd_tot
 