    result = minimize_scalar(end.total_cd, args=constants_tuple, bounds=(0, 8), method='bounded')

    print(f"Optimization successful: {result.success}")
    print(f"Minimum value of x found: {result.x[0]:.4f}")
    print(f"Minimum function value (f(x)): {result.fun:.4f}")