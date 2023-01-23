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
                        "saludos",
                        "que tal",
                        "que sopa",
                        "habla",
                        "hi",
                        "hello",
                        "q xopa"
                    ],
                    "responses": [
                        "Hola has contactado con Grappe BOX (bot), en que podemos ayudarle.\n*Ayuda* para ver mis opciones."
                    ],
                    "context": [
                        "saludos"
                    ]
                },
                {
                    "tag": "despedidas",
                    "patterns": [
                        "chao",
                        "adios",
                        "hasta luego",
                        "nos vemos",
                        "bye",
                        "hasta pronto",
                        "hasta la proxima"
                    ],
                    "responses": [
                        "Hasta luego, tenga un buen dia",
                        "Ha sido un placer, vuelva pronto",
                        "Feliz d\u00eda"
                    ],
                    "context": [
                        "despedidas"
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
                        "fue de ayuda",
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
                    "tag": "ayuda",
                    "patterns": [
                        "necesito ayuda",
                        "ayuda",
                        "que sabes hacer",
                        "en que me puedes ayudar",
                        "dime lo que puedes hacer",
                        "/help",
                        "como me puedes ayudar",
                        "help",
                        "ense\u00f1ame tus comandos"
                    ],
                    "responses": [
                        "-Si quieres que te busque algo en wikipedia pidemelo, por ejemplo: *Dime quien es, Pablo Escobar*.\n-Si quieres que te envie videos o musica de youtube prueba con *Como se llama la cancion que hace, es la guitarra de lolo*\n-Tambien podemos solamente hablar.\n*Recuerda siempre utiliza la coma antes de tu peticion a buscar, de esa forma te puedo ayudar.*\nEvita utilizar stikers o enviar imagenes, puedo volverme un poco loco...\nDe momento no puedo hacer nada m\u00e1s, pero el equipo que trabaja en mi est\u00e1 a\u00f1adiendo muchas funciones para mi."
                    ],
                    "context": [
                        "ayuda"
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
                        "\u00bfQu\u00e9 has dicho?",
                        "Verifica el mensaje que has enviado",
                        "No he sido capaz de entenderte humano"
                    ],
                    "context": [
                        ""
                    ]
                }
            ]
        }
    save_json(text)




