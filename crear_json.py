# Grupo: Grappes
# Creador de json para el programa

#_LIBS_________
import json

#_FUNCTIONS_________
def save_json(data):
    file = open("intents.json", "w")
    json.dump(data, file, indent=4)

def start_intents():
    text = {
              "intents": [
                {
                  "tag": "saludos",
                  "patterns": [
                    "hola",
                    "buenos dias",
                    "buenas tardes",
                    "buenas noches",
                    "como estas",
                    "hay alguien ahi?",
                    "hey",
                    "ayuda",
                    "que tal",
                    "que sopa",
                    "habla",
                    "hi",
                    "hello",
                    "q xopa"
                  ],
                  "responses": [
                    "Hola has contactado con Grappe BOX (bot)\n1- Puedo ayudarte en hacer una cotización\n2- Puedo ayudarte a programar un envío\n3- Tambien puedo ayudarte con el tracking del paquete\n4- Puedo enlazarte con un agente."
                  ],
                  "context": [
                    "saludos"
                  ]
                },
                {
                  "tag": "ayuda_realizar_cotizacion",
                  "patterns": [
                    "realizar la cotizacion",
                    "1",
                    "agente",
                    "quiero una cotizacion",
                    "cotizacion",
                    "solicitar cotizacion",
                    "necesito una cotizacion",
                    "ayudar con una cotizacion"
                  ],
                  "responses": [
                    "Para realizarte una cotizacion env\u00eda un mensaje con la siguiente informaci\u00f3n:\nCotizacion, Nombre de la empresa, Tu nombre, Correo \nEjemplo: Cotización, Grappes INC, Pablo Andres, pablo.andres@correo.com"
                  ],
                  "context": [
                    "ayuda_cotizacion"
                  ]
                },
                {
                  "tag": "ayuda_cotizacion",
                  "patterns": [
                    "cotizacion, ",
                    "cotizacion,",
                    "Cotizacion, ",
                    "Cotizacion,",
                    "cotizacion, empresa, nombre apellido, correo",
                    "cotizacion,empresa,nombre apellido,correo",
                    "cotizacion, Apple Computers, Steve Jobs, steve.jobs@applecomputers.com",
                    "cotizacion,Apple Computers,Steve Jobs,steve.jobs@applecomputers.com"
                  ],
                  "responses": [
                    "Espera un momento mientras realizo tu cotizacion, estara llegando a tu correo...",
                    "Perfecto! dame un momento.",
                    "Enviando cotizacion al correo."
                  ],
                  "context": [
                    "ayuda_cotizacion"
                  ]
                },
                {
                  "tag": "ayuda_estatus_orden",
                  "patterns": [
                    "status",
                    "3",
                    "estatus",
                    "tracking",
                    "trackear",
                    "estado de la orden",
                    "quiero saber sobre mi orden",
                    "orden",
                    "mi orden"
                  ],
                  "responses": [
                    "Para solicitar el estatus de tu orden env\u00eda un mensaje con la siguiente informaci\u00f3n:\nOrden, numero de orden\nEjemplo: Orden, 9101"
                  ],
                  "context": [
                    "ayuda_estatus"
                  ]
                },
                {
                  "tag": "ayuda_estatus",
                  "patterns": [
                    "orden, ",
                    "orden,",
                    "Orden, ",
                    "Orden,",
                    "orden, xxxx",
                    "orden,xxxx",
                    "orden, 1234",
                    "orden,1234"
                  ],
                  "responses": [
                    "Espera un momento mientras verifico tu orden, en unos momentos recibiras un correo con el estatus de tu orden.",
                    "Sin problemas, dame un momento para verificar en el sistema.",
                    "En unos momentos recibiras un correo con el estatus de tu orden."
                  ],
                  "context": [
                    "ayuda_estatus"
                  ]
                },
                {
                    "tag": "ayuda_programar_envio",
                    "patterns": [
                        "nuevo envio",
                        "2",
                        "programar entrega",
                        "entrega",
                        "cita entrega"
                        "quiero enviar"
                        "quiero recibir"

                    ],
                    "responses": [ "Buenas, contamos con entregas de lunes a viernes,para programar una entrega env\u00eda un mensaje con la siguiente informaci\u00f3n:\nEntrega, Nombre, contacto, día\nEjemplo: Entrega, Pablo Andres, 12346789, día"
                    ],
                    "context": [
                        "ayuda_programar_envio"
                    ]
                },
                {
                    "tag": "programar_envio",
                    "patterns": [
                        "entrega, ",
                        "Entrega, ",
                        "entrega, nombre apellido, xxxxxxxxx, xxxxx",
                        "Entrega,nombre apellido,xxxxxxxxx, día",

                    ],
                    "responses": [
                        "Desplegando menú de entrega",
                        "Gracias por confiar en nosotros, creando entrega...",
                        "De inmediato!"
                    ],
                    "context": [
                        "programar_envio"
                    ]
                },
                {
                  "tag": "programar_envio",
                  "patterns": [
                    "entrega, ",
                    "Entrega, ",
                    "entrega, nombre apellido, xxxxxxxxx",
                    "Entrega,nombre apellido,xxxxxxxxx",
                    
                  ],
                  "responses": [
                    "Desplegando menú de entrega",
                    "Gracias por confiar en nosotros, creando entrega...",
                    "De inmediato!"
                  ],
                  "context": [
                    "programar_envio"
                  ]
                },
                {
                    "tag": "ayuda_asesoría",
                    "patterns": [
                        "cita asesoría",
                        "asesoría",
                        "cita ",
                        "sucursal",
                        "ir a oficina",
                        "5"
                    ],
                    "responses": ["Buenas, contamos con citas de asesoría de lunes a viernes en los siguientes horarios: \n a. 7:00 am\nb.8:00 am\nc. 9:00 am\nd. 10:00 am\ne.11:00 am\npara solicitar una cita env\u00eda un mensaje con la siguiente informaci\u00f3n:\ncita, Nombre, contacto, día, hora seleccionada \nEjemplo: cita, Pablo Andres , 67856989 , lunes, a"
                    ],
                    "context": [
                        "ayuda_asesoría"
                    ]
                },
                {
                    "tag": "cita_asesoría",
                    "patterns": [
                        "cita, ",
                        "asesor,",
                        "cita, nombre apellido, XXXXXXXX, xxxxx,x",
                        "citas,nombre apellido, 67855599, lunes, b ",

                    ],
                    "responses": [
                        "Entendido, desplegando el menú de citas de asesoría",
                        "Sin problemas, deme un momento.",
                        "¿Vas a visitarnos?, excelente!", 
                    ],
                    "context": [
                        "contactar_agente"
                    ]
                },
                {
                  "tag": "cita_asesoría",
                  "patterns": [
                    "cita, ",
                    "asesor,",
                    "cita, nombre apellido, XXXXXXXX ",
                    "citas,nombre apellido, 67855599 ",
                    
                  ],
                  "responses": [
                    "Entendido, desplegando el menú de citas de asesoría",
                    "Sin problemas, deme un momento.",
                    "¿Vas a visitarnos?, excelente!",
                    
                  ],
                  "context": [
                    "contactar_agente"
                  ]
                },
                {
                  "tag": "ayuda",
                  "patterns": [
                    "ayuda",
                    "help",
                    "necesito ayuda",
                    "ayuda por favor",
                    "ayuda porfavor"
                  ],
                  "responses": [
                    "1- Puedo ayudarte en hacer una cotización\n2- Puedo ayudarte a programar un envío\n3- Tambien puedo ayudarte con el tracking del paquete\n4- Puedo enlazarte con un agente.\n5- Programar citas para asesorias."
                  ],
                  "context": [
                    "ayuda"
                  ]
                },
                {
                  "tag": "ayuda_contactar_agente",
                  "patterns": [
                    "contactar agente",
                    "4",
                    "agente",
                    "hablar agente",
                    "persona",
                    "humano",
                    "hablar con agente",
                    "quiero hablar con un agente",
                    "personal"
                  ],
                  "responses": [
                    "Para contactarte con un agente envía un mensaje con la siguiente información:\nAgente, Nombre, Numero de telefono\nEjemplo: *Agente, Pablo Andres, 12346789*",
                    
                  ],
                  "context": [
                    "contactar_agente"
                  ]
                },
                {
                  "tag": "contactar_agente",
                  "patterns": [
                    "agente, ",
                    "agente,",
                    "Agente, ",
                    "Agente,",
                    "agente, nombre apellido, xxxxxxxxx",
                    "agente,nombre apellido,xxxxxxxxx",
                    "agente, Andres Iniesta, 67590298",
                    "agente,andres iniesta,67590298"
                  ],
                  "responses": [
                    "Espere un momento mientras realizo el enlace...",
                    "Sin problemas, deme un momento.",
                    "Transfiriendo con un agente."
                  ],
                  "context": [
                    "contactar_agente"
                  ]
                },
                {
                  "tag": "agradecimientos",
                  "patterns": [
                    "gracias",
                    "muchas gracias",
                    "mil gracias",
                    "muy amable",
                    "se lo agradezco",
                    "gracias por la ayuda",
                    "muy agradecido",
                    "gracias por su tiempo",
                    "ty"
                  ],
                  "responses": [
                    "De nada",
                    "Feliz por ayudarlo",
                    "Gracias a usted",
                    "Estamos para servirle",
                    "Fue un placer",
                    "Sin problemas",
                    "No se preocupe",
                    "Siempre para servirle"
                  ],
                  "context": [
                    "agradecimientos"
                  ]
                },
                {
                  "tag": "no_response",
                  "patterns": [
                    ""
                  ],
                  "responses": [
                    "No te he logrando entender, intentalo de nuevo.",
                    "\u00bfC\u00f3mo has dicho, disculpa?",
                    "Lo siento, no entiendo lo que me pides...",
                    "Repiteme, por favor",
                    "Disculpe \u00bfQu\u00e9Qué ha dicho?",
                    "Verifica el mensaje que has enviado"
                  ],
                  "context": [
                    ""
                  ]
                }
              ]
            }
    save_json(text)




