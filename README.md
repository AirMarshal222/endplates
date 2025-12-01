# Endplate Optimization

The purpose of this script is to do endplate optimization using Selig's empirical formula for endplate design. The effective AR that an endplate generates can be generalized by a k-const that is a function of the h/c ratio of the endplate. Where h is the endplate height and c is the MAC of the wing. This script will take in the k constant and use it to calculate the effective AR within the total drag equation. It will then minimize the drag equation with respect to h/c, where the parasitic drag and induced drag are both functions of h/c, and all other factors held constant. In the future we can also implement multi-variable optimization with both h/c and alpha as variables(alpha controls the Cl value). 

The MAC of Duck Duck Goose is 0.2 m. The wingspan is 1.44. The aspect ratio is 7.17.

