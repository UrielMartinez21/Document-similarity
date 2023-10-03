# ---------------------| Bibliotecas |---------------------
from tkinter import filedialog                                                  # Cuadro de dialogo
from spacy.lang.es.stop_words import STOP_WORDS                                 # Palabras vacias
import spacy                                                                    # Procesamiento de lenguaje natural
import math                                                                     # Matematicas
import os                                                                       # Rutas ingresadas
import re                                                                       # Obtener expresiones regulares

# ---------------------| Funciones |---------------------
def leer_corpus(ruta):
    """
    Leer corpus preparado
    return: lista
    """

    with open(ruta, "r", encoding="utf-8") as informacion:
        corpus = informacion.read().split('\n')
    return corpus


def cargar_archivo():
    """
    Lee archivo de usuario
    return: lista
    """

    ruta_archivo = filedialog.askopenfilename(title="Abrir archivo", filetypes=(("Archivos de texto", "*.txt"),))
    nombre_archivo= os.path.splitext(os.path.basename(ruta_archivo))[0]
    numero = re.findall(r'\d+', nombre_archivo)
    with open(ruta_archivo, "r", encoding="utf-8") as informacion:
        noticias_seleccionadas = informacion.read().split('\n')
    return noticias_seleccionadas, numero[0]


def normalizar_corpus(lista_noticias):
    """
    Función para normalizar el corpus
    return: lista
    """

    nlp = spacy.load("es_core_news_sm")

    # Tokenizar
    corpus_tokenizado = []
    for noticia in lista_noticias:
        # Analisis de texto
        doc = nlp(noticia)
        # Tokenización = separación de palabras
        tokens = [token.text for token in doc]
        # Lista de tokens a cadena de texto
        corpus_tokenizado.append(" ".join(tokens))

    # Lematizar
    corpus_lematizado = []
    for noticia_tokenizada in corpus_tokenizado:
        # Analisis de texto
        doc = nlp(noticia_tokenizada)
        # Lematización = reducción de palabras a su raíz
        lemas = [token.lemma_ for token in doc]
        # Lista de lemas a cadena de texto
        corpus_lematizado.append(" ".join(lemas))

    # Eliminar palabras vacías
    # Categorías de palabras para eliminar: articulos, preposiciones, conjunciones y prononmbres
    categorias_a_eliminar = ["DET", "ADP", "CCONJ", "PRON"]
    corpus_filtrado = []
    for noticia_lematizada in corpus_lematizado:
        # Analizar el texto
        doc = nlp(noticia_lematizada)
        # Filtrar palabras según las categorías especificadas
        tokens_filtrados = [token.text for token in doc if token.pos_ not in categorias_a_eliminar]
        # Convertir la lista de tokens en una cadena de texto
        texto_filtrado = " ".join(tokens_filtrados)
        # Agregar el texto filtrado al nuevo corpus
        corpus_filtrado.append(texto_filtrado)

    # Retornar el corpus filtrado
    return corpus_filtrado


def cosine(x, y):
    """
    Función para calcular la similitud coseno
    return: float
    """

    val = sum(x[index] * y[index] for index in range(len(x)))
    sr_x = math.sqrt(sum(x_val**2 for x_val in x))
    sr_y = math.sqrt(sum(y_val**2 for y_val in y))
    res = val/(sr_x*sr_y)
    return (res)
