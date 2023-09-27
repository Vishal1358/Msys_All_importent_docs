import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")
# sptext()

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
# speechtx('I love You Kiran')

if __name__ =="__main__":

    # if "hey jarvis" in sptext().lower():
            while True:
                data1 = sptext().lower()

                if "your name" in data1:
                    name = " my name is jarvis"
                    speechtx(name)
                elif "old are you" in data1:
                    age = "i am 2 years old"
                    speechtx(age)
                elif "time" in data1:
                    time = datetime.datetime.now().strftime("%I%M%p")
                    speechtx(time)
                elif "youtube" in data1:
                    webbrowser.open("https://www.youtube.com/")
                elif "joke" in data1:
                    joke = pyjokes.get_joke(language="en", category="neutral")
                    print(joke)
                    speechtx(joke)
                
                elif "file" in data1:
                    add = "D:\Msys_Program\Msys_Programs\MSys_Projects\PythonProg\mini_projects\Jarvis"
                    open_1 = os.listdir(add)
                    print(open_1)
                    os.startfile(os.path.join(add,open_1[1]))
                elif "exit" in data1:
                    speechtx("thank you")
                    break

                time.sleep(5)

    # else:
    #     print("thanks")