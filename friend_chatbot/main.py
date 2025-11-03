# # main.py
# import os
# from dotenv import load_dotenv
# import argparse
# from ttt import chat_with_groq, detect_language
# from tts import tts_with_groq_text_to_speech, tts_fallback_pyttsx3
# from stt import transcribe

# load_dotenv()

# def run_text_mode(text: str, speak: bool = False):
#     reply = chat_with_groq(text)
#     print("--- Inai says ---")
#     print(reply)
#     if speak:
#         try:
#             audio_path = tts_with_groq_text_to_speech(reply, filename="inai_reply.wav")
#         except Exception as e:
#             print("TTS via Groq failed, using local fallback:", e)
#             audio_path = tts_fallback_pyttsx3(reply, filename="inai_reply_local.wav")
#         print("Audio saved to:", audio_path)

# def run_audio_mode(audio_path: str, speak: bool = True):
#     print("Transcribing audio...")
#     text = transcribe(audio_path)
#     if not text:
#         print("Couldn't transcribe audio.")
#         return
#     print("You said:", text)
#     reply = chat_with_groq(text)
#     print("--- Inai replies ---")
#     print(reply)
#     if speak:
#         try:
#             audio_path = tts_with_groq_text_to_speech(reply, filename="inai_reply_from_audio.wav")
#         except Exception as e:
#             print("TTS via Groq failed, using local fallback:", e)
#             audio_path = tts_fallback_pyttsx3(reply, filename="inai_reply_local2.wav")
#         print("Audio saved to:", audio_path)

# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--text", help="Send a text message to Inai")
#     parser.add_argument("--audio", help="Path to audio file to transcribe then reply")
#     parser.add_argument("--nospeak", action="store_true", help="Don't produce TTS audio")
#     args = parser.parse_args()

#     if args.text:
#         run_text_mode(args.text, speak=not args.nospeak)
#     elif args.audio:
#         run_audio_mode(args.audio, speak=not args.nospeak)
#     else:
#         # interactive quick demo
#         print("Welcome to Inai demo. Type a message (Gujarati or English). Type 'exit' to quit.")
#         while True:
#             text = input("You: ")
#             if text.strip().lower() in ("exit", "quit"):
#                 break
#             run_text_mode(text, speak=False)

# if __name__ == "__main__":
#     main()







































import os
from dotenv import load_dotenv

# મોડ્યુલો ઇમ્પોર્ટ કરો
from stt import record_and_transcribe
from ttt import get_inai_response
from tts import speak_text

# .env ફાઇલ લોડ કરો
load_dotenv()

def main_chat_loop():
    """
    મુખ્ય ચેટ લૂપ ચલાવે છે: STT -> TTT (Groq) -> TTS.
    """
    print("🤖 ઇનાઇ ફ્રેન્ડ ચેટબોટ શરૂ થઈ રહ્યો છે (Groq દ્વારા સંચાલિત) 🤖")
    print("વાતચીત શરૂ કરવા માટે તૈયાર. 'બસ' કહીને ચેટ સમાપ્ત કરી શકાય છે.")

    while True:
        # **1. સ્પીચ-ટુ-ટેક્સ્ટ (STT) - ઇનપુટ**
        # અહીં આપણે STT માટે ડિફોલ્ટ તરીકે ગુજરાતી ભાષાનો ઉપયોગ કરીએ છીએ, 
        # જોકે Google STT બંને ભાષાઓમાં બોલાયેલું ઓળખી શકે છે.
        user_input_text = record_and_transcribe(language="gu-IN") 

        if user_input_text == "SERVICE_ERROR":
            speak_text("સ્પીચ-ટુ-ટેક્સ્ટ સર્વિસમાં ભૂલ આવી છે. કૃપા કરીને થોડીવાર પછી ફરી પ્રયાસ કરો.")
            continue
        elif user_input_text == "UNKNOWN_VALUE" or user_input_text == "NO_SPEECH_DETECTED":
            speak_text("માફ કરશો, હું તમારા શબ્દો સમજી શકી નથી. શું તમે ફરીથી પ્રયાસ કરશો?")
            continue
        
        # લૂપ સમાપ્ત કરવાની શરત
        if user_input_text.lower() in ['બસ', 'stop', 'quit', 'exit']:
            speak_text("આવજો! ફરી મળીશું, મારા મિત્ર.")
            break
        
        # **2. ટેક્સ્ટ-ટુ-ટેક્સ્ટ (TTT) - પ્રોસેસિંગ**
        # Groq API નો ઉપયોગ કરીને ઇનાઇનો જવાબ મેળવો.
        inai_response = get_inai_response(user_input_text)
        
        if inai_response == "માફ કરશો, અત્યારે હું તમારા મિત્ર સાથે વાત નથી કરી શકતી.":
            speak_text(inai_response)
            continue

        # **3. ટેક્સ્ટ-ટુ-સ્પીચ (TTS) - આઉટપુટ**
        # ઇનાઇના જવાબને સ્પીચમાં કન્વર્ટ કરો અને પ્લે કરો.
        speak_text(inai_response)

if __name__ == "__main__":
    # જરૂરી લાઇબ્રેરીઓ ઇન્સ્ટોલ કરો:
    # pip install groq python-dotenv SpeechRecognition playsound pyttsx3
    main_chat_loop()