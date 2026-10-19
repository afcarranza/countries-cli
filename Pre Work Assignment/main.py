import requests


## Fetch data

def fetch_countries():
    try:
        response = requests.get("https://countries.dev/countries", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Sorry, couldn't reach the countries API: {error}")
        return None


## Process data

def filter_by_region(countries, region):
    results = []
    for country in countries:
        if country.get("region", "").lower() == region.lower():
            results.append(country)
    return results


def find_largest(countries, field):
    largest_country = None
    largest_value = 0

    for country in countries:
        value = country.get(field)
        if value is not None and value > largest_value:
            largest_value = value
            largest_country = country

    return largest_country


def compare_countries(countries, name1, name2, field):
    country1 = None
    country2 = None

    for country in countries:
        if country.get("name", "").lower() == name1.lower():
            country1 = country
        elif country.get("name", "").lower() == name2.lower():
            country2 = country

    if not country1 or not country2:
        return None

    value1 = country1.get(field)
    value2 = country2.get(field)

    if value1 is None or value2 is None:
        return None

    if value1 > value2:
        return f"{country1['name']} has a larger {field} ({format_number(value1)}) than {country2['name']} ({format_number(value2)})."
    elif value1 < value2:
        return f"{country2['name']} has a larger {field} ({format_number(value2)}) than {country1['name']} ({format_number(value1)})."
    else:
        return f"{country1['name']} and {country2['name']} have the same {field} ({format_number(value1)})."


def get_regions(countries):
    regions = set()
    for country in countries:
        region = country.get("region")
        if region:
            regions.add(region)
    return sorted(regions)


## Display results

def format_number(value):
    if value is None:
        return "N/A"
    return f"{value:,}"


def display_countries(results, region):
    if not results:
        print(f"No countries found in '{region}'.")
        return
    print(f"\nCountries in {region.title()} ({len(results)}):")
    for number, country in enumerate(results, start=1):
        name = country.get("name", "Unknown")
        population = format_number(country.get("population"))
        area = format_number(country.get("area"))
        print(f"{number}. {name} | Population: {population} | Area: {area} km²")


def display_largest(country, field):
    if country is None:
        print(f"No data available for '{field}'.")
        return
    value = format_number(country.get(field))
    print(f"\nLargest country by {field}: {country.get('name')} ({value})")


def display_comparison(result):
    if result is None:
        print("Couldn't compare those countries. Check the spelling, or the data may be missing.")
        return
    print(f"\n{result}")


## User interaction

def show_menu():
    print("\n=== Countries Explorer ===")
    print("1. Filter countries by region")
    print("2. Find the largest country")
    print("3. Compare two countries")
    print("4. Quit")


def run_region_filter(countries):
    regions = get_regions(countries)
    print(f"Available regions: {', '.join(regions)}")
    region = input("Enter a region: ").strip()
    if not region:
        print("Please enter a region name.")
        return
    results = filter_by_region(countries, region)
    display_countries(results, region)


def run_find_largest(countries):
    field = input("Find the largest by (population/area): ").strip().lower()
    if field not in ("population", "area"):
        print("Please type 'population' or 'area'.")
        return
    display_largest(find_largest(countries, field), field)


def run_compare(countries):
    name1 = input("First country: ").strip()
    name2 = input("Second country: ").strip()
    if not name1 or not name2:
        print("Please enter two country names.")
        return
    field = input("Compare by (population/area): ").strip().lower()
    if field not in ("population", "area"):
        print("Please type 'population' or 'area'.")
        return
    display_comparison(compare_countries(countries, name1, name2, field))


## Main program

def main():
    countries = fetch_countries()
    if countries is None:
        return

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            run_region_filter(countries)
        elif choice == "2":
            run_find_largest(countries)
        elif choice == "3":
            run_compare(countries)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()