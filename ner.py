import spacy
import sys
import json
import pymongo
from datetime import datetime
import re
import os

MONGODB = "mongodb+srv://spinifexit:SpinifexIT@cluster0.qrflpxo.mongodb.net/?retryWrites=true&w=majority"

def main(docname, classification, model, input, user):
    
    client = pymongo.MongoClient(MONGODB)
    db = client['test']
    collection = db["smart-keywords"]
    smartwords = []
    
    if (classification == "Invoice"):
        f = open(input)
        input = json.load(f)
        for key in input[0]['headerFields']:
            if ("value" in input[0]['headerFields'][key]):
                if (input[0]['headerFields'][key]["value"] != ''):
                    key = key.title()
                    smartwords.append({
                    "label" : key,
                    "value" : str(input[0]['headerFields'][key]["value"]).strip()
                })
        f.close()
    elif (classification == "Identification" or classification == "Vaccination"):
        nlp = spacy.load(model)
        nlp.pipe_names
        doc = nlp(input)
        for ent in doc.ents:
            smartwords.append({
                "label" : ent.label_,
                "value" : ent.text.strip()
            })
    
    directory = os.path.dirname(os.path.abspath(__file__))
    print(directory)
    keywords = []
    f = open(directory + "\BERT-keywords.json")
    BERT_text = json.load(f)
    for key in BERT_text:
        keywords.append(key["word"])
    f.close()
    
    nlp = spacy.load("en_core_web_sm")
    nlp.pipe_names
    doc = nlp(input)
    for ent in doc.ents:
        keywords.append(ent.text.strip())
    
    keywords = list(dict.fromkeys(keywords))
    
    smart_document = {
        "type" : classification,
        "document_name" : docname,
        "file_address" : "./" + user + "/rpa/" + classification + "/" + docname,
        "keywords" : keywords,
        "smart_words" : smartwords,
        "user" : user,
        "storage_date" : datetime.today()
    }
    collection.insert_one(smart_document)

main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])