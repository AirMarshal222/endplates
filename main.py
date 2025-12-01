import endplates as end
from scipy.optimize import minimize_scalar
import numpy as np

# Constants
reynolds = end.reynolds(20, 0.2, 1.46e-5) # reynolds number
tc = 0.091  # thickness-to-chord ratio
sweep = 0  # sweep angle in degrees
mac = 0.2  # mean aerodynamic chord in meters
thickness = 0.001  # endplate thickness in meters
Sref = 0.29  # reference area in square meters
cl = 0.5 # lift coefficient
geo_AR = 7.17 # geometric aspect ratio
e = 1.0 # Oswald efficiency factor
b = 1.44 # wingspan in meters

"""
Formulas: 

Effective Aspect Ratio with endplates
eff_AR = geo_AR * (1 + 1.9*(height/b))

Endplate Contribution to Zero-Lift Drag Coefficient
cd0e = 1.28 * (front_area / Sref) 

Total Drag Coefficient
cd_tot = cd0w + cd0e + (cl^2)/(pi*eff_AR*e)
"""

def main():
    cd0w = end.wing_cd0(reynolds, tc, sweep) # wing zero-lift drag coefficient
    constants_tuple = (cd0w, cl, e, geo_AR, b, thickness, Sref)

    # Minimize Objective Function
    result = minimize_scalar(end.total_cd, args=constants_tuple, bounds=(0, 8), method='bounded')

    print(f"Optimization successful: {result.success}")
    print(f"Minimum value of x found: {result.x:.4f}")
    print(f"Minimum function value (f(x)): {result.fun:.4f}")


if __name__ == "__main__":
    main()






