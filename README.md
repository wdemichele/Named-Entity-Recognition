# Named Entity Extraction

## Create a new extraction model
### Extract PDF text
Perform Optical Character Recognition (OCR) to extract text from PDF files. Can use Sap Robot Process Automation to automate this process using SAP OCR.

### Create training data
Use the linked tool [^1] to be able to extract labelled information from a textfile
Data will be extracted into a JSON file

### Convert JSON extracted data to spaCy formatting
SpaCy has a specialised tuple-based data format [^2] 
Use the json-to-spacy.py file to convert json data to spaCy data

### Getting extra data
Use randomise-data.py to generate extra data entries. Ensure that each data field has an extensive list of values, to prevent data from getting stale and resulting overfitting.
Adapt as needed

### Train model
With enough data you can now use train_model.py to train a model from the data provided in spaCy format. Choose the number of iterations you wish, remembering that to few iterations may
cause the model to be unfamiliar with the required extraction extractions, but too many 
iterations may lead to overtraining, causing the model to be dependant on the training data.

## Extract Keywords
You can now use your trained model to extract data as recognised by the model. This will convert the provided text file of input into a JSON file consisting of the metadata of the document including
the extracted:

#### Smart Words
Smart words are complex, labelled data extracted using tailored pre-trained spaCy pipelines, or SAP Information Extraction where relevant.
They allow complex query searches of the database, 
i.e. "Find all users with an expired drivers licence"

Smartwords examples:
- “Document Number” : “INV12345”
- "Name" : "William De Michele"
- “License Expiry” : “27/03/2026”

#### Key Words
Key words are much simpler informaton extraction, that can be performed on any document even if the document is an untrained classification with no previous spaCy model trained for it. 
It uses a Bidirectional Encoder Representations from Transformers (BERT) API from HuggingFace, and consolidates these keywords with the spaCy Named Entity Recognition core English package.
Queries performed on this data is much more limited, relying on simple "find 'x' word in database".

Keyword examples:
- “1912 Harvest Ln NY”, 
- “John Doe”, 
- “27/08/2019”, 
- "East Repair Inc“

## Running the Named Entity Recognition tool
This tool relies on many outputs provided by the SAP Robot Process Automation built by SpinifexIT, "*Document Classification with Extraction to STRATO Storage*". As such many of the contextual files, are required before running the extraction process.
It is recommended to only use this tool in context of the RPA, however it may be adapted as needed.

If used outside of the RPA, run the file ner.py, providing the 3 arguments:
- Document Name
- Document Classification
- User Name

This will then store a *Smart Document* object into the linked MongoDB database, that can then be queried using the *RPA-Document-Classification* query online tool. 

#### SAP Robot Process Automation dependent files
In cases of the classification being that of a:
- Invoice
- Payment Advice
- Purchase Summary
the SAP built in information extraction is used, as it has been found to perform with greater consistency.

In cases of an extraction template being used, as per the Sample Form example given, this will be handled by the SAP Information Extraction by Template method.

All documents will have keywords compiled within the automation, using an API call to HuggingFace BERT API.

All of these seperate events will require JSON files to be stored at the file directory of the NER tool, and will be used by the tool. Please config as necessary if wishing to use the tool outside of the RPA.


[^1]: https://tecoholic.github.io/ner-annotator/
[^2]: https://spacy.io/api/data-formats