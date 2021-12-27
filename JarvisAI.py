import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,Rohit")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon,Rohit")
    else:
        speak("Good Evening,Rohit")
    speak("My name is Tejas shetty. please tell me How may i help you")

def takeCommand():
    #it takes microphone input from the user and return the output in form of string
   r=sr.Recognizer() #helps to recognize the audio
   with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1 #it should not complete the audio if i take pause
        r.adjust_for_ambient_noise(source,duration=2)
        print("say something!")
        r.energy_threshold=200
        audio = r.listen(source)
        
   try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-IN')
        print(f"User Said: {query}\n")
      
        
   except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
   return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rohitrao1411@gmail.com','Rohitr@o14')
    server.sendmail('rohitrao1411@gmail.com', to, content)
    server.close()
    
if __name__ == '__main__':
    #speak("Rohit is a good boy")
    wishMe()
    while True:
        query = takeCommand().lower()   #for matching he queries down
        
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            music_dir = ''
            songs=os.listdir()
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strtime}")
            
        elif 'open code' in query:
            codepath ="C:\\Users\\ROHIT RAO\\AppData\\Local\\Programs\\Spyder\\Python\\pythonw.exe"
            os.startfile(codepath)
            
        elif 'hello' in query:
            speak("hello sir,what can i do for you??")
            
        elif 'how are you' in query:
            speak("I am fine, how are you doing")
            
        elif 'fine' in query:
            speak("How may i help you")
            
        elif 'thank you' in query:
            speak("my pleasure sir")
            speak("ask me any time i will be there for you")
            
        elif 'email to rohit' in query:
            try:
                speak("what should i say?")
                content=takeCommand()   #return the string of words spoken
                to = "rohitrao1411@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry, not able to send...")
            
        elif 'quit' in query:
            speak("ok sir take care")
            break
        
            
            