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

#Variables prueba
name = 'Jose'
quotation_number = 2003
company = 'Apple Computers INC'

#Creacion del Documento pdf
doc = canvas.Canvas("documento_prueba.pdf",pagesize=A4)
doc.setFont("Times-Roman", 12)
doc.setLineWidth(.2)

#Formando la plantilla
doc.drawString(30,750,'Cotizacion %s'%quotation_number)
doc.drawString(30,735,'Grappes INC')
doc.drawString(500,755,'01/23/2023')
doc.line(378,723,580,723)
##################################
doc.drawString(275,725,'Estimado')
doc.drawString(400,725,name)
doc.line(378,723,580,723)

doc.drawString(30,703,'Nombre')
doc.line(120,700,580,700)
doc.drawString(120,703,'%s'%company)
doc.showPage()
doc.save()



#Creando el mensaje Email
time.sleep(1)
sender = 'grappes.sic@hotmail.com'
password = 'GrappesSic123'
addressee = input('Ingresa destinatario: ')
subject = input('Ingresa el asunto del correo: ')
body_message = input('Ingresa el mensaje que deseas enviar: ')
path_doc = input('Prueba documento (ingresa el nombre del archivo): ')
doc_name = 'Cotizacion'


#Generando el Email
menssage = MIMEMultipart()
menssage['From'] = sender
menssage['To'] = addressee
menssage['Subject'] = subject
menssage.attach(MIMEText(body_message,'plain'))
doc_attach = open(path_doc,'rb')
attach_MIMEbase = MIMEBase('application','octet-stream')
attach_MIMEbase.set_payload((doc_attach).read())
encoders.encode_base64(attach_MIMEbase)
attach_MIMEbase.add_header('Content-Disposition', 'attachment; filename=%s'%doc_name)
menssage.attach(attach_MIMEbase)



#Conexion con el servidor Microsoft
sesion_smtp = smtplib.SMTP('smtp.office365.com',587)
sesion_smtp.starttls()
sesion_smtp.login(sender,password)
text = menssage.as_string()
sesion_smtp.sendmail(sender,addressee,text)
sesion_smtp.quit()