# this is a minor python project;)
# this is an virtual asistant created using python(script), multiple modules from python library.
# it has some basic functionalities such as:-
# --> Opening web sites(such as youtube, google, etc).
# --> Playing songs ( from musicLib.py).
# --> Entering message using voice in some .txt file.
# --> Reading data from the .txt file.
# --> Deleting data from the .txt file.
# --> Answer some basic things(like, What are you doing?)


#------------------------------------------------------------------------------------------------
# For this project you need to install  the required module.
# to install, use command: pip install <module name> in the terminal.
#------------------------------------------------------------------------------------------------


# the following line of code is important for writing message in demo.txt by voice input
from pyexpat.errors import messages

# the following line of statement is for importing the speech recognition module
import speech_recognition as sr

# the following line of code is important for using .recognize_google()
from speech_recognition.recognizers import google

# the following line of statement for web browser module, used for opening link in the web browser
import webbrowser

# the following line of statement is for text-to-speech output module
import pyttsx3

# the following line of statement is for importing data from musicLib.py
import musicLib


# to activate assistant say the name of the assistant("YOGA")


# for better speech recognition and better voice, you can use Google's dedicated API for TTS.
# further implementation and initialization code are present on Google's site, stackoverflow, GFG, etc.


# the following block of code is for speech recognition and the text-to-speech implementation
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# to change voice, change the index value in voices[].id from 0,1 or2 in the following method.
engine.setProperty('voice', voices[1].id)

# the following block of code is for defining speak() method to get the audio output
def speak(text):
    engine.say(text)
    engine.runAndWait()

# the following block of code is for defining the commands.
def processCommand(c):


    # you can define your own command by writting them as the following command and responses.


    # to get response for your questions you can define a condition using OpenAI's API
    # the required code snippet is available at their website


    # to get the contents of the file as audio output

    # to activate say "READ"
    if "read" in c.lower():
        speak("okay, i am reading your file...")
        g = open("demo.txt", "r")
        speak(g.read())
        g.close()


    # to delete all the contents of the file
    # to delete line-by-line you have to make some changes to the code

    # to activate say "FORMAT"
    elif "format" in c.lower():
        h = open("demo.txt" , "w")
        speak("okay, i have deleted all the contents of the file")
        h.close()


    # this is a sample for question and the reply

    # to activate ask "What are you doing?"
    elif "what are you doing" in c.lower():
        speak("Waiting for you to get command or assist you")


    # for writting or entering data using voice by generating transcripts of voice

    # to activate say "Open Book"
    elif "open book" in c.lower():
        speak("Tell me, what should I note down?")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for your note...")
            try:
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=4)
                message = recognizer.recognize_google(audio)
                with open("demo.txt", "a") as f:
                    f.write(message + "\n")
                speak(f"I've written: {message}")
            except sr.WaitTimeoutError:
                speak("No input detected. Please try again.")
            except sr.UnknownValueError:
                speak("Sorry, I couldn't understand. Try again.")
            except Exception as e:
                speak("Something went wrong while writing.")
                print(f"Error: {e}")


    # to open google, youtube or any other site by the voice command
    # .open() is from webbrowser module, used to open the link in your default browser

    # to activate say "Open Google"
    elif "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com")

    # to activate say "Open YouTube
    elif "open youtube" in c.lower():
        speak("opening youtube for you")
        webbrowser.open("https://youtube.com")


    # for playing songs which are present in the musicLib.py.
    # uses .open() to play song as the songs in musicLib.py are the link of the song from youtube music.
    # for defining similar commands like open or start something you can define them as the following.
    # you hate to write their keyword and responses in another python program(such as musicLib.py).

    # to play song say "Open <song name>"
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLib.music[song]
        speak("okay! here is your song")
        webbrowser.open(link)



# the following block of code contains script for the initialization of the assistant
if __name__ == "__main__":
    speak("your virtual assistant is ready")

    while True:
        r = sr.Recognizer()

        try:

            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)

            # you can change the statement to activate the assistant and the response in following code
            if (word.lower() == "yoga"):
                speak("hi there, ask me something")

                with sr.Microphone() as source:
                    print("Assistant activated...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error ; {0}".format(e))


#-----------------------------------------------END-----------------------------------------------------