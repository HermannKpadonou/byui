"""
Author: Brother Hermann
Purpose: data analyst
"""
print('Data Analyst for life expectancy in the world')
print()
min_life_expectancy = float(99.99)
min_country = ''
max_life_expectancy = float(0)
max_country = ''
year = int(input('Enter the year of interest:'))

with open('life_expectancy.csv') as data_file:
    next(data_file)
    for line in data_file:
        parts = line.strip()
        parts = parts.split(',')
        Entity = parts[0]
        Code = parts[1]
        Year = int(parts[2])
        life_expectancy = float(parts [3])
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_country = Entity 
            max_year = Year
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_country = Entity  
            min_year = Year         
    print(f'The overall max life expectancy is : {max_life_expectancy} from {max_country} in {max_year}')      
    print(f'The overall min life expectancy is : {min_life_expectancy} from {min_country} in {min_year}')
data_file.close()
print()
# the user enter year
max_life_expectancy = float(0)
max_country = ''
min_life_expectancy = float(99.99)
min_country = ''
sum_life_expectancy = float(0)
count_life_expectancy = float(0)
with open("life_expectancy.csv") as data_file:
    next(data_file)
    for line in data_file:
        parts = line.strip()
        parts = parts.split(',')
        Entity = parts[0]
        Code = parts[1]
        Year = int(parts[2])
        life_expectancy = float(parts [3])
        if year == Year:
            sum_life_expectancy += life_expectancy
            count_life_expectancy += 1
            if life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy
                max_country = Entity 
            if life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy
                min_country = Entity   
    average_life_expectancy = sum_life_expectancy / count_life_expectancy
    print()
    print(f'For the Year {year} :')
    print(f'The average life expectancy across all countries was {average_life_expectancy:.2f}')
    print(f'The max life expectancy was in {max_country} with {max_life_expectancy}')
    print(f'The min life expectancy was in {min_country} with {min_life_expectancy}')
data_file.close()

# Creativity Part 
# Allow the user to type in a country, 
# then show the minimum, maximum, and average life expectancy for that country.
# The User enters Country
Country = input('Please,enter the country of interest: ')
max_life_expectancy = float(0)
min_life_expectancy = float(99.99)
sum_life_expectancy = float(0)
count_life_expectancy = float(0)

with open("life_expectancy.csv") as data_file:
    next(data_file)
    for line in data_file:
        parts = line.strip()
        parts = parts.split(',')
        Entity = parts[0]
        Code = parts[1]
        Year = int(parts[2])
        life_expectancy = float(parts[3])
        if Country.lower() == Entity.lower():
            sum_life_expectancy += life_expectancy
            count_life_expectancy += 1
            if life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy
                max_country = Entity 
                max_year = Year
            if life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy
                min_country = Entity 
                min_year = Year  
    average_life_expectancy = sum_life_expectancy / count_life_expectancy
    print()
    print(f'For the country {Country} :')
    print(f'The average life expectancy across in {Country} was {average_life_expectancy:.2f}')
    print(f'For {max_year},the max life expectancy  in {Country} was {max_life_expectancy}')
    print(f'For {min_year},The min life expectancy in {Country} was {min_life_expectancy}')
print()
print('Thanks you')