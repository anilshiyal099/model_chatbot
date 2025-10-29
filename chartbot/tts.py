
# ==================== tts.py ====================
# Text-to-Speech Module (Updated with pygame)

from gtts import gTTS
import os
import pygame
import time

class TextToSpeech:
    def __init__(self, language='en'):
        self.language = language
        self.temp_file = "temp_audio.mp3"
        # pygame mixer initialize કરો
        pygame.mixer.init()
    
    def speak(self, text):
        """Text ને audio માં convert કરો અને play કરો"""
        try:
            print(f"🔊 Bot: {text}")
            
            # Text ને speech માં convert કરો
            tts = gTTS(text=text, lang=self.language, slow=False)
            tts.save(self.temp_file)
            
            # Audio play કરો
            pygame.mixer.music.load(self.temp_file)
            pygame.mixer.music.play()
            
            # Audio પૂરો થાય ત્યાં સુધી રાહ જુઓ
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            
            # Temp file delete કરો
            pygame.mixer.music.unload()
            if os.path.exists(self.temp_file):
                os.remove(self.temp_file)
                
        except Exception as e:
            print(f"❌ Error in speech: {e}")
    
    def __del__(self):
        """Cleanup"""
        try:
            pygame.mixer.quit()
            if os.path.exists(self.temp_file):
                os.remove(self.temp_file)
        except:
            pass
