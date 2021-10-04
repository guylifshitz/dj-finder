from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import re

downloads_folder = "data/downloads"

files = [f for f in listdir(downloads_folder) if isfile(join(downloads_folder, f))]

for file in files:
    with open(f"{downloads_folder}/{file}", 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'html.parser')
        description = soup.find(itemprop="description").text
        matches = re.findall(r"(.*)(\d\d?.\d\d?.(\d\d|\d\d\d\d))\s(.*)", description)
        print(matches)
