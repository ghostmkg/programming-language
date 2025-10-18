import speech_recognition as sheru
import pyttsx3
import pywhatkit
import wikipedia

def Take_query(): 
  

    Hello()
   
    while(True):
          
       
        query = takeCommand().lower()
        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks ")
              
            # in the open method we just to give the link
            # of the website and it automatically open 
            # it in your default browser
            webbrowser.open("www.geeksforgeeks.com")
            continue
          
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
              
        elif "which day it is" in query:
            tellDay()
            continue
          
        elif "tell me the time" in query:
            tellTime()
            continue
          
        # this will exit and terminate the program
        elif "bye" in query:
            speak("Bye. Check Out GFG for more exicting things")
            exit()
          
        elif "from wikipedia" in query:
              

            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
              
            # it will give the summary of 4 lines from 
            # wikipedia we can increase and decrease 
            # it also.
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
          
        elif "tell me your name" in query:
            speak("I am Jarvis. Your deskstop Assistant")

def speak(audio)
speak
