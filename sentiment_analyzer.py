from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tkinter import IntVar, Menu, Tk

import nltk
import csv

"""sentiment_analyzer.py: Un script que analiza los comentarios del Ice-hotel 
                          les asigna un score segun polaridad,sentimiento y realiza un estudio NER
                          y extrae las entidades que reconoce """

__author__      = "Benjamin Ruiz"
__copyright__   = "GPLv3"


chuck_quote = '''Chuck Norris died and came and he decided to come back because after life was boring him'''

# Tokenizo la frase celebre de Chuck Norris
words_in_quote = word_tokenize(chuck_quote)
# Consigo una lista de "stop-words" del lenguaje en este caso ingles
stop_words = set(stopwords.words("english"))
# Ignoro las "stop-words" y consigo una frase sin ellas 
lista_filtrada = [palabra for palabra in words_in_quote if palabra.casefold() not in stop_words]
print(f"\nFrase orgininal --> {chuck_quote}")
print(f"Frase Tokenizada --> {words_in_quote}")
print(f"Frase sin stop-words --> {lista_filtrada}")
tags = nltk.pos_tag(words_in_quote)
print(tags)
tree = nltk.ne_chunk(tags)
tree.draw()

def extraer_entidades(quote):
     words = word_tokenize(quote, language="english")
     # POS Parts Of Speach tagging se emplea para poder "leer el texto" 
     # entendiendo que rol gramatical que tiene cada palabra segun su contexto
     tags = nltk.pos_tag(words)
     # named entity chunking = "shallow-parsing" juntamos los POS tags en frases con estructura 
     # conseguir detectar las 6 W que son entidades 
     tree = nltk.ne_chunk(tags, binary=False)

     #Filtrar named entities 
     org = set(" ".join(i[0] for i in t) for t in tree 
            if hasattr(t,"label") and t.label() =="ORGANIZATION")
     
     person = set(" ".join(i[0] for i in t) for t in tree 
            if hasattr(t,"label") and t.label() =="PERSON")
     
     location = set(" ".join(i[0] for i in t) for t in tree 
            if hasattr(t,"label") and t.label() =="LOCATION")
     
     date = set(" ".join(i[0] for i in t) for t in tree 
            if hasattr(t,"label") and t.label() =="DATE")
     
     time = set(" ".join(i[0] for i in t) for t in tree 
            if hasattr(t,"label") and t.label() =="TIME")
     
     money = set(" ".join(i[0] for i in t) for t in tree 
            if hasattr(t,"label") and t.label() =="MONEY")
     
     percent = set(" ".join(i[0] for i in t) for t in tree 
            if hasattr(t,"label") and t.label() =="PERCENT")
     
     facility = set(" ".join(i[0] for i in t) for t in tree 
            if hasattr(t,"label") and t.label() =="FACILITY")
     
     gpe = set(" ".join(i[0] for i in t) for t in tree 
            if hasattr(t,"label") and t.label() =="GPE")

     namedEntities ={"organization": org, "person": person, 
                    "location": location,"date": date, "time": time,
                    "money": money, "percent": percent,"facility": facility,
                    "gpe": gpe}
     
     print("Entidades-----------------")
     for key,value in namedEntities.items():
          if value == set():
               value = "no encontrado"

          print(" >",key ,":", value )


      
def extraer_sentimiento():
 with open('IceHotelComments.csv', 'r', encoding="utf8") as file:
     reader = csv.reader(file,delimiter ='"')
     x=1
     for row in reader:
         print('\n\n______Comentario nº %d______'%(x))   
         print(row)
         comment=TextBlob(str(row))
         print("Analisis sentimiento -----")
         print(" > Polaridad = {0:.4f}".format(comment.sentiment[0]))
         print(" > Sentimiento = {0:.4f}".format(comment.sentiment[1]))
         extraer_entidades(str(comment))
         x+=1
        

extraer_sentimiento()