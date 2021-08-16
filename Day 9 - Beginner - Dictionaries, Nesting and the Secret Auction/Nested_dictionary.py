travel_log = [
    {"country": "France",
     "visits": 34,
     "cities_visited": ["Paris", "Lille", "Dijon"]
     },
    {
        "country": "Germany",
        "Visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    }
]


def add_new_country(country, visits, cities_visited):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Peterson"])
print(travel_log)
