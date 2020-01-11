#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv , json

csvFilePath = "2020-01-11_epl_players.csv"
jsonFilePath = "2020-01-11_epl_players.json"
arr = []

with open (csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    print(csvReader)
    for csvRow in csvReader:
        arr.append(csvRow)

print(arr)

# write the data to a json file
with open(jsonFilePath, "w") as jsonFile:
	# Make it more readable and pretty 😍
    jsonFile.write(json.dumps(arr, indent = 4))