# Grappes: Chatbot
# Model builder

#_LIB___________________
import nltk, json, pickle, random, webbrowser as wb, numpy as np
import openpyxl, string, secrets, smtplib, datetime, pandas as pd
from nltk.stem import SnowballStemmer
from tensorflow.keras.models import load_model
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

stemmer = SnowballStemmer("spanish")
modelo = load_model("Chatbot_modelo.h5")
intents = json.loads(open("intents.json").read())
palabras = pickle.load(open("palabras.pkl", "rb"))
clases = pickle.load(open("clases.pkl", "rb"))
letters = string.ascii_letters
digits = string.digits
alphabet = letters + digits


#cuenta de email
sender = 'grappes.sic@hotmail.com'
password = 'GrappesSic123'

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
    ERROR_THRESHOLD = 0.75
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD] 
    results.sort(key = lambda x: x[1], reverse = True)  
    return_list = []    
    for r in results:   
        return_list.append({"intent": clases[r[0]], "probability": str(r[1])})
    print("accurracy:", return_list[0]["probability"])
    if len(return_list) == 0:
        return_list.append({"intent": "no_response", "probability": "1.00"})
    return return_list

def get_response(ints, intents_json, text):
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"]
    try:
        for i  in list_of_intents: 
            if (i["tag"] == tag):
                result = random.choice(i["responses"])
                break
    except:
        tag = "ayuda"
        for i  in list_of_intents: 
            if (i["tag"] == tag):
                result = random.choice(i["responses"])
                break
            
    if(tag == "contactar_agente"):
        try:
            datos = text.split(",")
            nombre = datos[1].lower().strip()
            telefono = datos[2].lower().strip()
            if not "+507" in telefono:
                link = "https://wa.me/+507" + telefono
            else:
                link = "https://wa.me/" + telefono
            wb.open(link)
            return result, 0
        except:
            return result, "Has escrito mal el comando, intentalo nuevamente."
    if (tag == "cita_asesoría"):
        try:
            datos = text.split(",")
            nombre = datos[1].lower().strip()
            telefono = datos[2].lower().strip()
            dia = datos[3].lower().strip()
            hora = datos[4].lower().strip()       
            res = create_date(nombre, telefono, dia, hora)
            return result, res
        except:
            return result, "Has escrito mal el comando, intentalo nuevamente."
    
    if(tag == "ayuda_estatus"):
        try:
            datos = text.split(",")
            num = datos[1].lower().strip()
            res = check_tracking(num)
            return result, res
        except:
            return result, "Has escrito mal el comando, intentalo nuevamente."
        
    if(tag == "programar_envio"):
        try:
            datos = text.split(",")
            nombre = datos[1].lower().strip()
            telefono = datos[2].lower().strip()
            dia = datos[3].lower().strip()       
            res = create_pack(nombre, telefono, dia)
            return result, res
        except:
            return result, "Has escrito mal el comando, intentalo nuevamente."
        
    if(tag == "ayuda_cotizacion"):
        try:
            datos = text.split(",")
            company = datos[1].lower().strip()
            name = datos[2].lower().strip()
            email = datos[3].lower().strip()       
            res = create_cotizacion(company, name, email)
        except:
            return result, "Has escrito mal el comando, intentalo nuevamente."
        
    return result, 0

def create_date(nombre, telefono, dia, hora):
    citas= open("citas.csv", "a")
    if ("lunes" in dia) or ( "1" in dia):
        dia= "lunes"
    if ("martes" in dia) or ( "2" in dia):
        dia= "martes"
    if ("miércoles" in dia) or ( "3" in dia):
        dia= "miércoles" 
    if ("jueves" in dia) or ( "4" in dia):
        dia= "jueves"
    if ("viernes" in dia) or ( "5" in dia):
        dia= "viernes"            
    if "a" in hora:
        hora= "7:00 am"          
    if "b" in hora:
        hora= "8:00 am"
    if "c" in hora:
        hora= "9:00 am"           
    if "d" in hora:
        hora= "10:00 am"            
    if "e" in hora:
        hora= "11:00 am"
        
    datos= [nombre, telefono, dia , hora]
    
    for i in datos:
        citas.write(i)
        citas.write(";")
        
    citas.write("\n")
    citas.close()
    res = "Su cita ha sido guardada correctamente para el " + dia + " a las " + hora + "\nLo esperamos."
    return res

def create_code():
    code_length = 6
    code = ''
    for i in range(code_length):
        code += ''.join(secrets.choice(alphabet))
    
    while True:
        code = ''
        for i in range(code_length):
            code+= ''.join(secrets.choice(alphabet))

        if sum(char in digits for char in code)>=2:
              break
    return code

def create_pack(nombre, telefono, dia):
    entregas= open("entregas.csv", "a")
    ID_paquete= create_code() 
    Estado= "No entregado"
    
    if ("lunes" in dia) or ( "1" in dia):
        dia= "lunes"
    if ("martes" in dia) or ( "2" in dia):
        dia= "martes"
    if ("miércoles" in dia) or ( "3" in dia):
        dia= "miércoles" 
    if ("jueves" in dia) or ( "4" in dia):
        dia= "jueves"
    if ("viernes" in dia) or ( "5" in dia):
        dia= "viernes"
        
    datos= [nombre , ID_paquete , telefono , Estado, dia]
    
    for i in datos:
        entregas.write(i)
        entregas.write(";")
        
    entregas.write("\n")
    entregas.close()
    res = "Su paquete con numero de tracking " + ID_paquete + " ha sido programado para ser enviado el " + dia + "\nGracias por preferirnos."
    return res

def create_cotizacion(company, name, email):
    quotation_number = random.randint(0,100)
    date = datetime.date.today()
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
        #Conexion con el servidor Microsoft
        sesion_smtp = smtplib.SMTP('smtp.office365.com',587)
        sesion_smtp.ehlo()
        sesion_smtp.starttls()
        sesion_smtp.ehlo()
        sesion_smtp.login(sender,password)
        text = menssage.as_string()
        sesion_smtp.sendmail(sender,addressee,text)
        sesion_smtp.quit()
        return "¡El correo con la cotización fue enviado correctamente!"
    except:
        return "Lo sentimos no pudimos realizar el envío del correo. Intente nuevamente."
     
def buscar_status(x):
    for index, row in grappes_tracking.iterrows():
        if x in grappes_tracking.index:
            name = grappes_tracking["Nombre"][x]
            status = grappes_tracking["Estado"][x]
            email = grappes_tracking["Correo"][x]
            return name, status, email

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


           
def check_tracking(num):
    # Le consultamos al cliente su numero de orden para verificar su estatus en la db
    num_order = list(num)
    verification  = len(num_order)
    if verification < 4 or verification > 4:
        return "Error, intentalo nuevamente"
    else:
        name, status, email = buscar_status(int(num))
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

            else:
                return "Error, intentalo nuevamente"

        except:
            return "Error, intentalo nuevamente"
            quit()
        # Conexion con el servidor Microsoft
    sesion_smtp = smtplib.SMTP('smtp.office365.com', 587)
    sesion_smtp.starttls()
    sesion_smtp.login(sender, password)
    text = menssage.as_string()
    sesion_smtp.sendmail(sender, addressee, text)
    sesion_smtp.quit()
    return "El estado del su paquete ha sido enviado a su correo.\nGracias por preferirnos."
        
def bot(text):
    ints = predict_class(text,modelo)
    res1, res2 = get_response(ints, intents, text)   
    return res1, res2
