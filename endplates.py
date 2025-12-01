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

def endplate_cd0(thickness, height, Sref):
    """Calculate the endplate conribution to zero-lift drag coefficient"""
    # We use the drag coefficient of a flat plate: 1.28
    cd_plate = 1.28
    front_area = thickness * height
    cd0_endplate = cd_plate * (front_area / Sref) * 2  # multiply by 2 for both endplates
    return cd0_endplate

def eff_AR(geo_AR, height, b):
    """Calculate the effective aspect ratio with endplates"""
    return geo_AR * (1 + 1.9 * (height / b))

def total_cd(height, cd0w, cl, e, geo_AR, b, thickness, Sref):
    """Calculate the total drag coefficient with endplate height as variable"""
    eff_ar = eff_AR(geo_AR, height, b)
    cd0e = endplate_cd0(thickness, height, Sref)
    cd_tot = cd0w + cd0e + (cl ** 2) / (math.pi * eff_ar * e)
    return cd_tot

 