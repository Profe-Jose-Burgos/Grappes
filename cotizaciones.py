#COTIZACIONES Y CORREOS
#Librerias
import random as rdm
import smtplib
import datetime
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

#cuenta de email
sender = 'grappes.sic@hotmail.com'
password = 'GrappesSic123'


#Pidiendo datos para la cotizacion
company = input('Ingresa nombre de la empresa: ')
name = input('Ingresa tu nombre: ')
email = input('Ingresa el correo para la cotizacion: ')
quotation_number = rdm.randint(0,100)
date = datetime.date.today()


#Creacion del Documento pdf
doc = canvas.Canvas("quotation%s.pdf"%date,pagesize=A4)
doc.setFont("Times-Roman", 12)
doc.setLineWidth(.2)
#Formando la plantilla
doc.drawString(30,750,'Cotizacion %s'%quotation_number)
doc.drawString(30,735,'Grappes INC')
doc.drawString(500,755,'%s'%date)
doc.line(378,723,580,723)
##################################
doc.drawString(275,725,'Estimado')
doc.drawString(400,725,name)
doc.line(378,723,580,723)
doc.drawString(30,703,'Empresa')
doc.line(120,700,580,700)
doc.drawString(120,703,'%s'%company)
doc.showPage()
doc.save()


try:
#Creando el mensaje Email 
    time.sleep(1)
    addressee = email
    subject = 'Cotizacion_%s'%quotation_number
    body_message = 'Hola %s, \n\nGracias por solicitar una cotizacion con Grappes Shipping. Podras encontrar la cotizacion adjuntada en el correo.'%name
    path_doc = "quotation%s.pdf"%date
    doc_name = "Cotizacion_%s.pdf"%date


#Generando el Email
    menssage = MIMEMultipart()
    menssage['From'] = sender
    menssage['To'] = addressee
    menssage['Subject'] = subject
    menssage.attach(MIMEText(body_message,'plain'))
    doc_attach = open(path_doc,'rb')
    attach_quotation = MIMEBase('application','octet-stream')
    attach_quotation.set_payload((doc_attach).read())
    encoders.encode_base64(attach_quotation)
    attach_quotation.add_header('Content-Disposition', 'attachment; filename=%s'%doc_name)
    menssage.attach(attach_quotation)
    print('Email send succesfully!')
except:
    print('Something is wrong with the email...')


#Conexion con el servidor Microsoft
sesion_smtp = smtplib.SMTP('smtp.office365.com',587)
sesion_smtp.ehlo()
sesion_smtp.starttls()
sesion_smtp.ehlo()
sesion_smtp.login(sender,password)
text = menssage.as_string()
sesion_smtp.sendmail(sender,addressee,text)
sesion_smtp.quit()