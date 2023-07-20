from pprint import pprint
from collections import Counter
from readrides import read_rides_as_dictionary

records = read_rides_as_dictionary("Data/ctabus.csv")

# 1. How many bus routes exist in Chicago?
routes = set()
for r in records:
    routes.add(r["route"])
print(len(routes))

# 2. How many people rode the number 22 bus on February 2, 2011?
#    What about any route on any date of your choosing?
for r in records:
    if r["route"] == "22" and r["date"] == "02/02/2011":
        print(r["rides"])
        break

# 3. What is the total number of rides taken on each bus route?
counter = Counter()

for r in records:
    counter[r["route"]] += r["rides"]

pprint(counter)

# 4. What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
counter_2001 = Counter()
counter_2011 = Counter()

for r in records:
    if r["date"].endswith("2001"):
        counter_2001[r["route"]] += r["rides"]
    elif r["date"].endswith("2011"):
        counter_2011[r["route"]] += r["rides"]

diffs = {}

for route in routes:
    diffs[route] = counter_2011[route] - counter_2001[route]

pprint(sorted(diffs.items(), key=lambda x: x[1], reverse=True)[:5])
