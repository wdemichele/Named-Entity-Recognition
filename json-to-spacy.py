TEXT_JSON = {"classes":["NAME","LICENSE NUMBER","ADDRESS","DATE OF BIRTH","EXPIRY DATE"],"annotations":[["DRIVER LICENSE VICTORIA  AUSTRALIA LICENCE NO JANE CITIZEN 98765432 77 SAINT PARADE KEW EAST VIC 3102 LICENCE EXPIRY DATE OF BIRTH 20-05-2019 29-07-1983 LICENCE TYPE CONDITIONS CAR SBEAVX vic roac",{"entities":[[46,58,"NAME"],[59,67,"LICENSE NUMBER"],[68,101,"ADDRESS"],[131,141,"EXPIRY DATE"],[142,152,"DATE OF BIRTH"]]}]]}

text = []

for annotation in TEXT_JSON["annotations"]:
    entities = {'entities':[]}
    for entity in annotation[1]["entities"]:
        entities["entities"].append(tuple(entity))
    text.append((annotation[0],entities))

print(text)