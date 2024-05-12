def Reynolds(rho, v, L, mu):

    '''
    Function calculating Reynolds number according to general definition.
    Function determines if a fluid flow is laminar or turbulent. 

    Input: 
    -   rho         =           Density of the Fluid            [kg/m3]
    -   v           =           Flow speed of Fluid             [m/s]
    -   L           =           Characteristic Length           [m]
    -   mu          =           Dynamic viscosity of Fluid      [Pa • s, N / sm2, kg/(m•s)]

    Output:
    - Re            =           Dimensionless Reynolds Number   [-]
    '''

    Re = (rho * v * L)/mu

    return Re

def Prandtl(Cp, mu, k):

    '''
    Function calculating Prandtl number according to general definition.
    Prandtl number defined the ratio of momentum diffusivity over heat diffusivity. In other words, it is an indication of the relative
    thickness of the velocity boundary layer compared to thermal boundary layer. 

    Input: 
    -   Cp          =           Specific heat                    [J/ Kg K]
    -   mu          =           dynamic viscosity              [Pa • s, N / sm2, kg/(m•s)]
    -   k           =           Thermal conductivity            [m]

    Output:
    - Pr            =           Dimensionless Prandtl Number   [-]
    '''

    Pr = (Cp * mu)/k

    return Pr


def Schmidt(mu, rho, D):

    '''
    Function calculating Schmidt number according to general definition.
    Schmidt number defines the ratio of momentum diffusivity over Mass diffusivity. In other words, it is an indication of the relative
    thickness of the velocity boundary layer compared to Mass transfer boundary layer. 

    Input: 
    -   mu          =           dynamic viscosity               [Pa • s, N / sm2, kg/(m•s)]
    -   rho         =           Density of the Fluid            [kg/m3]
    -   D           =           Mass diffusivity                [m2/s]

    Output:
    - Sc            =           Dimensionless Schmidt Number   [-]
    '''

    Sc = mu/(rho * D)

    return Sc

def Schmidt(mu, rho, D):

    '''
    Function calculating Schmidt number according to general definition.
    Schmidt number defines the ratio of momentum diffusivity over Mass diffusivity. In other words, it is an indication of the relative
    thickness of the velocity boundary layer compared to Mass transfer boundary layer. 

    Input: 
    -   mu          =           dynamic viscosity               [Pa • s, N / sm2, kg/(m•s)]
    -   rho         =           Density of the Fluid            [kg/m3]
    -   D           =           Mass diffusivity                [m2/s]

    Output:
    - Sc            =           Dimensionless Schmidt Number   [-]
    '''

    Sc = mu/(rho * D)

    return Sc


def Nusselt()
    '''
    Function calculating Nusselt number according to general definition.
    The Nusselt number is the ratio of total heat trasfer to conductive heat transfer at the boundary in a fluid.
    Total heat transfer combines conduction and convection. Convection includes both advection and diffusion.

    Input: 
    -   Cp          =           Specific heat                    [J/ Kg K]
    -   mu          =           dynamic viscosity              [Pa • s, N / sm2, kg/(m•s)]
    -   k           =           Thermal conductivity            [m]

    Output:
    - Pr            =           Dimensionless Prandtl Number   [-]
    '''

    Pr = (Cp * mu)/k

    return Nu