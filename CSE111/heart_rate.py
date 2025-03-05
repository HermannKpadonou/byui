"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

print( "Welcome in the Heart rate Control")
print()
# asks for a person’s age
age = int(input("Please,Enter your age "))

#your maximum heart rate per minute
rate_maxi = int(220-age)

slowest = float(rate_maxi*(65/100))
fastest = float(rate_maxi*(85/100))

print("When you exercise to strengthen your heart,")
print(f"you should keep your heart rate between {slowest:.0f} and {fastest:.0f} beats per minute.")
 