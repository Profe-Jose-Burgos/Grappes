#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

def open_csv(file):
    track=pd.read_csv(file,sep=";")
    return track

file="Grappes.csv"
df=open_csv(file)

num_track=df["No.Tracking"]
nombre=df["Nombre"]
user=df["Usuario"]
tel=df["Teléfono"]
correo=df["Correo"]
status=df["Estado"]

data={"No.Tracking":num_track,"Nombre":nombre,"Usuario":user,"Teléfono":tel,"Correo":correo,"Estado":status}

grappes_tracking=pd.DataFrame(data)
grappes_tracking.set_index("No.Tracking",inplace=True)
#grappes_tracking

def buscar_status(x):
    for i in range(len(grappes_tracking)):
        if x is in df.iloc[i]["No.Tracking"]:
            print ()
        #print (df.iloc[i]["No.Tracking"])
        
    #df.grappes_tracking.isin([])
    
buscar_status()


# In[ ]:




