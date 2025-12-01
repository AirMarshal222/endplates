# Endplate Optimization

The purpose of this script is to conduct endplate optimization using varying methodologies from Selig's paper, `An Angle of Attack Correction Scheme for the Design of LowAspect Ratio Wings with Endplates`. In this paper there are a few formula that are used to define the effective Aspect ratio gains from endplate heights. This project aims to compile these varying methodologies into an interactive script for endplate geometry optimization.

## Hoerner's Formula for Higher Aspect Ratios

The formula that the script is currently designed to use is a formula developed by Hoerner:

eff_AR = geo_AR * (1 + 1.9*(height/b))

Where height is the endpalte height, b being the wingspan, eff_AR the effective Aspect Ratio, and geo_AR the geometric Aspect Ratio. This formula works up to a height/b of 0.4.


## Empirical Formula for Low Aspect Ratio Wings

Selig's empirical formula for endplate design. The effective AR that an endplate generates can be generalized by a k-const that is a function of the h/c ratio of the endplate. Where h is the endplate height and c is the MAC of the wing. This script will take in the k constant and use it to calculate the effective AR within the total drag equation. It will then minimize the drag equation with respect to h/c, where the parasitic drag and induced drag are both functions of h/c, and all other factors held constant. In the future we can also implement multi-variable optimization with both h/c and alpha as variables(alpha controls the Cl value). 

## Drag Coefficient Calculations

We can estimate the various wing and endplate drag coefficients from a variety of empirical formula, I won't list them all here, but you can easily find them online or in Daniel Raymer's `Aircraft Design: A Conceptual Approach`. 

Essentially the total drag coefficient will be the sum of the zero-lift drag coefficient(cd0) and the induced drag coefficient(cdi).

cd0 can be derived from the sum of parasitic and pressure drags of all bodies.

cdi can be derived by the formula:

cl^2/(pi * AR * e)

where cl is the wing lift coefficient, AR is the aspect ratio, and e is the oswald's efficiency factor. AR in our context is the effective Aspect Ratio. 

