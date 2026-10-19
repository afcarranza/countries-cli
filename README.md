# Countries CLI

## What it does
A user runs the script and sees a menu with four options: filter countries by region, find the largest or most populous country, compare two countries, or quit. If they choose to filter by region, they enter a region name (e.g., “Europe”), and the tool returns a numbered list of every country in that region with its population and area. If they choose to find the largest country, they pick a metric (population or area), and the tool returns the top country with its value. If they choose to compare, they enter two country names and a metric (e.g., which is larger), and the tool prints a sentence stating which country is larger. After each result, the menu reappears until the user chooses to quit. The tool uses four fields from the API: name, region, population, and area. Instead of crashing, the program prints a clear message and returns to the menu when the API is unreachable, the user enters an empty, invalid, or unrecognized menu option, region, or country name, or a country is missing the requested data.

## How to run
1. Activate the virtual environment: `source .venv/Scripts/activate`
2. Install dependencies: `pip install requests`
3. Run the program: `python countries.py`