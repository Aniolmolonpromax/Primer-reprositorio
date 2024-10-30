meme_dict = {
    "cringe": "Algo excepcionalmente raro o embarazoso",
    "lol": "Una respuesta común a algo gracioso",
    "rofl": "Una respuesta a una broma",
    "sheesh": "Ligera desaprobación",
    "creepy": "Aterrador, siniestro",
    "aggro": "Ponerse agresivo/enojado",
    "fam": "Amigos cercanos o familia",
    "lit": "Algo emocionante o increíble",
    "vibe": "La atmósfera o sensación de un lugar o situación",
    "slay": "Hacer algo excepcionalmente bien",
    "sus": "Sospechoso o dudoso",
    "flex": "Mostrar con orgullo algo que se tiene",
    "ghosting": "Dejar de comunicarse con alguien sin explicación",
    "stan": "Un fanático obsesivo de alguien o algo",
    "no cap": "Sin mentiras, hablando en serio",
    "shade": "Crítica sutil o indirecta",
    "tea": "Chisme o información jugosa",
    "woke": "Consciente sobre temas sociales y políticos",
    "bop": "Una canción muy buena o pegajosa",
    "simp": "Alguien que muestra demasiada atención a alguien que no le corresponde",
    "fomo": "Miedo a perderse algo",
    "yolo": "Solo se vive una vez, así que hay que aprovechar",
    "lit AF": "Extremadamente emocionante o increíble",
    "ride or die": "Alguien que te apoya incondicionalmente",
    "bet": "Afirmar que algo es cierto o aceptar un desafío",
    "lowkey": "De manera discreta o secreta",
    "highkey": "De manera abierta o evidente",
    "mood": "Una expresión de identificación con una situación o sentimiento"
}

word = input("Escribe una palabra que no entiendas: ").lower()
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Tu palabra no se encuentra en mi diccionario")
