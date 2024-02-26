country = input("Enter the country name:\n") # Add country name
visits = int(input("Enter the number of visits:\n")) # Number of visits
list_of_cities = input("List the visited cities with a space:\n").split() # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

#TODo: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country, visits, list_of_cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": list_of_cities,
        }
        )
#def add_new_country(name, times_of_visits, cities_visited):
    #new_country = {}
    #new_country["country"] = name
    #new_country["visits"] = times_of_visits
    #new_country["cities"] = cities_visited
    #travel_log.append(new_country)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")