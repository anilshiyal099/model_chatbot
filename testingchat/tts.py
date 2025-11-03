# # ==================== tts.py ====================
# # Text-to-Speech Module

# from gtts import gTTS
# import os
# import pygame
# import time

# class TextToSpeech:
#     def __init__(self, language='en'):
#         """
#         Initialize Text-to-Speech
        
#         Args:
#             language: 'gu' (Gujarati) or 'en' (English)
#         """
#         self.language = language
#         self.temp_file = "temp_audio.mp3"
#         pygame.mixer.init()
    
#     def speak(self, text):
#         """Convert text to speech and play"""
#         try:
#             print(f"🔊 Inai: {text}")
            
#             # Generate speech
#             tts = gTTS(text=text, lang=self.language, slow=False)
#             tts.save(self.temp_file)
            
#             # Play audio
#             pygame.mixer.music.load(self.temp_file)
#             pygame.mixer.music.play()
            
#             # Wait for audio to finish
#             while pygame.mixer.music.get_busy():
#                 pygame.time.Clock().tick(10)  # Use pygame clock instead of time.sleep
            
#             # Cleanup
#             pygame.mixer.music.unload()
#             if os.path.exists(self.temp_file):
#                 os.remove(self.temp_file)
                
#         except Exception as e:
#             print(f"❌ Speech error: {e}")
    
#     def __del__(self):
#         """Cleanup"""
#         try:
#             pygame.mixer.quit()
#             if os.path.exists(self.temp_file):
#                 os.remove(self.temp_file)
#         except:
#             pass


















# # ==================== tts.py ====================
# # Text-to-Speech Module (Fixed Gujarati Support)

# from gtts import gTTS
# import os
# import pygame
# import time

# class TextToSpeech:
#     def __init__(self):
#         """Initialize Text-to-Speech with language auto-detection"""
#         self.temp_file = "temp_audio.mp3"
#         pygame.mixer.init()
    
#     def speak(self, text, language=None):
#         """
#         Convert text to speech and play
        
#         Args:
#             text: Text to speak
#             language: "gu" (Gujarati) or "en" (English) or None (auto-detect)
#         """
#         try:
#             # Auto-detect language if not provided
#             if language is None:
#                 language = self._detect_language(text)
            
#             print(f"🔊 Inai [{language.upper()}]: {text}")
            
#             # Generate speech with proper language
#             tts = gTTS(text=text, lang=language, slow=False)
#             tts.save(self.temp_file)
            
#             # Play audio
#             pygame.mixer.music.load(self.temp_file)
#             pygame.mixer.music.play()
            
#             # Wait for audio to finish (fixed KeyboardInterrupt issue)
#             while pygame.mixer.music.get_busy():
#                 pygame.time.Clock().tick(10)
            
#             # Small delay before cleanup
#             time.sleep(0.1)
            
#             # Cleanup
#             pygame.mixer.music.unload()
#             if os.path.exists(self.temp_file):
#                 try:
#                     os.remove(self.temp_file)
#                 except:
#                     pass  # Ignore cleanup errors
                    
#         except Exception as e:
#             print(f"❌ Speech error: {e}")
    
#     def _detect_language(self, text):
#         """
#         Detect if text is Gujarati or English
        
#         Args:
#             text: Input text
            
#         Returns:
#             str: "gu" or "en"
#         """
#         # Gujarati Unicode range
#         gujarati_chars = set('અઆઇઈઉઊઋએઐઓઔકખગઘચછજઝઞટઠડઢણતથદધનપફબભમયરલવશષસહળક્ષજ્ઞ')
        
#         # Count Gujarati characters
#         gujarati_count = sum(1 for char in text if char in gujarati_chars)
        
#         # If more than 30% Gujarati characters, use Gujarati
#         if len(text) > 0 and (gujarati_count / len(text)) > 0.3:
#             return "gu"
        
#         return "en"
    
#     def __del__(self):
#         """Cleanup on destroy"""
#         try:
#             pygame.mixer.quit()
#             if os.path.exists(self.temp_file):
#                 os.remove(self.temp_file)
#         except:
#             pass
































# ==================== tts.py ====================
# Text-to-Speech with Real Girl Voice (Emotional)

import os
import asyncio
import edge_tts
import pygame
import time

class TextToSpeech:
    def __init__(self):
        """Initialize TTS with emotional female voices"""
        self.temp_file = "temp_audio.mp3"
        pygame.mixer.init()
        
        # Real female voices (more natural and emotional)
        self.voices = {
            "gu": "gu-IN-DhwaniNeural",      # Gujarati Female (natural)
            "en": "en-IN-NeerjaNeural"       # English Indian Female (expressive)
        }
    
    async def _generate_audio(self, text, language):
        """Generate audio with emotional voice using Edge TTS"""
        voice = self.voices.get(language, self.voices["en"])
        
        # Edge TTS with emotional speech
        communicate = edge_tts.Communicate(
            text=text,
            voice=voice,
            rate="+5%",     # Slightly faster (more natural)
            pitch="+2Hz"    # Slightly higher (more feminine)
        )
        
        await communicate.save(self.temp_file)
    
    def speak(self, text, language=None):
        """
        Speak with emotional real girl voice
        
        Args:
            text: Text to speak (with emojis removed for TTS)
            language: "gu" or "en" or None (auto-detect)
        """
        try:
            # Auto-detect language if not provided
            if language is None:
                language = self._detect_language(text)
            
            # Remove emojis for TTS (they cause issues)
            clean_text = self._remove_emojis(text)
            
            print(f"🔊 Inai [{language.upper()}]: {text}")
            
            # Generate audio with Edge TTS (better quality than gTTS)
            asyncio.run(self._generate_audio(clean_text, language))
            
            # Play audio
            pygame.mixer.music.load(self.temp_file)
            pygame.mixer.music.play()
            
            # Wait for completion
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            time.sleep(0.1)
            
            # Cleanup
            pygame.mixer.music.unload()
            if os.path.exists(self.temp_file):
                try:
                    os.remove(self.temp_file)
                except:
                    pass
                    
        except Exception as e:
            print(f"❌ Speech error: {e}")
    
    def _remove_emojis(self, text):
        """Remove emojis from text for TTS"""
        import re
        # Remove emoji patterns
        emoji_pattern = re.compile(
            "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            "]+", flags=re.UNICODE
        )
        return emoji_pattern.sub(r'', text).strip()
    
    def _detect_language(self, text):
        """Auto-detect Gujarati or English"""
        gujarati_chars = set('અઆઇઈઉઊઋએઐઓઔકખગઘચછજઝઞટઠડઢણતથદધનપફબભમયરલવશષસહળક્ષજ્ઞ')
        gujarati_count = sum(1 for char in text if char in gujarati_chars)
        
        if len(text) > 0 and (gujarati_count / len(text)) > 0.2:
            return "gu"
        return "en"
    
    def __del__(self):
        """Cleanup"""
        try:
            pygame.mixer.quit()
            if os.path.exists(self.temp_file):
                os.remove(self.temp_file)
        except:
            pass