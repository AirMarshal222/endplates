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
Sref = 0.3  # reference area in square meters
cl = 0.556 # lift coefficient
geo_AR = 7.66 # geometric aspect ratio
e = 0.925 # Oswald efficiency factor
b = 1.524 # wingspan in meters
chordw = 0.2 # mac length in meters

lamb = 0.000004  # regularization coefficient

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
    constants_tuple1 = (cd0w, cl, e, geo_AR, b, v, chordw, Sref, lamb)
    constants_tuple2 = (cd0w, cl, e, geo_AR, b, v, chordw, Sref, lamb)

    # Minimize Objective Function
    #resulte1 = minimize_scalar(end.total_cd_end_1, args=constants_tuple1, bounds=(0, 0.3), method='bounded')
    resulte2 = minimize(end.total_cd_end_2, x0=[0.1, 0.1], args=constants_tuple2, bounds=[(0, 1.0), (0.01, 1.0)], method='L-BFGS-B')
    result = end.total_cd(cd0w, cl, e, geo_AR)

    """
    Dont need this rn
    print(f"Method 1 Optimization successful: {resulte1.success}")
    print(f"Minimum height: {resulte1.x:.4f}")
    print(f"Total drag coefficient with endplates: {resulte1.fun:.4f}")
    print()
    """
    print(f"Method 2 Optimization successful: {resulte2.success}")
    print(f"Minimum height: {resulte2.x[0]:.4f}")
    print(f"Minimum chord: {resulte2.x[1]:.4f}")
    print(f"Total drag coefficient with endplates: {resulte2.fun:.4f}")
    print()
    print(f"Total drag coefficient without endplates: {result:.4f}")

    test_height = 0.1
    test_chord = 0.25
    find = end.total_cd_end_2([test_height, test_chord], *constants_tuple2)
    print(f"Test calc at height {test_height} and chord {test_chord}m: {find:.4f}")



if __name__ == "__main__":
    main()






