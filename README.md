# dj-finder

## About
This is a utility to track upcoming performances of DJs based on the list of events in their soundcloud description.
The performances of all the DJs you track will be output to an HTML file, ordered by date. 

## Running
To run:
1- add DJs who's soundcloud pages you want to track to the data data/djs.txt file.
2- run 'python downloader.py' to download the latest soundcloud pages for the DJs.
3- run 'python parser.py' to attempt to extract performance dates and output them all into an HTML file.

## Todo:
- add the requirements file
- handle month-first formatted event dates