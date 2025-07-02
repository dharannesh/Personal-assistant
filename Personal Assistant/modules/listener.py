import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎤 Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=0.3)  
        print("Listening now...")

        try:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=4) 
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()

        except sr.WaitTimeoutError:
            return "no speech detected."
        except sr.UnknownValueError:
            return "sorry, i didn't catch that."
        except sr.RequestError:
            return "sorry, network error."
