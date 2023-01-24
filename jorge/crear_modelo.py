# Grappes: Chatbot
# Model builder

#_LIB___________________
import json, pickle, nltk, numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import SGD
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("spanish")
ignored_words = ["?", "¿", "!", "¡"]
json_data = open("intents.json").read()
intents = json.loads(json_data)

#_FUNCTIONS_______________
def tokenizador():
    palabras=[]
    clases=[]
    documentos=[]

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            w=nltk.word_tokenize(pattern)
            palabras.extend(w)
            documentos.append((w,intent["tag"]))
            if intent["tag"] not in clases:
                clases.append(intent["tag"])     
    return palabras,clases,documentos

def lematizador(palabras, clases, documentos):
    palabras = [stemmer.stem(token.lower()) for token in palabras if token not in ignored_words]
    palabras2 = palabras
    pickle.dump(palabras, open("palabras.pkl","wb"))
    pickle.dump(clases, open("clases.pkl","wb"))
    return palabras2

def entrenamiento(palabras, clases, documentos):
    entrenamiento=[]
    output_empty=[0]*len(clases)
    for doc in documentos: 
        bolsa=[]
        pattern_words=doc[0]
        pattern_words= [stemmer.stem(word.lower()) for word in pattern_words  if word not in ignored_words ]
        for palabra in palabras:
            bolsa.append(1) if palabra in pattern_words else bolsa.append(0) 
        output_row =list(output_empty)
        output_row[clases.index(doc[1])] = 1
        entrenamiento.append([bolsa,output_row])
    entrenamiento1=np.array(entrenamiento) 
    x= list(entrenamiento1[:,0])
    y= list(entrenamiento1[:,1])  
    return x, y

def modelo(x, y):
    modelo = Sequential()
    modelo.add(Dense(128, input_shape=(len(x[0]),), activation='relu'))
    modelo.add(Dropout(0.5))
    modelo.add(Dense(64,activation='relu'))
    modelo.add(Dropout(0.5))
    modelo.add(Dense(len(y[0]),activation='softmax'))
    sgd=SGD(learning_rate=0.01,decay=1e-6,momentum=0.9,nesterov=True) 
    print("Using sgd...")
    modelo.compile(loss="categorical_crossentropy",optimizer=sgd,metrics=["accuracy"])
    hist=modelo.fit(np.array(x),np.array(y),epochs=600,batch_size=5,verbose=0)
    modelo.save("Chatbot_modelo.h5",hist)
    print("The model was created succesfuly...")
    
def crear_modelo():
    palabras, clases, documentos = tokenizador()
    palabras2 = lematizador(palabras, clases, documentos)
    x, y = entrenamiento(palabras2, clases, documentos)
    modelo(x, y) 
