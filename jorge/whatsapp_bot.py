import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from unicodedata import normalize
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from chatbot import bot
from keep_session import start_keep_session

filepath = "./whatsapp_session.txt"
driver = webdriver

def crear_driver_session():
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            if cnt == 0:
                executor_url = line
            if cnt == 1:
                session_id = line
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            return {"succes":0, "value":None, "sessionId":session_id}
        else:
            return org_command_execute(self, command, params)
        org_command_execute = RemoteWebDriver.execute
        RemoteWebDriver.execute = RemoteWebDriver.execute
        RemoteWebDriver.execute = new_command_execute
        new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        new_driver.session_id = session_id
        RemoteWebDriver.execute = org_command_execute
        return new_driver

def whatsapp_bot_init():
    start_keep_session()
    global driver
    driver = crear_driver_session()
    esperando = 1
    while esperando == 1:
        esperando = len(driver.find_elements(By.CLASS_NAME,"_3AjBo"))
        sleep(5)
        print("Login success: ", esperando)        
    while True:
        if not buscar_chats():
            sleep(3)
            continue
        message = identificar_mensaje()
        if message == None:
            continue
        else:
            procesar_mensaje(message)
            
def normalizar(message: str):
    message = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", message), 0, re.I)
    return normalize( 'NFC', message)

def checkMensajes(chat):
    try:
        sleep(0.5)
        numMens = chat.find_element(By_CLASS_NAME, "_1pJ0J")
        msleer = re.findall("\d+", numMens)
        if len(msleer) != 0:
            pending = True
        else:
            pending = False
    except:
        pending = False
    return pending

def buscar_chats():
    print("Looking for new chats...")
    sleep(1)
    if len(driver.find_elements(By.CLASS_NAME,"zaKsw")) == 0:
        print("Chat opened...")
        message != identificar_mensaje()
        if message != None:
            return True
    else:
        sleep(0.5)
        chats = driver.find_elements(By.CLASS_NAME,"_1Oe6M")
        for chat in chats:
            por_responder = verificar_msn(chat)
            if por_responder:
                chat.click()
                sleep(0.5)
                return True
            else:
                print("No new chats...")
                continue
    return False

def identificar_mensaje():
    sleep(0.5)
    element_box_message = driver.find_elements(By.CLASS_NAME,"_27K43")
    posicion = len(element_box_message)-1
    sleep(0.5)
    element_message = element_box_message[posicion].find_element(By.CLASS_NAME,"_21Ahp")
    message = element_message.text.lower().strip()
    return normalizar(message)

def procesar_mensaje(message :str):
    sleep(0.5)
    chatbox = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    response1, response2 = preparar_respuesta(message)
    sleep(1)
    chatbox.send_keys(response1, Keys.ENTER)
    sleep(0.5)
    if not response2 == 0:
        chatbox = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        sleep(1)
        chatbox.send_keys(response2, Keys.ENTER)
        sleep(0.5)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

def preparar_respuesta(message :str):
    r1, r2 = bot(message)    
    return r1, r2      
