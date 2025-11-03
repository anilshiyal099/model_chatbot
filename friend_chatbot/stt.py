# # stt.py
# import os
# import requests
# from dotenv import load_dotenv
# from langdetect import detect
# import speech_recognition as sr

# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# GROQ_BASE_URL = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")

# def stt_with_groq(audio_path: str) -> str:
#     """
#     Try to use Groq's speech->text endpoint (OpenAI-compatible). If your Groq account
#     has an ASR model, configure model name accordingly.
#     This function expects a wav or mp3 file path.
#     """
#     if not GROQ_API_KEY:
#         raise RuntimeError("GROQ_API_KEY not set in environment")

#     url = f"{GROQ_BASE_URL}/audio/transcriptions"  # openai-like endpoint; may vary
#     headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
#     files = {
#         "file": open(audio_path, "rb")
#     }
#     data = {
#         "model": "whisper-large-v3"  # change to the model your Groq account has
#     }
#     resp = requests.post(url, headers=headers, files=files, data=data)
#     if resp.status_code == 200:
#         j = resp.json()
#         # openai format often returns 'text'
#         return j.get("text") or j.get("transcription") or ""
#     else:
#         # raise or fallback
#         return None

# def stt_fallback_local(audio_path: str) -> str:
#     """Fallback using SpeechRecognition + default recognizer (Sphinx or Google online if available)."""
#     r = sr.Recognizer()
#     ext = audio_path.split(".")[-1].lower()
#     with sr.AudioFile(audio_path) as source:
#         audio = r.record(source)
#     try:
#         # Try Google Web Speech API (requires internet but no key if small usage)
#         text = r.recognize_google(audio)
#         return text
#     except Exception as e:
#         try:
#             return r.recognize_sphinx(audio)  # offline (requires pocketsphinx)
#         except Exception:
#             return ""

# def transcribe(audio_path: str) -> str:
#     """
#     Public function to get transcription text.
#     Will attempt Groq first, and if that fails, use local fallback.
#     """
#     try:
#         text = stt_with_groq(audio_path)
#         if text:
#             return text
#     except Exception as e:
#         # print("Groq STT failed:", e)
#         pass

#     return stt_fallback_local(audio_path)










import speech_recognition as sr

def record_and_transcribe(language="gu-IN"):
    """
    માઇક્રોફોનમાંથી ઓડિયો રેકોર્ડ કરે છે અને તેને ટેક્સ્ટમાં કન્વર્ટ કરે છે.
    
    :param language: ઓળખ માટેની ભાષાનો કોડ (ઉદાહરણ: 'gu-IN' ગુજરાતી માટે, 'en-US' અંગ્રેજી માટે).
    :return: ટ્રાન્સક્રાઇબ્ડ ટેક્સ્ટ અથવા ભૂલ સંદેશ.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("ઇનાઇ સાંભળી રહી છે. કૃપા કરીને બોલો...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return "NO_SPEECH_DETECTED"
    
    try:
        # Google Web Speech API નો ઉપયોગ
        text = r.recognize_google(audio, language=language)
        print(f"તમે કહ્યું: {text}")
        return text
    except sr.UnknownValueError:
        print("માફ કરશો, હું સ્પીચ ઓળખી શકી નથી.")
        return "UNKNOWN_VALUE"
    except sr.RequestError as e:
        print(f"Google Speech Recognition સર્વિસમાંથી ભૂલ આવી; {e}")
        return "SERVICE_ERROR"

# સરળ પરીક્ષણ માટે
if __name__ == '__main__':
    # ગુજરાતી ઓળખવાનો પ્રયાસ
    gujarati_text = record_and_transcribe(language="gu-IN")
    print(f"ગુજરાતી પરિણામ: {gujarati_text}")

    # અંગ્રેજી ઓળખવાનો પ્રયાસ
    # english_text = record_and_transcribe(language="en-US")
    # print(f"અંગ્રેજી પરિણામ: {english_text}")