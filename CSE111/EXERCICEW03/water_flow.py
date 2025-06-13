"""
Author : Hermann KPADONOU
Purpose : Water flow simulation
explain : This code simulates water flow in a pipe system.
"""


# The density of water and the gravitational acceleration are constants
density_of_water = 998.2  # kg/m^3
gravitational_acceleration = 9.80665  # m/s^2

def water_column_height(tower_height, tank_height):
    """
    Calculates and returns the height of a column of water from a tower height
    and a tank wall height.

    Parameters:
        tower_height (float): the height of the tower.
        tank_height (float): the height of the walls of the tank.
    Return:
        float: the height of the water column.
    """
    # h = t + (3*w) / 4
    h_column = tower_height + (3 * tank_height) / 4
    return h_column


def pressure_gain_from_water_height(height):
    """
    Calculates and returns the pressure caused by Earth’s gravity pulling
    on the water stored in an elevated tank.

    Parameters:
        height (float): the height of the water column in meters.
    Return:
        float: the pressure in kilopascals.
    """
    # P = (ρ * g * h) / 1000

    pressure = (density_of_water * gravitational_acceleration * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    
    """Calculates and returns the pressure loss in a pipe due to friction.          
    Parameters:
        pipe_diameter (float): the diameter of the pipe in meters.
        pipe_length (float): the length of the pipe in meters.
        friction_factor (float): the Darcy-Weisbach friction factor.
        fluid_velocity (float): the velocity of the fluid in meters per second.
    Return:
        float: the pressure loss in kilopascals.
    """

    # P = -(f * L * ρ * v^2) / (2000 * D)
    pressure_loss_from_pipe = -(friction_factor * pipe_length * density_of_water *
                     fluid_velocity ** 2) / (2000 * pipe_diameter)
    return pressure_loss_from_pipe


def pressure_loss_from_fittings(
    fluid_velocity, quantity_fittings):
    """Calculates and returns the pressure loss in a pipe due to fittings.
    Parameters:
        fluid_velocity (float): the velocity of the fluid in meters per second.
        quantity_fittings (int): the number of 90° angles in the pipe.
    Return: float: the pressure loss in kilopascals.
    """
    # P = -0.04 * ρ * v^2 * n / 2000
    pressure_loss_from_fittings = -(0.04 * density_of_water * (fluid_velocity ** 2) *
                     quantity_fittings) / 2000
    return pressure_loss_from_fittings

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculates and returns the Reynolds number for a fluid flowing in a pipe.
    parameters:
        hydraulic_diameter (float): the hydraulic diameter of the pipe in meters.   
        fluid_velocity (float): the velocity of the fluid in meters per second.
    Return: float: the Reynolds number.
    """
    # R= (ρ * v * d) / μ
    dynamic_viscosity = 0.0010016
    reynolds = (density_of_water * fluid_velocity * hydraulic_diameter) / dynamic_viscosity
    
    return reynolds


def pressure_loss_from_pipe_reduction(larger_diameter,
    fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculates and returns the pressure loss in a pipe due to a reduction in diameter.
    Parameters:
        larger_diameter (float): the diameter of the larger pipe in meters.
        fluid_velocity (float): the velocity of the fluid in meters per second.
        reynolds_number (float): the Reynolds number of the fluid.
        smaller_diameter (float): the diameter of the smaller pipe in meters.
    Return:
        float: the pressure loss in kilopascals.
    """
    # k= (0.1+ 50 / R) * ((D / d)^4-1)
    # P = -k * (ρ * v^2) / 2000
    k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    pressure_loss_from_pipe_reduction = -k * (density_of_water * fluid_velocity ** 2) / 2000
    return pressure_loss_from_pipe_reduction

#========================================================================================================#

#Exceeding the Requirements : convert pressure from kilopascals to pounds per square inch
def kpa_to_psi(kpa_pressure: float) -> float:
    """Converts pressure from kilopascals (kPa) to pounds per square inch (psi).

    Args:
        kpa_pressure: Pressure in kilopascals.

    Returns:
        Pressure in pounds per square inch.
    """
    kpa_to_psi_cf = 0.1450377377 # cf = conversion factor
    psi_pressure = kpa_pressure * kpa_to_psi_cf
    return psi_pressure

#=========================================================================================================#

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(pressure):.2f} pounds per square inch") #exceeding the requirements
if __name__ == "__main__":
    main()

# end of the code