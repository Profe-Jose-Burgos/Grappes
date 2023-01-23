#_Grappes
#_Program driver

#_LIBS_____
from time import sleep
from os.path import isfile

# _________________________________MAIN________________________
# Driver program
if __name__ == '__main__':
    
    if not isfile("intents.json"):
        from crear_json import start_intents
        print("Creating intents...")
        start_intents()
        sleep(1)

    if not isfile("Chatbot_modelo.h5"):
        from crear_modelo import crear_modelo
        print("Creating model...")
        sleep(1)
    from keep_session import start_keep_session
    print("Starting sesison...")
    start_keep_session()
    sleep(1)

    from whatsapp_bot import whatsapp_bot_init    
    print("Starting chatbot...")
    whatsapp_bot_init()
