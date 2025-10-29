
# ==================== main.py ====================
# Main Application

import os
from dotenv import load_dotenv
from stt import SpeechToText
from ttt import TextToText
from tts import TextToSpeech

def main():
    # .env file load કરો
    load_dotenv()
    
    # API key મેળવો
    groq_api_key = os.getenv('GROQ_API_KEY')
    
    if not groq_api_key:
        print("❌ Error: GROQ_API_KEY not found in .env file")
        print("📝 કૃપા કરીને .env file બનાવો અને તેમાં GROQ_API_KEY=your_key_here ઉમેરો")
        return
    
    # Modules initialize કરો
    stt = SpeechToText(language='en-IN')  # ગુજરાતી
    ttt = TextToText(api_key=groq_api_key)
    tts = TextToSpeech(language='en')  # ગુજરાતી
    
    print("=" * 50)
    print("🤖 Speech-to-Speech Chatbot શરૂ થયો!")
    print("=" * 50)
    print("📝 Commands:")
    print("  - ગુજરાતીમાં બોલો chatbot સાથે વાત કરવા")
    print("  - 'quit' કહો બંધ કરવા માટે")
    print("=" * 50)
    
    while True:
        # Step 1: Speech-to-Text
        user_text = stt.listen()
        
        if user_text is None:
            continue
        
        # Quit command check કરો
        if 'quit' in user_text.lower() or 'બંધ' in user_text.lower():
            tts.speak("અલવિદા! મળીશું ફરી!")
            break
        
        # Step 2: Text-to-Text (Generate response)
        bot_response = ttt.generate_response(user_text)
        
        # Step 3: Text-to-Speech (Speak response)
        tts.speak(bot_response)
        
        print("-" * 50)

if __name__ == "__main__":
    main()
