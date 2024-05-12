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

def Lewis(Pr, Sc):

    '''
    Function calculating Lewis number according to general definition.
    Lewis number defines the ratio of Heat diffusivity over Mass diffusivity. Used to characterize flows where there is both heat and mass transfer.
    Equal to one, transfer of both heat and mass or the presence of a velocity boundary layer which hinders heat and mass Transport 

    Input: 
    - Pr            =           Dimensionless Prandtl Number   [-]
    - Sc            =           Dimensionless Schmidt Number   [-]


    Output:
    - Le            =           Dimensionless Le Number   [-]
    '''

    Le = Pr / Sc

    return Le

def Peclet_heat(Re=None, Pr=None, u=None, alpha=None, L=None):

    '''
    Function calculating Peclet number according to general definition for heat transfer.
    Peclet number defines the ratio of Thermal convected energy over thermal conducted energy within the fluid. 
    For small Peclet numbers, conduction dominated over convection.

    Input: 
    - Re            =           Dimensionless Reynolds Number   [-]
    - Pr            =           Dimensionless Prandlt Number    [-]

    Or:

    -   u           =           Flow Velocity                   [m/s]
    -   L           =           Chraracteristic length          [m]
    -   alpha       =           Thermal diffusivity             [m2/s]




    Output:
    - Pe            =           Dimensionless Peclet Number for heat transfer   [-]
    '''

    if Re and Pr:
        
        Pe = Re * Pr
        return Pe
    
    if u and alpha and L:

        Pe = u / (alpha / L)

        return Pe

    raise ValueError('Not enough parameters provided or wrong combination of parameters provided')

def Peclet_mass(Re=None, Pr=None, u=None, alpha=None, L=None):

    '''
    Function calculating Peclet number according to general definition for heat transfer.
    Peclet number defines the ratio of Thermal convected energy over thermal conducted energy within the fluid. 
    For small Peclet numbers, conduction dominated over convection.

    Input: 
    - Re            =           Dimensionless Reynolds Number   [-]
    - Sc            =           Dimensionless Schmidt Number    [-]

    Or:

    -   u           =           Flow Velocity                   [m/s]
    -   L           =           Chraracteristic length          [m]
    -   D           =           Mass diffusivity                [m2/s]




    Output:
    - Pe            =           Dimensionless Peclet Number for heat transfer   [-]
    '''

    if Re and Sc:
        
        Pe = Re * Sc
        return Pe
    
    if u and alpha and L:

        Pe = u / (D / L)

        return Pe

    raise ValueError('Not enough parameters provided or wrong combination of parameters provided')

def Stanton(Nu=None, Pe=None, h=None, rho=None, u=None, Cp=None):
    '''
    Function calculating Stanton number according to general definition.
    The Stanton number is the ratio of total heat trasfer to the thermal capacity of a fluid.
    Used to characterize heat transfer in forced convection flow.

    Input: 
    -   Cp          =           Specific heat                    [J/ Kg K]
    -   mu          =           dynamic viscosity              [Pa • s, N / sm2, kg/(m•s)]
    -   k           =           Thermal conductivity            [m]

    Output:
    - St            =           Dimensionless Stanton Number   [-]
    '''

    if Nu and Pe:
        '''
        Calculate Stanton using Nusselt over Peclet Definition
        '''
        St = Nu / Pe

        return St
    
    if h and rho and Cp:
        '''
        Calculate Stanton using thomas Edward Stanton definition
        '''
        St = h / (rho * u * Cp)

        return St

    raise ValueError('Not enough parameters provided or wrong combination of parameters provided')

def Sherwood():
    '''
    Function calculating Sherwood number according to general definition.
    The Sherwood number is the ratio of Convective to Diffusive mass transport.

    Input: 
    -   L          =           Characteristic length                  [m]
    -   h          =           convective Mass transfer coefficient             [m/s]
    -   D           =           Mass diffusivity            [m2/s]

    Output:
    - Sh            =           Dimensionless Sherwood Number   [-]
    '''

    Sh = L * h / D

    return Sh



def Nusselt():
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