import pyttsx3 
import speech_recognition as sr
import datetime
import webbrowser
import os
from GoogleNews import GoogleNews
import Test
from Test import label


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

print('Detected Emotion....')
print(label)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")   

    else:
        print("Good Evening!")
        speak("Good Evening!") 
        
    print("I am EBASS. To know your options say HELP")
    speak("I am EBASS. To know your options say HELP")       
   

    
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


if __name__ == "__main__":
    wishMe()
    while True:
 
        query = takeCommand().lower()


        if 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")
            
        elif 'movie' in query:
            import movie_rec
            
        elif 'help' in query:
            print("1. open Youtube")
            speak("open youtube")
            print("2. open Google")
            speak("open google")
            print("3. open an AudioBook")
            speak("open an AudioBook")
            print("4. Ask me for a movie recommendation")
            speak("Ask me for a movie recommendation")
            print("5. Exercise")
            speak("Exercise")
            print("6. Play music")
            speak("Play music")
            print("7. Ask me the time")
            speak("Ask me the time")
            print("8. Get today's news")
            speak("Get today's news")
              
        elif 'exercise' in query:
            print("Opening a exercise video of your choice...")
            webbrowser.get(chrome_path).open("https://youtu.be/ml6cT4AZdqI")
            
        elif 'play audiobook' in query:
            print("Opening an audiobook of your choice...")
            webbrowser.get(chrome_path).open("https://ia903102.us.archive.org/19/items/mindthepaintgirl_1911_librivox/mindthepaint_1_pinero_64kb.mp3")

        elif 'play music' in query:
            print("Playing some beats...")
            music_dir = 'C:/Users/ryshi/Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")
            
        elif 'get news' in query:
            print('Searching News...')
            speak('Searching News...')
            googlenews=GoogleNews()
            googlenews=GoogleNews('en','d')
            print('What news would you like to know about?')
            speak('What news would you like to know about?')
            googlenews.search(takeCommand())
            googlenews.getpage(1)
            googlenews.gettext()
            n=(googlenews.gettext())
            print(n)
            #speak(n)
            
        elif 'exit' in  query:
            print("Exiting...")
            speak('Exiting')
            break