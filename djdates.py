import re

gigs = re.compile(r'(\d\d?.\d{2}.\d\d+)\s?(w+)')

gigsreverse = re.compile(r'(w+)\s?(\d\d?.\d{2}.\d\d+)')

djdates = gigs.finditer()
djdatesreverse = gigsreverse.finditer()
gigdates = []
venues = []

for match in djdates:
    gigdates.append(match.group(1))
    venues.append(match.group(2))

for match in djdatesreverse:
    gigdates.append(match.group(2))
    venues.append(match.group(1))
