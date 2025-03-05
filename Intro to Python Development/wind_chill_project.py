"""
Author: Brother Hermann
Purpose: wind chill
"""

def wind_chill(temperature,wind_speed):
    return 35.74+0.6215*temperature - 35.75*wind_speed**0.16 + 0.4275*temperature*wind_speed**0.16

def celsius_to_fahrenheit(celsius):
    return celsius * (9/5) + 32

new_temperature = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ")
# convert Celsius to fahrenheit
if unit == 'C':
    new_temperature = celsius_to_fahrenheit(new_temperature)
# Caculate the wind-chill
for wind_speed in range (5,65,5):
    new_wind_chill = wind_chill(new_temperature,wind_speed)
    print(f"At temperature {new_temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {new_wind_chill:.2f}F")
# Creativity requirement
# Define a list of possible comments based on the wind chill
comments = ['its freezing!', 'You should wear a warm coat.', 'It is not too bad.', 'It feels nice and cozy.', 'Wow, it is hot!']
if new_wind_chill < 0:
    print(comments[0])
elif new_wind_chill < 32:
    print(comments[1])
elif new_wind_chill < 50:
    print(comments[2])
elif new_wind_chill < 80:
    print(comments[3])
else:
    print(comments[4])
# end to program