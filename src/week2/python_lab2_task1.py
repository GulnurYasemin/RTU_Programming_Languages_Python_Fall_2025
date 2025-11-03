"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

#  Create the datasets
temperatures = [15.5, 17.0, 16.3, 18.2, 19.0, 20.1, 21.3]  # Daily temperatures in °C

# Type annotation removes Pylance warnings
city_population: dict[str, int] = {
    "Riga": 632614,
    "Vilnius": 588412,
    "Tallinn": 437619,
    "Warsaw": 1793579,
    "Helsinki": 658864
}

#  Compute aggregates
average_temperature = sum(temperatures) / len(temperatures)

# Use lambda to make Pylance understand the key function clearly
largest_city = max(city_population, key=lambda c: city_population[c])
largest_population = city_population[largest_city]
smallest_city = min(city_population, key=lambda c: city_population[c])
smallest_population = city_population[smallest_city]
total_population = sum(city_population.values())

#  Print results
print(f"Average temperature: {average_temperature:.2f}°C")
print(f"Largest city: {largest_city} - {largest_population:,}")
print(f"Smallest city: {smallest_city} - {smallest_population:,}")
print(f"Total population: {total_population:,}")
