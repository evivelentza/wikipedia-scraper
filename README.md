
# 🕵️‍♀️ Wikipedia Scraper

A small Python tool that:
1. Calls the **Country Leaders API** to retrieve a list of countries and their past/present political leaders.  
2. Visits each leader’s **Wikipedia page** and grabs the first paragraph of their biography.  
3. Cleans that paragraph (removes footnote markers, pronunciation text, extra whitespace) with regular expressions.  
4. Saves everything as nicely formatted **JSON** (`leaders.json`).

## Features

**Fast** – reuses one `requests.Session()` connection for all Wikipedia calls  
**Cookie-aware** – automatically refreshes API cookies if they expire 
**One-command run** – `python leaders_scraper.py` fetches → scrapes → cleans → saves


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/evivelentza/wikipedia-scraper.git
    cd wikipedia-scraper
    ```

2. (Recommended) Create and activate a virtual environment:
    ```sh
    python3 -m venv clean_venv
    source clean_venv/bin/activate
    ```

3. Install dependencies:
    ```sh
    pip install beautifulsoup4
    pip install requests
    ```

## Usage

To run the scraper from the command line:
```sh
python3 leaders_scaper.py
