import pyttsx3
import speech_recognition as sr
import pyaudio as p;print(p.__version__)
import wikipedia
import webbrowser
import os
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning!")
        elif hour >= 12 and hour < 18:
            speak("Good afternoon!")

        else:
            speak("Good Evening!")
        speak("I am Jarvis Sir. Please tell me may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-IN')
        print("User said:" +query)

    except Exception as e:

        print("Say that again Please...")
        return "None"
    return query





if __name__ == "__main__":
        #speak("Sanket is a good boy")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=10)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'who are you' in query:
            speak("I am jarvis")


        elif 'Are you intelligent' in query:
            speak("Like Master, Like jarvis")


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime(" %H:%M:%S")
            speak("Sir,the time is "+strTime)

        elif 'play song' in query:
            music_dir = 'E:\song\Dhadak'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'romantic song' in query:
            music_dir = 'E:\song\sad'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))


        elif 'open  Google map' in query:
            webbrowser.open("www.google.com/maps")

        elif 'open Facebook' in query:
            webbrowser.open("Facebook.com")













