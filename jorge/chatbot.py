# Grappes: Chatbot
# Model builder

#_LIB___________________
import nltk, json, pickle, random, wikipedia, pywhatkit
import numpy as np
from nltk.stem import SnowballStemmer
from tensorflow.keras.models import load_model

stemmer = SnowballStemmer("spanish")
modelo = load_model("Chatbot_modelo.h5")
intents = json.loads(open("intents.json").read())
palabras = pickle.load(open("palabras.pkl", "rb"))
clases = pickle.load(open("clases.pkl", "rb"))

def clean_up_sentences(sentence):
    sentence_words=nltk.word_tokenize(sentence)
    sentence_words=[stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentences, palabras, show_details=True):
    sentences_words = clean_up_sentences(sentences)
    bag = [0] * len(palabras)
    for i in sentences_words:
        for j, w, in enumerate(palabras):
            if w == i:
                bag[j]=1
    return(np.array(bag))

def predict_class(sentences, modelo):
    p = bow(sentences,palabras,show_details=False)    
    res = modelo.predict(np.array([p]))[0]   
    ERROR_THRESHOLD = 0.65   
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD] 
    results.sort(key = lambda x: x[1], reverse = True)  
    return_list = []    
    for r in results:   
        return_list.append({"intent": clases[r[0]], "probability": str(r[1])})
    print("accurracy:", return_list[0]["probability"])
    return return_list

def get_response(ints, intents_json, text):
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"] 
    for i  in list_of_intents: 
        if (i["tag"] == tag):
            result = random.choice(i["responses"])
            break
        if(tag == "contactar_agente"):
            print("done")
        if(tag == "trackear_paquete"):
            print("done")
        if(tag == "programar_envios"):
            print("done")
        if(tag == "cotizacion"):
            print("done")
        if(tag == "mostrar_info"):
            print("done")
    return result, 0

def bot(text):
    ints = predict_class(text,modelo)
    res1, res2 = get_response(ints, intents, text)   
    return res1, res2

res, res1 = bot("hola")

print(res, res1)
