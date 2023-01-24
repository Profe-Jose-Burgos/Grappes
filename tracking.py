#!/usr/bin/env python
# coding: utf-8
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pandas as pd
import time


# cuenta de email
sender = 'grappes.sic@hotmail.com'
password = 'GrappesSic123'

# abriendo db
def open_csv(file):
    track = pd.read_csv(file, sep=";")
    return track


file = "Grappes.csv"
df = open_csv(file)

# Variables para acceder a la db
num_track = df["NumTracking"]
name = df["Nombre"]
user = df["Usuario"]
tel = df["Teléfono"]
correo = df["Correo"]
status = df["Estado"]
data = {"NumTracking": num_track, "Nombre": name, "Usuario": user,
        "Teléfono": tel, "Correo": correo, "Estado": status}

# se crea un DataFrame
grappes_tracking = pd.DataFrame(data)
grappes_tracking.set_index("NumTracking", inplace=True)
# grappes_tracking

# Buscamos los datos en la db


def buscar_status(x):
    for index, row in grappes_tracking.iterrows():
        if x in grappes_tracking.index:
            name = grappes_tracking["Nombre"][x]
            status = grappes_tracking["Estado"][x]
            email = grappes_tracking["Correo"][x]
            return name, status, email


# Le consultamos al cliente su numero de orden para verificar su estatus en la db
num = input("Ingrese su número de tracking:")
num_order = list(num)
verification = len(num_order)
if verification < 4 or verification > 4:
    print('Error numero de orden invalido... Ingresa otro: ')
else:
    name, status, email = buscar_status(int(num))
    print(f"El paquete a nombre de {name} está a {status}.")
    print(f"{email}")


#Enviamos los correos dependiendo del estatus de la orden
try:
        if status == 'Retirado':
            time.sleep(1)
            addressee = email
            subject = 'Tu orden_%s' % num
            body_message = 'Hola %s, \n\nTu producto ya lo has retirado con exito. \n\nGracias, \nGrappes Shipping' % name
            menssage = MIMEMultipart()
            menssage['From'] = sender
            menssage['To'] = addressee
            menssage['Subject'] = subject
            menssage.attach(MIMEText(body_message, 'plain'))
            print('Email send succesfully!')

        elif status == 'Listo para retirar':
            time.sleep(1)
            addressee = email
            subject = 'Tu orden_%s'%num
            body_message = 'Hola %s, \n\nTu producto ya listo para retirar en la sucursal de San Francisco.\n\nGracias, \nGrappes Shipping'%name
            menssage = MIMEMultipart()
            menssage['From'] = sender
            menssage['To'] = addressee
            menssage['Subject'] = subject
            menssage.attach(MIMEText(body_message, 'plain'))
            print('Email send succesfully!')

        elif status == 'En camino':
            time.sleep(1)
            addressee = email
            subject = 'Tu orden_%s' % num
            body_message = 'Hola %s, \n\nTu producto ya ha sido enviado.\n\nGracias, \nGrappes Shipping' % name
            menssage = MIMEMultipart()
            menssage['From'] = sender
            menssage['To'] = addressee
            menssage['Subject'] = subject
            menssage.attach(MIMEText(body_message, 'plain'))
            print('Email send succesfully!')

        elif status == 'En bodega':
            time.sleep(1)
            addressee = email
            subject = 'Tu orden_%s' % num
            body_message = 'Hola %s, \n\nTu producto ya lo hemos recibido en nuestra bodega.\n\nGracias, \nGrappes Shipping' % name
            menssage = MIMEMultipart()
            menssage['From'] = sender
            menssage['To'] = addressee
            menssage['Subject'] = subject
            menssage.attach(MIMEText(body_message, 'plain'))
            print('Email send succesfully!')

        elif status == 'Solicitado':
            time.sleep(1)
            addressee = email
            subject = 'Tu orden_%s' % num
            body_message = 'Hola %s, \n\nHaz solicitado tu el envio de tu producto para el envio.\n\nGracias, \nGrappes Shipping' % name
            menssage = MIMEMultipart()
            menssage['From'] = sender
            menssage['To'] = addressee
            menssage['Subject'] = subject
            menssage.attach(MIMEText(body_message, 'plain'))
            print('Email send succesfully!')

        else:
            print('Disculpa numero de orden no valido, ingresa otro')

except:
    print('Something is wrong with the email....')
    quit()


# Conexion con el servidor Microsoft
sesion_smtp = smtplib.SMTP('smtp.office365.com', 587)
sesion_smtp.starttls()
sesion_smtp.login(sender, password)
text = menssage.as_string()
sesion_smtp.sendmail(sender, addressee, text)
sesion_smtp.quit()


# Menú del cliente
# Indica por favor, en qué deseas que te ayude:
#     1-Contactar con un agente
#     2-Realizar una  cotización.
#     3-Consultar planes o servicios disponibles.
#     4-Agendar el envío de tu paquete.
#     5-Consultar el estado de tu paquete.
