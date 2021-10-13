from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import re
import pandas as pd

downloads_folder = "data/downloads"

def find_date_lines_in_description(description):
    """ 
    output: a list of matches in format
        date: the date of the match
        line: the full line
        line_before: the text matches before the date
        line_after: the text matches after the date
    """

    description.strip()
    output = []
    splitdescription = description.splitlines()

    for line in splitdescription:
        p = re.compile(
            r"(?P<line_before>.*?)(?P<date>\d\d*[^0-9]?\d\d?[^0-9]?\d\d+)\s?(?P<line_after>.*)")
        matches = p.finditer(line)

        for match in matches:
            date = match.group("date")
            line_before = match.group("line_before")
            line_after = match.group("line_after")
            output.append({"date": date, "line_before": line_before, "line_after": line_after, "line_full": line })

    return output

def test():
    """
    TODO move this to a proper test
    """

    test_str = """ 25.09.2021, la folie 
        01102021 les souffleurs
        01.1020 les souffleurs
        12.11.2921 @lamyt
        02.10.2021 @la folie
        28.10.2021 v2v 
        kidnap@rosya 11.11.2021
        kidnap@rosya 11.11.2021
        kidnap@rosya 11.11.2021
        12.11.2921 @lamyt 
        adaads adsads
        """
    res = find_date_lines_in_description(test_str)

    for r in res:
        print(r)

def build_df(event_lines):
    events = pd.DataFrame(event_lines)
    events["date_parsed"] = pd.to_datetime(events["date"],  errors="coerce", dayfirst=True)
    return events

def output_to_html(events):
    events[["date_parsed", "date", "artist", "line_full", "line_before", "line_after"]].sort_values("date_parsed", ascending=False).to_html("output.html")

def run():
    parsed_events = []
    files = [f for f in listdir(downloads_folder) if isfile(join(downloads_folder, f))]
    for file in files:
        with open(f"{downloads_folder}/{file}", 'r') as f:
            contents = f.read()
            soup = BeautifulSoup(contents, 'html.parser')
            description = soup.find(itemprop="description").text
            res = find_date_lines_in_description(description)
            [r.update(artist=file) for r in res]
            parsed_events.extend(res)
    events = build_df(parsed_events)
    output_to_html(events)

run()