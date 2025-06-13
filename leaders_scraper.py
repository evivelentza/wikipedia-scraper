import requests
import re
from bs4 import BeautifulSoup
import json

session = requests.Session()
def get_first_paragraph(wikipedia_url, session):
    #print(wikipedia_url) # keep this for the rest of the notebook
    
    response = session.get(wikipedia_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraph_list =[]
    for p in soup.select('p'):
        text = p.get_text(strip=True)
        if len(text)> 80:
            text = re.sub(r"\[\d+\]", "", text)
            text = re.sub(r"\([^()]*[ˈˌa-zA-Z].*?\)", "", text)
            text = re.sub(r"\s+", " ", text)
            paragraph_list.append(text.strip())
        
    if paragraph_list:   
        return paragraph_list[0]
    else:
        return "No paragraph found"


def get_leaders():
    base_url = "https://country-leaders.onrender.com"
    cookie_url = "https://country-leaders.onrender.com/cookie"
    countries_url = "https://country-leaders.onrender.com/countries"
    leaders_url = "https://country-leaders.onrender.com/leaders"
    
    session = requests.Session()

    cookies = session.get(cookie_url).cookies
    countries = session.get(countries_url, cookies=cookies).json()
    
    leaders_per_country = {}
    
    for code in countries:
        response = session.get(leaders_url, cookies=cookies, params={"country": code})
        if response.status_code == 200:
            leaders = response.json()
            for leader in leaders:
                wikipedia_url = leader["wikipedia_url"]
                leader["bio"] = get_first_paragraph(wikipedia_url, session)
        else:
            cookies = session.get(cookie_url).cookies
            leaders = response.json()
    

        leaders_per_country[code] = leaders

    return leaders_per_country

def save(leaders_per_country):
    with open("leaders.json", "w", encoding="utf-8") as f:
        json.dump(leaders_per_country, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    all_leaders = get_leaders()
    save(all_leaders)
    print("Scraping Done and Info saved to leaders.json!")