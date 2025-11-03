# # tts.py
# import os
# import requests
# from dotenv import load_dotenv
# from pathlib import Path

# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# GROQ_BASE_URL = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")
# OUTPUT_DIR = Path("output_audio")
# OUTPUT_DIR.mkdir(exist_ok=True)

# def tts_with_groq_text_to_speech(text: str, filename: str = "out.wav", voice: str = "alloy") -> str:
#     """
#     Request Groq TTS (OpenAI-compatible style). Endpoint path may vary — update if Groq docs specify different.
#     Returns local file path of generated wav.
#     """
#     if not GROQ_API_KEY:
#         raise RuntimeError("GROQ_API_KEY not set in environment")

#     url = f"{GROQ_BASE_URL}/audio/speech"   # common openai-like path; change if your provider uses something else
#     headers = {
#         "Authorization": f"Bearer {GROQ_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "model": "llama-3.3-70b-versatile",   # example model name — change as per GroqConsole available models
#         "voice": voice,
#         "input": text,
#         "format": "wav"
#     }

#     resp = requests.post(url, headers=headers, json=payload, stream=True)
#     out_path = OUTPUT_DIR / filename
#     if resp.status_code == 200:
#         # stream bytes to file
#         with open(out_path, "wb") as f:
#             for chunk in resp.iter_content(chunk_size=8192):
#                 if chunk:
#                     f.write(chunk)
#         return str(out_path)
#     else:
#         raise RuntimeError(f"TTS request failed: {resp.status_code} {resp.text}")

# def tts_fallback_pyttsx3(text: str, filename: str = "out_local.wav") -> str:
#     """
#     Local fallback using pyttsx3 (offline). Slightly lower quality but no API cost.
#     """
#     try:
#         import pyttsx3
#     except ImportError:
#         raise RuntimeError("pyttsx3 not installed. Run: pip install pyttsx3")

#     engine = pyttsx3.init()
#     out_path = OUTPUT_DIR / filename
#     engine.save_to_file(text, str(out_path))
#     engine.runAndWait()
#     return str(out_path)






















import os
# playsound, gtts ની પ્લેબેક માટે જરૂરી છે.
# pyttsx3 ને gTTS થી બદલી રહ્યા છીએ.
from playsound import playsound 
from gtts import gTTS 
from dotenv import load_dotenv

load_dotenv()

# કસ્ટમ વોઇસ ફાઇલ પાથ હટાવી દઈએ, કારણ કે આપણે Dynamic TTS વાપરીએ છીએ.

def speak_text(text, language='auto'):
    """
    gTTS નો ઉપયોગ કરીને આપેલ ટેક્સ્ટને સ્પીચમાં કન્વર્ટ કરે છે અને તેને પ્લે કરે છે.
    """
    print(f"TTS (gTTS): {text}")
    try:
        # ભાષા નક્કી કરો: જો ટેક્સ્ટ અંગ્રેજી જેવું લાગે, તો 'en' વાપરો, નહિતર 'gu'
        lang = 'gu'
        if any(c.isalpha() and c.isascii() for c in text): # સરળ ભાષા અનુમાન
             lang = 'en'
        
        # gTTS ઓબ્જેક્ટ બનાવો અને MP3 ફાઇલમાં સેવ કરો
        tts = gTTS(text=text, lang=lang)
        temp_file = "temp_speech.mp3"
        tts.save(temp_file)
        
        # MP3 ફાઇલ પ્લે કરો
        playsound(temp_file)
        
        # ફાઇલ ડિલીટ કરો
        os.remove(temp_file)

    except Exception as e:
        print(f"gTTS/Playsound માં ભૂલ આવી: {e}")
        # જો કોઈ ભૂલ આવે, તો fallback તરીકે pyttsx3 નો ઉપયોગ કરી શકાય.
        # પરંતુ સરળતા માટે, માત્ર ભૂલ દર્શાવીએ છીએ.

# સરળ પરીક્ષણ માટે (જરૂર હોય તો)
if __name__ == '__main__':
    # gTTS વાપરવા માટે ઈન્ટરનેટ કનેક્શન જરૂરી છે.
    speak_text("કેમ છો મિત્ર? હું ઇનાઇ છું અને હું તમારી મદદ કરવા માટે અહીં છું.", 'gu')
    speak_text("Hello friend! I am Inai and I am here to help you.", 'en')