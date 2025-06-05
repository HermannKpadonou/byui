"""
Author : Hermann KPADONOU
Purpose : Water flow simulation
explain : This code simulates water flow in a pipe system.
"""




def water_column_height(tower_height, tank_height):
    tower_height = float(input("Please,Enter the tower height in meters: "))
    tank_height = float(input("Please,Enter the tank height in meters: "))
    # Calculate the height of the water column in the tank
    water_column_height = tower_height + (3* tank_height) / 4
    return water_column_height
print(f"The height of the water column in the tank is {water_column_height(tower_height, tank_height)} meters.")


def pressure_gain_from_water_height(water_column_height):
    """Calculate the pressure gain from the water column height.
    The pressure gain is calculated using the formula:
    pressure_gain_from_water_height = water_column_height * 9.80665 * 998.2
    where 9.80665 is the acceleration due to gravity in m/s^2
    and 998.2 is the density of water in kg/m^3."""
    pressure_gain_from_water_height = (water_column_height * 9.81 * 998.2) / 1000  # Convert to kPa
    
    return pressure_gain_from_water_height
print(f"The pressure gain from the water column height is {pressure_gain_from_water_height} kPa.")