import speech_recognition as sprg
import pyttsx3 
import pyjokes
import webbrowser
import datetime
import time

def sp_text():
    recoginzer = sprg.Recognizer()
    with sprg.Microphone() as source:
        print("Listening....")
        recoginzer.adjust_for_ambient_noise(source)
        audio = recoginzer.listen(source)
        try:
            print("Recognizing ...")
            audio_data = recoginzer.recognize_google(audio)
            print(audio_data)
            return audio_data 
        except sprg.UnknownValueError:
             print("Sorry I can't hear you, Could you repeat it again")

def txt_sp(z):
    engine = pyttsx3.init()
    voice  = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(z)
    engine.runAndWait()


if __name__ == '__main__':

    if "hey friday" in sp_text().lower():
        while True:
            data = sp_text().lower()

            if 'your name' in data:
                name = "my name is friday"
                txt_sp(name)
            
            elif 'good morning' in data:
                gm = "Good Morning, Have a nice day"
                print(gm)
                txt_sp(gm)

            elif 'your age' in data:
                age = "I was developed in 2022, so technically I'm pretty young."
                txt_sp(age)
            
            elif 'location' in data:
                location = "It's Confidential "
                txt_sp(location)

            elif 'time' in data:
                time = datetime.datetime.now().strftime("%I%M%p")
                txt_sp(time)

            elif 'youtube' in data:
                webbrowser.open("https://www.youtube.com/")
                
            elif 'browser' in data:
                webbrowser.open("https://www.google.com/")
            
            elif 'instagram' in data:
                webbrowser.open("https://www.instagram.com/")
            
            elif 'whatsapp' in data:
                webbrowser.open("https://www.whatsapp.com/")
            
            elif 'songs' in data:
                webbrowser.open("https://www.spotify.com/")
            
            elif 'joke' in data:
                joke = pyjokes.get_joke(language='en',category="all")
                print(joke)
                txt_sp(joke)
            
            elif 'good night' in data:
                gm = "Good Night, sleep well"
                print(gm)
                txt_sp(gm)
                break
            
            elif 'bye' in data:
                txt_sp("bye,take care")
                break

            time.sleep(2)
                
    else:
         print("Sorry I can't hear you, Could you repeat it again")
         txt_sp("Sorry I can't hear you, Could you repeat it again")
        
        
            

            
            







  
  
  
  
  



