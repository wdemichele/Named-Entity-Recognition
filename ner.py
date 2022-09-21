import spacy, sys, json, pymongo, os, re
from datetime import datetime

MONGODB = "mongodb+srv://spinifexit:SpinifexIT@cluster0.qrflpxo.mongodb.net/?retryWrites=true&w=majority"

def camel_case_split(identifier):
    """
    Standardises text from SAP Extract Outsput to standard text
    SAP Extract: "purchaseOrder" -> "Purchase order"
    """
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return ' '.join(map(str, [m.group(0) for m in matches])) 

def extract_data(docname, classification, user):
    """
    Function takes as input: Document Name, Document Classification, User Name
    Uses information extraction method based on the Document Classification
    """
    
    # MongoDB collection
    client = pymongo.MongoClient(MONGODB)
    db = client['test']
    collection = db["smart-keywords"]
    
    # smartwords are labelled important information
    smartwords = []
    
    # grabs current directory location
    directory = os.path.dirname(os.path.abspath(__file__))
    
    # these classifications extractions are handles by SAP extract
    if (classification == "Invoice" or classification == "Payment Advice" or classification == "Purchase Order" or classification == "Sample Form"):
        
        # this is the file that information is extracted to in the RPA automation
        input = directory + "\\extracted.json"
        f = open(input)
        input = json.load(f)
        
        # standardising the text output to json format
        for key in input[0]['headerFields']:
            if ("value" in input[0]['headerFields'][key]):
                if (input[0]['headerFields'][key]["value"] != ''):
                    smartwords.append({
                    "label" : camel_case_split(key),
                    "value" : str(input[0]['headerFields'][key]["value"]).strip()
                    })
                    
        f.close()
    
    # these methods are handled by spaCy
    elif (classification == "Vaccination" or classification == "Identification"):
        
        # load the relevant model
        nlp = spacy.load(directory + "\Models\\"+ classification + "-model")
        nlp.pipe_names
        
        # converting doc to list of strings
        with open(directory + "\\text.txt") as f:
            lines = f.readlines()
            listToStr = ' '.join(map(str, lines))
            
        # using spacy model to extract from list of strings
        doc = nlp(listToStr)
        for ent in doc.ents:
            smartwords.append({
                "label" : ent.label_,
                "value" : ent.text.strip() # strip to standardise excess spaces
            })
    
    # keywords are unlabelled important information
    keywords = []
    
    # BERT keywords were extracted using the Hugging Face API in the automation
    f = open(directory + "\BERT-keywords.json")
    BERT_text = json.load(f)
    for key in BERT_text:
        keywords.append(key["word"])
    f.close()
    
    # spaCy en_cor_web_sm is a standard spaCy general purpose library
    nlp = spacy.load("en_core_web_sm")
    nlp.pipe_names
    with open(directory + "\\text.txt") as f:
        lines = f.readlines()
        listToStr = ' '.join(map(str, lines))
    
    # extract using general purpose model to build on our keywords (this will likely lead to repeats)
    doc = nlp(listToStr)
    for ent in doc.ents:
        keywords.append(ent.text.strip())
    
    keywords = list(dict.fromkeys(keywords))
    
    # build document object to be posted to Database
    smart_document = {
        "type" : classification,
        "document_name" : docname,
        "file_address" : "./" + user + "/rpa/" + classification + "/" + docname, # to be configured for STRATO Storage
        "keywords" : keywords,
        "smart_words" : smartwords,
        "user" : user,
        "storage_date" : datetime.today()
    }
    collection.insert_one(smart_document)

# start program by running file with arguments: Document Name, Document Classification, User Name
extract_data(sys.argv[1], sys.argv[2], sys.argv[3])