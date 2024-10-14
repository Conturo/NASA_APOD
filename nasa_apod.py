import requests
import re
from PIL import Image
from pathlib import Path

    
# replace with path to your API key
api_key = Path('nasa_api.env').read_text()

date = str(input("Enter date in YYYY-MM-DD format or leave blank for today's: "))

if date == "":
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
    jsonDict = response.json()
    img = Image.open(requests.get(jsonDict["url"], stream=True).raw)
    img.show()
elif re.match(r"\b\d{4}-\d{2}-\d{2}\b", date):
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}")
    jsonDict = response.json()
    img = Image.open(requests.get(jsonDict["url"], stream=True).raw)
    img.show()
else:
    print("fail")