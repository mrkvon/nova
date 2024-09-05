import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, UTC
from dateutil import parser

# Function to fetch and parse HTML
def fetch_and_parse(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def extract_magnitude_and_time(parsed_html):
    for infobox in parsed_html.find_all(class_='keyinfobox'):
        text = infobox.get_text()
        if 'Magnitude' in text:
            num = infobox.find('ar')
            full_magnitude = num.get_text()
            magnitude = full_magnitude.split(' ')[0]
            measured = [line for line in text.splitlines() if "Measured on" in line][0]
            date_time = measured.split(": ", 1)[1]
            return float(magnitude), date_time

def time_elapsed(date_time_raw):
    date_time = parser.parse(date_time_raw)
    now = datetime.now(UTC)
    return now-date_time

def exploded(magnitude):
    return magnitude < 5




# Example usage
url = 'https://theskylive.com/sky/stars/hr-5958-star'  # Replace with your target URL
parsed_html = fetch_and_parse(url)
magnitude, date_time = extract_magnitude_and_time(parsed_html)

print(magnitude, str(time_elapsed(date_time))[:-10] + (" \u2726" if exploded(magnitude) else ''))


