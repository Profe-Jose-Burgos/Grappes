#!/usr/bin/env python
# coding: utf-8

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pandas as pd
import time

def open_csv(file):
    track=pd.read_csv(file,sep=";")
    return track

file="Grappes.csv"
df=open_csv(file)

num_track=df["NumTracking"]
nombre=df["Nombre"]
user=df["Usuario"]
tel=df["Teléfono"]
correo=df["Correo"]
status=df["Estado"]

data={"NumTracking":num_track,"Nombre":nombre,"Usuario":user,"Teléfono":tel,"Correo":correo,"Estado":status}

grappes_tracking=pd.DataFrame(data)
grappes_tracking.set_index("NumTracking",inplace=True)
#grappes_tracking

def buscar_status(x):
    for index, row in grappes_tracking.iterrows():
        if x in grappes_tracking.index:
            nombre=grappes_tracking["Nombre"][x]
            status=grappes_tracking["Estado"][x]
            email=grappes_tracking["Correo"][x]
            return nombre, status, email



num=int(input("Ingrese su número de tracking:"))        
nombre, status, email=buscar_status(num)
print(f"El paquete a nombre de {nombre} está a {status}.")
print(f"{email}")

try:
    if status == 'Retirado':
        time.sleep(1)
        sender = 'grappes.sic@hotmail.com'
        password = 'GrappesSic123'
        addressee = email
        subject = 'Tu orden_%s'%num
        body_message = 'Hola %s, \n\nTu producto ya lo has retirado con exito.'%nombre
        #Generando el Email
        menssage = MIMEMultipart()
        menssage['From'] = sender
        menssage['To'] = addressee
        menssage['Subject'] = subject
        menssage.attach(MIMEText(body_message,'plain'))
        print('Email send succesfully!')

except:
    print('Algo salio malllllll....')
































#Creando el mensaje Email
# time.sleep(1)
# sender = 'grappes.sic@hotmail.com'
# password = 'GrappesSic123'
# addressee = email
# subject = 'Tu orden_%s'%num
# body_message = 'Hola %s, \n\nTu producto ya lo has retirado con exito.'%nombre


#Generando el Email
# menssage = MIMEMultipart()
# menssage['From'] = sender
# menssage['To'] = addressee
# menssage['Subject'] = subject

#Conexion con el servidor Microsoft
sesion_smtp = smtplib.SMTP('smtp.office365.com',587)
sesion_smtp.starttls()
sesion_smtp.login(sender,password)
text = menssage.as_string()
sesion_smtp.sendmail(sender,addressee,text)
sesion_smtp.quit()


#Menú del cliente
# Indica por favor, en qué deseas que te ayude:
#     1-Contactar con un agente
#     2-Realizar una  cotización. 
#     3-Consultar planes o servicios disponibles.
#     4-Agendar el envío de tu paquete.
#     5-Consultar el estado de tu paquete. 