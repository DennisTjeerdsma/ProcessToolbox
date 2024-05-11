from math import pi

def areaCircle(d, unit_in='m', unit_out='m'):
    '''
    Function calculating the area of a circle

    Input: 
    - d         =           Diameter of the circle
    - unit_in   =           the unit of the input value
    - unit_out  =           The desired output unit

    Output:
    - the area of the circle in desired output unit
    '''


    metric_units = [['fm', -15], ['pm', -12], ['A',-10], ['nm',-9], ['µm',-6], ['mm',-3], ['cm', -2], ['dm', -1 ], ['m', 0], ['dam', 1], ['hm', 2], ['km', 3], ['Mm', 6], ['Gm', 9], ['Tm', 12]]

    # Setting up required variables
    factor_in = 0
    factor_out = 0

    # Sanitize input, check if the units_in and unit_out are valid values and find the corresponding factor:
    for pair in metric_units:
        if pair[0] == unit_in:
            factor_in = pair[1]
        if pair[0] == unit_out:
            factor_out = pair[1]

    # If factors do not match, convert to new unit
    if factor_in != factor_out:
        d = d * 10**(factor_out-factor_in)

    # Calculate the area
    A_Circle = 0.25 * pi * d**2

    return A_Circle

print(areaCircle(5, 'm', 'mm'))
