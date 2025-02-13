# Description: This script scrapes church data from the ExpertGPS website and saves it to a CSV file.
"""
Webscraper

@author: peytonpope
"""

from bs4 import BeautifulSoup as Soup
import pandas as pd
import requests
from pandas import DataFrame

from urllib.parse import urlparse, parse_qs

usdf = DataFrame() # Empty DataFrame

states = ['va', 'in', 'il', 'oh', 'mi', 'ny', 'pa', 'ma', 'ct', 'nj', 
          'de', 'md', 'wv', 'nc', 'sc', 'ga', 'fl', 'al', 'ms', 'la', 
          'tx', 'ar', 'tn', 'ky', 'mo', 'ia', 'wi', 'mn', 'sd', 'nd', 
          'mt', 'wy', 'co', 'nm', 'az', 'ut', 'id', 'wa', 'or', 'ca', 
          'nv', 'ok', 'ks', 'ne', 'me', 'nh', 'vt', 'ri'] # List of all lower 48states

for state in states: # Loop through all states
    url = f"https://www.expertgps.com/data/{state}/churches.asp" # URL for each state
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    html = requests.get(url, headers=headers) # Get the HTML content

    site_soup = Soup(html.text, 'html.parser')  # Specify parser

    tags = site_soup.find_all('a') # Find all link tags

    def getLat(link): # Function to get latitude from link
        parsed_url = urlparse(link)
        params = parse_qs(parsed_url.query)
        lat = params.get("lat", [None])[0]
        return lat

    def getLon(link): # Function to get longitude from link
        parsed_url = urlparse(link)
        params = parse_qs(parsed_url.query)
        lon = params.get("lon", [None])[0]
        return lon

    lats = [getLat(x['href']) for x in tags if "lat=" in x['href']] # List of latitudes
    lons = [getLon(x['href']) for x in tags if "lat=" in x['href']] # List of longitudes

    names = [x.text for x in tags if "lat=" in x['href']] # List of church names only if link has coordinates

    # Create a DataFrame
    df = DataFrame({'name': names, 
                    'latitude': lats, 
                    'longitude': lons}) 

    coords = ['longitude', 'latitude']
    df[coords] = df[coords].astype(float) # Convert to float

    df['denomination'] = 'NA'  # Default value

    # Loop through the DataFrame to assign denominations
    for i in range(len(df)):
        if 'Baptist' in df['name'][i]:
            df.at[i, 'denomination'] = 'Baptist'
        elif 'Methodist' in df['name'][i]:
            df.at[i, 'denomination'] = 'Methodist'
        elif 'Presbyterian' in df['name'][i]:
            df.at[i, 'denomination'] = 'Presbyterian'
        elif 'Episcopal' in df['name'][i]:
            df.at[i, 'denomination'] = 'Episcopal'
        elif 'Catholic' in df['name'][i]:
            df.at[i, 'denomination'] = 'Catholic'
        elif 'Church of Christ' in df['name'][i]:
            df.at[i, 'denomination'] = 'Church of Christ'
        elif 'Church of God' in df['name'][i]:
            df.at[i, 'denomination'] = 'Church of God'
        elif 'Lutheran' in df['name'][i]:
            df.at[i, 'denomination'] = 'Lutheran'
        elif 'Pentecostal' in df['name'][i]:
            df.at[i, 'denomination'] = 'Pentecostal'
        elif 'Mennonite' in df['name'][i]:
            df.at[i, 'denomination'] = 'Mennonite'
        elif 'LDS' in df['name'][i] or 'Latter Day Saints' in df['name'][i]:
            df.at[i, 'denomination'] = 'Latter Day Saints'
        else:
            df.at[i, 'denomination'] = 'Unspecified'
        
    usdf = pd.concat([usdf, df], ignore_index=True) # Concatenate the DataFrames

    
usdf.to_csv('/Users/peytonpope/Downloads/churches.csv', index=False) # Save to CSV



