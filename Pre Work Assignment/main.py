from dataclasses import field

import requests

response = requests.get("https://countries.dev/countries")
countries = response.json()

#print(len(countries))
#print(countries[0])

## Filter countries by region

def filter_by_region(countries, region):
    results = []
    for country in countries:
        if country["region"].lower() == region.lower():
            results.append(country["name"])
    return results


europe = filter_by_region(countries, "europe")
africa = filter_by_region(countries, "africa")
asia = filter_by_region(countries, "asia")
americas = filter_by_region(countries, "americas")
print(europe)
print(len(europe))
print(africa)
print(len(africa))
print(asia)
print(len(asia))
print(americas)
print(len(americas))

## Find the largest country by a given field (population, area, etc.)

def find_largest(countries, field):
    largest_country = None
    largest_value = 0

    for country in countries:
        value = country.get(field)
        if value is not None and value > largest_value:
            largest_value = value
            largest_country = country

    return largest_country

biggest_pop = find_largest(countries, "population")
print(biggest_pop["name"], biggest_pop["population"])

biggest_area = find_largest(countries, "area")
print(biggest_area["name"], biggest_area["area"])

##compare two countries by a given field (population, area, etc.)

def compare_countries(countries, name1, name2, field):
    country1 = None
    country2 = None

    for country in countries:
        if country["name"].lower() == name1.lower():
            country1 = country
        elif country["name"].lower() == name2.lower():
            country2 = country

    if not country1 or not country2:
        return None

    value1 = country1.get(field)
    value2 = country2.get(field)

    if value1 is None or value2 is None:
        return None

    if value1 > value2:
        return f"{country1['name']} has a larger {field} ({value1}) than {country2['name']} ({value2})."
    elif value1 < value2:
        return f"{country2['name']} has a larger {field} ({value2}) than {country1['name']} ({value1})."
    else:
        return f"{country1['name']} and {country2['name']} have the same {field} ({value1})."

result = compare_countries(countries, "Brazil", "United States of America", "area")
print(result)

all_fields = set()
for country in countries:
    all_fields.update(country.keys())

for field in sorted(all_fields):
    missing = 0
    for country in countries:
        value = country.get(field)
        if value is None or value == "" or value == []:
            missing += 1
    print(field, missing)
