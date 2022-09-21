import spacy, sys, json, pymongo, os, re
from datetime import datetime

MONGODB = "mongodb+srv://spinifexit:SpinifexIT@cluster0.qrflpxo.mongodb.net/?retryWrites=true&w=majority"

def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return ' '.join(map(str, [m.group(0) for m in matches])) 

def main(docname, classification, user):
    
    client = pymongo.MongoClient(MONGODB)
    db = client['test']
    collection = db["smart-keywords"]
    smartwords = []
    directory = os.path.dirname(os.path.abspath(__file__))
    
    if (classification == "Invoice" or classification == "Payment Advice" or classification == "Purchase Order" or classification == "Sample Form"):
        input = directory + "\\extracted.json"
        f = open(input)
        input = json.load(f)
        for key in input[0]['headerFields']:
            if ("value" in input[0]['headerFields'][key]):
                if (input[0]['headerFields'][key]["value"] != ''):
                    smartwords.append({
                    "label" : camel_case_split(key),
                    "value" : str(input[0]['headerFields'][key]["value"]).strip()
                    })
                    
        f.close()
    # elif (spacy.util.is_package(model)):
    elif (classification == "Vaccination" or classification == "Identification"):
        nlp = spacy.load(directory + "\Models\\"+ classification + "-model")
        nlp.pipe_names
        with open(directory + "\\text.txt") as f:
            lines = f.readlines()
            listToStr = ' '.join(map(str, lines))
        doc = nlp(listToStr)
        for ent in doc.ents:
            smartwords.append({
                "label" : ent.label_,
                "value" : ent.text.strip()
            })
    
    keywords = []
    f = open(directory + "\BERT-keywords.json")
    BERT_text = json.load(f)
    for key in BERT_text:
        keywords.append(key["word"])
    f.close()
    
    nlp = spacy.load("en_core_web_sm")
    nlp.pipe_names
    with open(directory + "\\text.txt") as f:
        lines = f.readlines()
        listToStr = ' '.join(map(str, lines))
        
    doc = nlp(listToStr)
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

main(sys.argv[1], sys.argv[2], sys.argv[3])