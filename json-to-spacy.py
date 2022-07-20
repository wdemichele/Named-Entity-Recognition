TEXT_JSON = {
    "classes": ["NAME", "DATE", "COMPANY", "LOCATION", "JOB", "DOCUMENT NUMBER", "HEALTH IDENTIFIER", "VALID FROM"],
    "annotations": [
        ["PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA ANDREW JOHNSON  LICENCE NO 036143581 21 CREW ST BURWOOD VIC 3111 LICENCE EXPIRY DATE OF BIRTH 11-11-2024 04-07-1964 LICENCE TYPE CONDITIONS CAR 710200 P1 END DATE vicroads 03-12-2020", {
            "entities": [
                [47, 61, "NAME"],
                [74, 83, "DOCUMENT NUMBER"],
                [84, 111, "LOCATION"],
                [141, 151, "DATE"],
                [152, 162, "DATE"],
                [219, 229, "DATE"]
            ]
        }],
        ["PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA ANDREW JOHNSON  LICENCE NO 036143581 21 CREW ST BURWOOD VIC 3111 LICENCE EXPIRY DATE OF BIRTH 11-11-2024 04-07-1964 LICENCE TYPE CONDITIONS CAR 710200 P1 END DATE vicroads 03-12-2020", {
            "entities": [
                [47, 61, "NAME"],
                [74, 83, "DOCUMENT NUMBER"],
                [84, 111, "LOCATION"],
                [141, 151, "DATE"],
                [152, 162, "DATE"],
                [219, 229, "DATE"]
            ]
        }]
    ]
}

text = []

for annotation in TEXT_JSON["annotations"]:
    entities = {'entities':[]}
    for entity in annotation[1]["entities"]:
        entities["entities"].append(tuple(entity))
    text.append((annotation[0],entities))

print(text)