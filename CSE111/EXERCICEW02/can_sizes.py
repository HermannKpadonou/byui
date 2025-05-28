"""
Author: Hermann KPADONOU
Purpose: Can Storage Efficiency
Creative addittions
"""
import math
def compute_volume(radius,height):
    """compute and return thr volume of a cylinder
    Parameters
       radius:the radius of the cylinder
       height: the height of the cylinder
    Return: the volume of the cylinder
    """
    volume = math.pi * radius**2 * height
    return volume


def compute_surface_area(radius,height):

    """compute and return the surface area of a cylinder
    Parameters
        radius:the radius of the cylinder
        height: the height of the cylinder
    Return: the surface area of the cylinder
    """
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    """
    Computes and returns the storage efficiency of a can.
    Storage efficiency is defined as volume / surface_area.
    This function calls compute_volume and compute_surface_area.

    Parameters:
        radius: The radius of the can.
        height: The height of the can.
    Return:
        The storage efficiency of the can. Returns 0 if surface_area is 0.
    """
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    if surface_area == 0:
        return 0  # Avoid division by zero
    efficiency = volume / surface_area
    return efficiency

def compute_cost_efficiency(radius, height, cost):
    """
    Computes and returns the cost efficiency of a can.
    Cost efficiency is defined as volume / cost.
    This function calls compute_volume.

    Parameters:
        radius: The radius of the can.
        height: The height of the can.
        cost: The cost of the can.
    Return:
        The cost efficiency of the can (volume per dollar). Returns 0 if cost is 0.
    """
    volume = compute_volume(radius, height)
    if cost == 0:
        return 0 # Avoid division by zero
    efficiency = volume / cost
    return efficiency

def main():
    can_data = [
        {"name": "#1 Picnic",    "radius": 6.83,  "height": 10.16, "cost": 0.28},
        {"name": "#1 Tall",      "radius": 7.78,  "height": 11.91, "cost": 0.43},
        {"name": "#2",           "radius": 8.73,  "height": 11.59, "cost": 0.45},
        {"name": "#2.5",         "radius": 10.32, "height": 11.91, "cost": 0.61},
        {"name": "#3 Cylinder",  "radius": 10.79, "height": 17.78, "cost": 0.86},
        {"name": "#5",           "radius": 13.02, "height": 14.29, "cost": 0.83},
        {"name": "#6Z",          "radius": 5.40,  "height": 8.89,  "cost": 0.22},
        {"name": "#8Z short",    "radius": 6.83,  "height": 7.62,  "cost": 0.26},
        {"name": "#10",          "radius": 15.72, "height": 17.78, "cost": 1.53},
        {"name": "#211",         "radius": 6.83,  "height": 12.38, "cost": 0.34},
        {"name": "#300",         "radius": 7.62,  "height": 11.27, "cost": 0.38},
        {"name": "#303",         "radius": 8.10,  "height": 11.11, "cost": 0.42}
    ]

    # Loop through each can data
    for can in can_data:
        name = can["name"]
        radius = can["radius"]
        height = can["height"]

        # Compute the volume of a can
        volume = compute_volume(radius, height)

        # Compute the surface area of a can
        surface_area = compute_surface_area(radius, height)

        # Compute the storage efficiency
        storage_efficiency = compute_storage_efficiency(radius, height)
        

        # Print the storage efficiency
        print(f"{name} {storage_efficiency:.2f}")
        

#start this program by calling the main function
main()
