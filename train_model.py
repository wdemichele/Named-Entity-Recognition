import spacy
import random
from spacy.training import Example

# input data
TRAIN_DATA = [('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA KRISTIAN VALENZUELA LICENCE NO 49342304 U 2 20 13 MILLS STREET DALYSTON 3992 LICENCE EXPIRY DATE OF BIRTH 12-01-2023(A)28-10-2020S CAR SBEAVX vic roads', {'entities': [(47, 66, 'NAME'), (78, 86, 'DOCUMENT/LICENSE NUMBER'), (94, 123, 'ADDRESS'), (153, 163, 'EXPIRATION DATE'), (166, 176, 'DATE OF BIRTH')]}), ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA WESTON MERRIMAN LICENCE NO 5025995 U 2 20 15 WHITEWAYS RD MAJOR 3988 LICENCE EXPIRY DATE OF BIRTH 19-03-2027(A)08-09-2012S CAR SBEAVX vic roads', {'entities': [(47, 62, 'NAME'), (74, 81, 'DOCUMENT/LICENSE NUMBER'), (89, 115, 'ADDRESS'), (145, 155, 'EXPIRATION DATE'), (158, 168, 'DATE OF BIRTH')]}), 
              ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA a KAI EMERY LICENCE NO MCINNENY 38700594 200A JIM RD WESTBOURNE 9845 LICENCE EXPIRY DATE OF BIRTH 18-06-2023(B)07-07-1962R SBEAVX vic roads', {'entities': [(49, 58, 'NAME'), (79, 87, 'DOCUMENT/LICENSE NUMBER'), (88, 115, 'ADDRESS'), (145, 155, 'EXPIRATION DATE'), (158, 168, 'DATE OF BIRTH')]}), ('DRIVER LICENSE VICTORIA  AUSTRALIA LICENCE NO TERRI NOVAK 31775567 55 HEBBARD ST ST KILDA 3182 LICENCE EXPIRY DATE OF BIRTH 24-07-2026 28-04-1956 TYPE CONDITIONS CAR SBEAVX vic roads', {'entities': [(46, 57, 'NAME'), (58, 66, 'DOCUMENT/LICENSE NUMBER'), (67, 94, 'ADDRESS'), (124, 134, 'EXPIRATION DATE'), (135, 145, 'DATE OF BIRTH')]}), 
              ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA a GRACIE BEARDEN LICENCE NO MCINNENY 5025995 30 NAPIER TCE LONDON 3111 LICENCE EXPIRY DATE OF BIRTH 26-07-2023(B)18-12-1956R SBEAVX vic roads', {'entities': [(49, 63, 'NAME'), (84, 91, 'DOCUMENT/LICENSE NUMBER'), (92, 117, 'ADDRESS'), (147, 157, 'EXPIRATION DATE'), (160, 170, 'DATE OF BIRTH')]}), ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA LUCINDA MCSHERRY LICENCE NO 76225746 U 2 20 25 LENNOX STYARRAVILLE 3013 LICENCE EXPIRY DATE OF BIRTH 14-07-2031(A)08-02-2015S CAR SBEAVX vic roads', {'entities': [(47, 63, 'NAME'), (75, 83, 'DOCUMENT/LICENSE NUMBER'), (91, 119, 'ADDRESS'), (149, 159, 'EXPIRATION DATE'), (162, 172, 'DATE OF BIRTH')]}), 
              ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA HASSAN FROST LICENCE NO 76225746 U 2 20 161 HIGH ST PRAHRAN 2112 LICENCEEXPIRY DATE OF BIRTH 19-04-2021(A)03-11-2019S CAR SBEAVX vic roads', {'entities': [(47, 59, 'NAME'), (71, 79, 'DOCUMENT/LICENSE NUMBER'), (87, 111, 'ADDRESS'), (141, 151, 'EXPIRATION DATE'), (154, 164, 'DATE OF BIRTH')]}), ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA JESSE TEJEDA LICENCE NO 84455734 1 STOKESAY ST SLOUGH 3924 LICENCE EXPIRY DATE OF BIRTH 18-06-2023(B)03-02-1982NDITIONS CAR SBEAVX vic roads', {'entities': [(47, 59, 'NAME'), (71, 79, 'DOCUMENT/LICENSE NUMBER'), (80, 105, 'ADDRESS'), (135, 145, 'EXPIRATION DATE'), (148, 158, 'DATE OF BIRTH')]}), 
              ('DRIVER LICENCE VICTORIA AUSTRALIA DAKOTA YARBROUGH LICENCE NO 36968264 U 12 74 MCLEANS ROAD DUNDOWRAN 4655 LICENCE EXPIRY DATE OF BIRTH 18-01-2022 29-01-1939CE TYPE CONDITIONS CAR SBEAVX vic roa', {'entities': [(34, 50, 'NAME'), (62, 70, 'DOCUMENT/LICENSE NUMBER'), (76, 106, 'ADDRESS'), (136, 146, 'EXPIRATION DATE'), (147, 157, 'DATE OF BIRTH')]}), ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA PETER DIMITRIOU LICENCE NO 73130738 U 2 20 30 NAPIER TCE LONDON 3111 LICENCE EXPIRY DATE OF BIRTH 11-11-2027(A)15-04-2007S CAR SBEAVX vic roads', {'entities': [(47, 62, 'NAME'), (74, 82, 'DOCUMENT/LICENSE NUMBER'), (90, 115, 'ADDRESS'), (145, 155, 'EXPIRATION DATE'), (158, 168, 'DATE OF BIRTH')]}), 
              ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA HASSAN FROST LICENCE NO 61585328U 2 20 94 CUMBERLAND ST SUNSHINE 6839 LICENCE EXPIRY DATE OF BIRTH 07-06-2028(A)04-01-1995S CAR SBEAVX vic roads', {'entities': [(47, 59, 'NAME'), (71, 79, 'DOCUMENT/LICENSE NUMBER'), (87, 117, 'ADDRESS'), (147, 157, 'EXPIRATION DATE'), (160, 170, 'DATE OF BIRTH')]}), ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA CLAYTON TSAI LICENCE NO 62957068 U 2 20 63 EURACK CT NARRAWA 2583 LICENCE EXPIRY DATE OF BIRTH 20-09-2023(A)06-02-1998S CAR SBEAVX vic roads', {'entities': [(47, 59, 'NAME'), (71, 79, 'DOCUMENT/LICENSE NUMBER'), (87, 112, 'ADDRESS'), (142, 152, 'EXPIRATION DATE'), (155, 165, 'DATE OF BIRTH')]}),
              ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA KAI EMERY LICENCE NO 77344231 92 OLD GAYNDAH ROAD BEAVER ROCK 4650 LICENCE EXPIRY DATE OF BIRTH 02-10-2030 15-03-2010 CONDITIONS CAR SBEAVX vic roads', {'entities': [(47, 56, 'NAME'), (68, 76, 'DOCUMENT/LICENSE NUMBER'), (77, 113, 'ADDRESS'), (143, 153, 'EXPIRATION DATE'), (154, 164, 'DATE OF BIRTH')]}), ('DRIVER LICENSE VICTORIA  AUSTRALIA LICENCE NO ZAVIER MILES 90575532 59 COFTON CL TYRINGHAM 2453 LICENCE EXPIRY DATE OF BIRTH 02-02-2025 10-11-1924 TYPE CONDITIONS CAR SBEAVX vic roads', {'entities': [(46, 58, 'NAME'), (59, 67, 'DOCUMENT/LICENSE NUMBER'), (68, 95, 'ADDRESS'), (125, 135, 'EXPIRATION DATE'), (136, 146, 'DATE OF BIRTH')]}), 
              ('DRIVER LICENCE VICTORIA AUSTRALIA WESTON MERRIMAN LICENCE NO 39964566 U 12 38 SAVAGES RD ARCHERFIELD 4108 LICENCE EXPIRY DATE OF BIRTH 20-09-2023 03-02-1982CE TYPE CONDITIONS CAR SBEAVX vic roa', {'entities': [(34, 49, 'NAME'), (61, 69, 'DOCUMENT/LICENSE NUMBER'), (75, 105, 'ADDRESS'), (135, 145, 'EXPIRATION DATE'), (146, 156, 'DATE OF BIRTH')]}), ('DRIVER LICENCE VICTORIA AUSTRALIA ALANNAH CHOPRA LICENCENO 57388372 U 12 4 BEARCROFT GD MICKLETON 3332 LICENCE EXPIRY DATE OF BIRTH 23-08-2027 15-11-1973CE TYPE CONDITIONS CAR SBEAVX vic roa', {'entities': [(34, 48, 'NAME'), (60, 68, 'DOCUMENT/LICENSE NUMBER'), (74, 103, 'ADDRESS'), (133, 143, 'EXPIRATION DATE'), (144, 154, 'DATE OF BIRTH')]}), ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA GRACIE BEARDEN  LICENCE NO 40378180 55 HEBBARD ST ST KILDA 3182 LICENCE EXPIRY DATE OF BIRTH 14-09-2017 04-04-1967IONS CAR SBEAVX vic roads', {'entities': [(47, 61, 'NAME'), (74, 82, 'DOCUMENT/LICENSE NUMBER'), (83, 110, 'ADDRESS'), (140, 150, 'EXPIRATION DATE'), (151, 161,'DATE OF BIRTH')]}), ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA ALEXANDRE CLEMENT LICENCE NO 62957068 108 EDISON RD WALSALL 1223 LICENCE EXPIRY DATE OF BIRTH 03-10-2022 19-10-1966 CONDITIONS CAR SBEAVX vic roads', {'entities': [(47, 64, 'NAME'), (76, 84, 'DOCUMENT/LICENSE NUMBER'), (85, 111, 'ADDRESS'), (141, 151, 'EXPIRATION DATE'), (152, 162, 'DATE OF BIRTH')]}), ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA CLAYTON TSAI LICENCE NO 20013336 8 THE CROFT SHERBURN HILL 9010 LICENCE EXPIRY DATE OF BIRTH 24-07-2026 01-06-1952 CONDITIONS CAR SBEAVX vic roads', {'entities': [(47, 59, 'NAME'), (71, 79, 'DOCUMENT/LICENSE NUMBER'), (80, 110, 'ADDRESS'), (140, 150, 'EXPIRATION DATE'), (151, 161, 'DATE OF BIRTH')]}), ('DRIVER LICENSE VICTORIA  AUSTRALIA LICENCE NO ALEXCIA CERDA 99523853 161 HIGH ST PRAHRAN 2112 LICENCE EXPIRY DATE OF BIRTH 14-02-2024 24-02-1998 TYPE CONDITIONS CAR SBEAVX vic roads', {'entities': [(46, 59, 'NAME'), (60, 68, 'DOCUMENT/LICENSE NUMBER'), (69, 93, 'ADDRESS'), (123, 133, 'EXPIRATION DATE'), (134, 144, 'DATE OF BIRTH')]}), ('DRIVER LICENCE VICTORIA AUSTRALIA DREW VAIL  ADAMS LICENCE NO 21973701 313 ALBION ST SOUTHWICK 6778 LICENCE EXPIRY DATE OF BIRTH 18-01-2022 20-12-201183 LICENCE TYPE CONDITIONS CAR SBEAVX vic roads', {'entities': [(34, 43, 'NAME'), (62, 70, 'DOCUMENT/LICENSE NUMBER'), (71, 99, 'ADDRESS'), (129, 139, 'EXPIRATION DATE'), (140, 150, 'DATE OF BIRTH')]}), ('LICENCE DRIVER AUSTRALIA   IRA IRELAND LICENCE NO  76225746 22 BROOK LN CLAYTON 5989 LICENCE EXPIR DATE OF BIRTH 18-06-2023 04-01-19951983 LICENCE TYPE CONDITIONS CAR SBEAVX', {'entities': [(27, 38, 'NAME'), (51, 59, 'DOCUMENT/LICENSE NUMBER'), (60, 84, 'ADDRESS'), (113, 123, 'EXPIRATION DATE'), (124, 134, 'DATE OF BIRTH')]}), ('DRIVER LICENSE VICTORIA  AUSTRALIA LICENCE NO LUCINDA MCSHERRY 90575532 1 BEGLEY ST NORMAN 4890 LICENCE EXPIRY DATE OF BIRTH 03-03-2025 04-01-199583 LICENCE TYPE CONDITIONS CAR SBEAVX vic roa', {'entities': [(46, 62, 'NAME'), (63, 71, 'LICENSE NUMBER'), (72, 95, 'ADDRESS'), (125, 135, 'EXPIRY DATE'), (136, 146, 'DATE OF BIRTH')]}), ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA JESSE TEJEDA LICENCE NO 53499197 94 GLOUCESTER AV WOODVILLE 5012 LICENCE EXPIRY DATE OF BIRTH 07-08-2029 25-02-1992 CONDITIONS CAR SBEAVX vic roads', {'entities': [(47, 59, 'NAME'), (71, 79, 'DOCUMENT/LICENSE NUMBER'), (80, 111, 'ADDRESS'), (141, 151, 'EXPIRATION DATE'), (152, 162, 'DATE OF BIRTH')]}), ('DRIVER LICENCE VICTORIA AUSTRALIA JANELL RITTER  ADAMS LICENCE NO 43214057 39 BURNLEY ST MASLIN BEACH 5170 LICENCE EXPIRY DATE OF BIRTH 25-05-2022 10-04-190583 LICENCE TYPE CONDITIONS CAR SBEAVX vic roads', {'entities': [(34, 47, 'NAME'), (66, 74, 'DOCUMENT/LICENSE NUMBER'), (75, 106, 'ADDRESS'), (136, 146, 'EXPIRATION DATE'), (147, 157, 'DATE OF BIRTH')]}), ('DRIVER LICENSE VICTORIA AUSTRALIA LICENCE NO PRISCILLA FORRESTER 30356277 1 BEGLEY ST NORMAN 4890 LICENCE EXPIRY DATE OF BIRTH 10-11-2028 28-02-1975 TYPE CONDITIONS CAR SBEAVX vic roads', {'entities': [(46, 65, 'NAME'), (66, 74, 'DOCUMENT/LICENSE NUMBER'), (75, 98, 'ADDRESS'), (128, 138, 'EXPIRATION DATE'), (139, 149, 'DATE OF BIRTH')]}), ('PROBATIONARY DRIVER LICENCE VICTORIA AUSTRALIA CAROL GARNER  LICENCE NO 82023414 2 WYLAMS CTG CROOK 8787 LICENCE EXPIRY DATE OF BIRTH 14-09-2017 19-11-1902IONS CAR SBEAVX vic roads', {'entities': [(47, 59, 'NAME'), (72, 80, 'DOCUMENT/LICENSE NUMBER'), (81, 104, 'ADDRESS'), (134, 144, 'EXPIRATION DATE'), (145, 155, 'DATE OF BIRTH')]}), ('DRIVER LICENSE VICTORIA  AUSTRALIA LICENCE NO HARRIS CREECH 09697588 6 RIDGEWAY ST BARRY 4128 LICENCE EXPIRY DATE OF BIRTH 14-09-2017 24-01-1967 LICENCE TYPE CONDITIONS CAR SBEAVX vic roads', {'entities': [(46, 59, 'NAME'), (60, 68, 'DOCUMENT/LICENSE NUMBER'), (69, 93, 'ADDRESS'), (123, 133, 'EXPIRY DATE'), (134, 144, 'DATE OF BIRTH')]}), 
              ('DRIVER LICENSE VICTORIA  AUSTRALIA LICENCE NO LAKEN MOYER 57511006 8 ANDERSON STREET BRACKEN RIDGE 4017 LICENCE EXPIRY DATE OF BIRTH 19-04-2021 24-04-2000 TYPE CONDITIONS CAR SBEAVX vic roads', {'entities': [(46, 57, 'NAME'), (58, 66, 'DOCUMENT/LICENSE NUMBER'), (67, 103, 'ADDRESS'), (133, 143, 'EXPIRATION DATE'), (144, 154, 'DATE OF BIRTH')]}), ('DRIVER LICENSE VICTORIA  AUSTRALIA LICENCE NO ALEXANDRE CLEMENT 99023683 70 DABINETT RD PURNONG 5238 LICENCE EXPIRY DATE OFBIRTH 21-10-2026 29-02-196983 LICENCE TYPE CONDITIONS CAR SBEAVX vic roa', {'entities': [(46, 63, 'NAME'), (64, 72, 'LICENSE NUMBER'), (73, 100, 'ADDRESS'), (130, 140, 'EXPIRY DATE'), (141, 151, 'DATE OF BIRTH')]})]
def train_spacy(data,iterations):
    """
    Takes spaCy formatted data and the number of iterations for the classifier to train on, and builds a spaCy model
    """
    TRAIN_DATA = data
    nlp = spacy.blank('en')  # create blank Language class
    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.add_pipe('ner', last=True)
       

    # add labels
    for _, annotations in TRAIN_DATA:
         for ent in annotations.get('entities'):
            ner.add_label(ent[2].strip())

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(iterations): # increasing the number of iterations by too much may lead to overtraining
            print("Staring iteration " + str(itn))
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)

                nlp.update([example], sgd=optimizer, losses=losses, drop=0.2)
            print(losses)
    return nlp

                
nlp = train_spacy(TRAIN_DATA, 30)

# Save our trained Model, use the same name as the classifier will output
modelfile = input("Enter your Model Name: ")
nlp.to_disk(".\\Models\\" + modelfile)

# Test with sample text
test_text = input("Enter your testing text: ")
doc = nlp(test_text)
for ent in doc.ents:
    print(ent.text, ent.label_)