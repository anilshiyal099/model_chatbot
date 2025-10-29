
# ==================== stt.py ====================
# Speech-to-Text Module

import speech_recognition as sr

class SpeechToText:
    def __init__(self, language='en-IN'):
        self.recognizer = sr.Recognizer()
        self.language = language
    
    def listen(self):
        """માઇક્રોફોનમાંથી audio સાંભળો અને text return કરો"""
        with sr.Microphone() as source:
            print("🎤 બોલો...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = self.recognizer.listen(source)
            
        try:
            print("🔄 Processing...")
            text = self.recognizer.recognize_google(audio, language=self.language)
            print(f"તમે કહ્યું: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ સમજાયું નહીં. ફરીથી પ્રયાસ કરો.")
            return None
        except sr.RequestError as e:
            print(f"❌ Error: {e}")
            return None
