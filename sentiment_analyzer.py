from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import nltk
import csv


text = ''' ",You can visit the hotel and be wowed by the artistry of the rooms, but if you come, you have to spend the night in a cold room. This is what this place is all about! The beauty of the rooms is secondary to the experience of spending the night in one. The anticipation, fear, excitement... and when all is done you will have an experience that you will remember forever. We stayed in the ice hotel for 2 nights. The first in a hot room and the second in a cold one. The hot room was very nice and clean. For the cold one we went all out and stayed in a cold suite with a warm bathroom. First let me explain a little bit. When you stay overnight in a cold room, the room is made of ice with only a bed and nothing else. If you need to use the bathroom, you have to walk to an adjacent"
", building that is warm. The building is a service center with coffee, showers, lockers, sauna and is staffed 24/7. You have access to your room after 6 PM. When you go to sleep, you leave your stuff in the service center and only take your thermal underwear, a cap and your sleeping bag. The sleeping bag is warm and it covers your head. You are also given a liner to use inside of the sleeping bag. I found the bed and sleeping bag to be confortable and once I overcame the excitement, I was able to get an excellent night sleep. The rooms are very dark. They wake you up in the morning. Our room was a suite so we had a hot bathroom with showers and we had our luggage with us. If you can afford it, this makes the stay very pleasant and does not change the experience of sleeping in the ice room. In my opinion, if you don’t stay in a suite with the warm bathroom, there is no point in staying on a art room or a basic ice room. Both are beautiful and at night you just sleep. During the day, you will have time to visit all the rooms and take pictures of them, you will not miss a thing. After finishing my Northern Lights trip, I would not have stayed at the Ice Hotel for two nights. There are a lot of activities, but I would have rather stayed at the Abisko Tourist Station an extra night to enjoy better scenery and similar activities in a less touristy environment. Don’t hesitate to spend a night here. It will be an experience to remember"
",…" '''

blob = TextBlob(text)
worf_quote = "Sir, I protest. I am not a merry man!"

words_in_quote = word_tokenize(worf_quote)

print(words_in_quote)

stop_words = set(stopwords.words("english"))

filterd_list = [word for word in words_in_quote if word.casefold() not in stop_words]
print(filterd_list)

def extract_ne(quote):
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
     
     for key,value in namedEntities.items():
          if value == set():
               value = "no encontrado"

          print(key ,":", value )       
     
     return namedEntities

      
def extraer_sentimiento():
 with open('IceHotelcomments.csv', 'r', encoding="utf8") as file:
     reader = csv.reader(file,delimiter ='"')
     x=1
     for row in reader:
         print('Comentario nº %d'%(x))   
         print(row)
         comment=TextBlob(str(row))
         print(format(comment.sentiment))
         print('\n\n')
         x+=1
        

#print (extract_ne(text))

extraer_sentimiento()