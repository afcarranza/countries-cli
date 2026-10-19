# Countries CLI
A command-line tool for exploring country data from the [countries.dev](https://countries.dev) API.

## What it does

A user runs the script and sees a menu with four options: filter countries by region, find the largest or most populous country, compare two countries, or quit. If they choose to filter by region, the tool lists the available regions, the user enters one (e.g., "Europe"), and the tool returns a numbered list of every country in that region with its population and area. If they choose to find the largest country, they pick a metric (population or area), and the tool returns the top country with its value. If they choose to compare, they enter two country names and a metric, and the tool prints a sentence stating which country is larger. After each result, the menu reappears until the user chooses to quit. The tool uses four fields from the API: name, region, population, and area. Instead of crashing, the program prints a clear message when the API is unreachable, the user enters an empty, invalid, or unrecognized menu option, region, or country name, or a country is missing the requested data.

## API used

[countries.dev](https://countries.dev/docs), a free REST API for country data. No API key or signup required.

## How to run

1. Clone this repository and move into the folder:
```bash
   git clone https://github.com/afcarranza/countries-cli.git
   cd countries-cli
```
2. Create and activate a virtual environment:
```bash
   python -m venv .venv
   source .venv/Scripts/activate   # Windows (Git Bash)
   source .venv/bin/activate       # Mac/Linux
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Run the program:
```bash
   python main.py
```

## Example

```
Choose an option (1-4): 3
First country: Brazil
Second country: United States of America
Compare by (population/area): area

United States of America has a larger area (9,372,610) than Brazil (8,515,767).
```

## Project structure

`main.py` is organized into sections:
- **Fetch data**: calls the API with error handling
- **Process data**: filters, finds the largest, and compares countries
- **Display results**: formats output for the user
- **User interaction**: the menu and input validation
- **Main program**: runs the menu loop

## How to run
1. Activate the virtual environment: `source .venv/Scripts/activate`
2. Install dependencies: `pip install requests`
3. Run the program: `python main.py`