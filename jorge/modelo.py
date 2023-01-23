# Grappes: Chatbot
# Model builder

#_LIB___________________
import json, pickle, nltk, numpy as np
from tensorflow.keras import Secuential
from tensorflow.keras.layer import Conv2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizer import SGD, Adam
from nltk.stem import SnowballStemmer

stemmer = Snowballstemer("spanish")
ignored_words = ["?", "¿", "!", "¡", "[", "]", "{", "}", "(", ")", "+", "-", "*", "/"]
json_data = open("intents.json").read()
intents = json.loads(json_data)

#_FUNCTIONS_______________
def tokenizador():
    palabras = []
    clases = []
    documentos = []

    for intent in intents["intents"]:
        for pattern in intents["patterns"]:
            token = nltk.word_tokenize(pattern)
            palabras.extend(token)
            documentos.append((token, intent["tag"]))
            if intent["tag"] not in clases:
                clases.append(intent["tag"])
    return palabras, clases, documentos

def lematizador(palabras, clases, documentos):
    palabras = [stemmer.stem(token.lower()) for token in palabras if token not in ignored_words]
    pickle.dump(palabras, open("palabras.pkl","wb"))
    pickle.dump(clases, open("clases.pkl","wb"))
    return palabras

def entrenamiento(palabras, clases, documentos):
    entrenamiento = []
    output_empty = [0] * len(clases)
    for documento in documentos:
        bolsa = []
        patrones = documento[0]
        patrones = [stemmer.stem(palabras.lower()) for palabra in patrones if palabra not in ignored_words]
        for palabra in palabras:
            bolsa.append(1) if palabra in patrones else bolsa.append(0)
            salida = list(output_empty)
            salida[clases.index(documento[1])] = 1
    entrenamiento = np.array(entrenamiento)
    x = list(entrenamiento[:, 0])
    y = list(entrenamiento[:, 1])
    return x, y

def modelo(x, y):
    modelo = Secuential()
    modelo.add(Dense(128, input_shape=(len(x[0]), ), activation="relu"))
    modelo.add(Dropout(0.5))
    modelo.add(Dense(64, ativation="relu"))
    modelo.add(Dropput(0.5))
    modelo.add(Dense(len(y[0]), ativation="relu"))
    sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    #adam = Adam(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True) <------ try
    try:
        print("Utilizando Adam...")
        modelo.compile(loss="categorical_crossentropy", optimizer=adam, metrics=["accuracy"])
        data = modelo.fit(np.array(x), np.array(y), epochs=1000, batch_size=5, verbose=0)
        modelo.save("Chatbot_modelo.h5", data)
    except:
        print("Utilizando SGD...")
        modelo.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])
        data = modelo.fit(np.array(x), np.array(y), epochs=1000, batch_size=5, verbose=0)
        modelo.save("Chatbot_modelo.h5", data)

def crear_modelo():
    palabras, clases, documentos = tokenizador()
    palabras = lematizador(palabras, clases, documentos)
    x, y = entrenamiento(palabras, clases, documentos)
    modelo(x, y)



    
