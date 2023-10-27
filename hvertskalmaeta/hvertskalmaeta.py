#! /usr/bin/env python3
"""
Kattis hvert skal maeta problem.

Given the city determine whether Reykjavi or Akureyri is closer

Algorithm:
    1. Read input data into function
    2. Consult the city dictonary to make sure it's in data set
    3. Based on input and dictinary determine which city it's closest to
    4. Print/Return the result
"""
__author__ = "Eli St. Onge"
__date__ = "Oct 23, 2021"

# Dictionary of the cities and which of the two it's closest too
cityDict = {
    "Reykjavik": "Reykjavik",
    "Kopavogur": "Reykjavik",
    "Hafnarfjordur": "Reykjavik",
    "Reykjanesbaer": "Reykjavik",
    "Akureyri": "Akureyri",
    "Gardabaer": "Reykjavik",
    "Mosfellsbaer": "Reykjavik",
    "Arborg": "Reykjavik",
    "Akranes": "Reykjavik",
    "Fjardabyggd": "Akureyri",
    "Mulathing": "Akureyri",
    "Seltjarnarnes": "Reykjavik"
}


# Returns city that is closeset based on dictionary
# Otherwise returns Error as str
def answer(city: str) -> str:
    if city in cityDict:
        print(cityDict[city])
        return cityDict[city]
    else:
        print("Error: no matching data")
        return "Error"


if __name__ == "__main__":
    city = input()
    answer(city)
