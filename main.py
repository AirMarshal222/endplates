import endplates as end
from scipy.optimize import minimize_scalar, minimize
import numpy as np

# Constants
reynolds = end.reynolds(20, 0.2, 1.46e-5) # reynolds number of the plane
v = 20  # velocity in m/s
tc = 0.091  # thickness-to-chord ratio
sweep = 0  # sweep angle in degrees
mac = 0.2  # mean aerodynamic chord in meters
thickness = 0.001  # endplate thickness in meters
Sref = 0.29  # reference area in square meters
cl = 0.49 # lift coefficient
geo_AR = 7.17 # geometric aspect ratio
e = 0.75 # Oswald efficiency factor
b = 1.44 # wingspan in meters
chordw = 0.2 # mac length in meters

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
    constants_tuple1 = (cd0w, cl, e, geo_AR, b, v, chordw, Sref)
    constants_tuple2 = (cd0w, cl, e, geo_AR, b, v, chordw, Sref)

    # Minimize Objective Function
    resulte1 = minimize_scalar(end.total_cd_end_1, args=constants_tuple1, bounds=(0, 0.5), method='bounded')
    resulte2 = minimize(end.total_cd_end_2, x0=[0.1, 0.1], args=constants_tuple2, bounds=[(0, 0.5), (0.01, 1.0)], method='L-BFGS-B')
    result = end.total_cd(cd0w, cl, e, geo_AR)

    print(f"Method 1 Optimization successful: {resulte1.success}")
    print(f"Minimum height: {resulte1.x:.4f}")
    print(f"Total drag coefficient with endplates: {resulte1.fun:.4f}")
    print()
    print(f"Method 2 Optimization successful: {resulte2.success}")
    print(f"Minimum height: {resulte2.x[0]:.4f}")
    print(f"Minimum chord: {resulte2.x[1]:.4f}")
    print(f"Total drag coefficient with endplates: {resulte2.fun:.4f}")
    print()
    print(f"Total drag coefficient without endplates: {result:.4f}")



if __name__ == "__main__":
    main()






