import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pyttsx3 
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
            
        print("Say that again please...")  
        return "None"
    return query
    
    

def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

df = pd.read_csv("movie_dataset.csv")

features = ['keywords','cast','genres','director']
for feature in features:
    df[feature]=df[feature].fillna('')

def combine_features(row):
    try:
        return row['keywords']+" "+row['cast']+" "+row["genres"]+" "+row["director"]
    except:
        print("Error:", row)
df["combined_features"] = df.apply(combine_features,axis=1)

cv=CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)

speak("Enter name of the movie")
print("Enter name of the movie")
query = takeCommand()
#name1 = input("Enter name of the movie : ") 
print(query) 
movie_user_likes = query


movie_index = get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cosine_sim[movie_index]))


sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1],reverse=True)

i=0
for movie in sorted_similar_movies:
        print (get_title_from_index(movie[0]))
        i=i+1
        if i>50:
            break