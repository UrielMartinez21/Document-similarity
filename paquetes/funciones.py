# ---------------------| Bibliotecas |---------------------
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer  # Vectorizador


# ---------------------| Funciones |---------------------
def leer_corpus(ruta):
    """Función para leer el corpus"""

    with open(ruta, "r", encoding="utf-8") as informacion:
        corpus = informacion.read().split('\n')
    return corpus

def vector_binario(corpus):
    """Función para vectorizar el corpus en binario"""

    vectorizador_binario = CountVectorizer(binary=True, token_pattern=r'(?u)\w\w+|\w\w+\n|\.')
    X = vectorizador_binario.fit_transform(corpus)
    print('[+]Representación vectorial binarizada')
    return X.toarray()

def vector_frecuencia(corpus):
    """Función para vectorizar el corpus por frecuencia"""

    vectorizador_frecuencia = CountVectorizer(token_pattern=r'(?u)\w\w+|\w\w+\n|\.')
    X = vectorizador_frecuencia.fit_transform(corpus)
    print('Representación vectorial por frecuencia')
    return X.toarray()


def vector_tfidf(corpus):
    """Función para vectorizar el corpus por tf-idf"""

    vectorizador_tfidf = TfidfVectorizer(token_pattern=r'(?u)\w\w+|\w\w+\n|\.')
    X = vectorizador_tfidf.fit_transform(corpus)
    print('Representación vectorial tf-idf')
    print(X.toarray())