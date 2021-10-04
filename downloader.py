import pandas as pd
import requests


def download_dj(dj_name, dj_url):
    r = requests.get(dj_url)
    with open(f"data/downloads/{dj_name}.html" , "w") as f:
        f.write(r.text)

def run():
    djs = pd.read_csv("data/djs.txt")
    print(djs)
    for idx, dj in djs.iterrows():
        print(dj)
        download_dj(dj["name"], dj["url"])

run()