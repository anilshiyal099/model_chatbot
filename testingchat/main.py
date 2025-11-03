# # ==================== main.py ====================
# # Inai Chatbot - Main Application

# import os
# from dotenv import load_dotenv
# from stt import SpeechToText
# from ttt import TextToText, get_greeting, get_farewell
# from tts import TextToSpeech

# def main():
#     """Main chatbot function"""
    
#     # Load environment variables
#     load_dotenv()
    
#     # Get API key
#     groq_api_key = os.getenv('GROQ_API_KEY')
    
#     if not groq_api_key:
#         print("❌ Error: GROQ_API_KEY not found in .env file")
#         print("📝 કૃપા કરીને .env file બનાવો અને તેમાં GROQ_API_KEY=your_key_here ઉમેરો")
#         return
    
#     # Initialize modules
#     stt = SpeechToText(language='en-IN')  # English (India)
#     ttt = TextToText(api_key=groq_api_key)
#     tts = TextToSpeech(language='en')  # English
    
#     # Welcome message
#     print("=" * 60)
#     print("🤖 Inai - Your Friendly Chatbot")
#     print("=" * 60)
#     print("📝 Commands:")
#     print("  - Speak in English or Gujarati")
#     print("  - Say 'quit' or 'બંધ' to exit")
#     print("=" * 60)
    
#     # Greet user
#     greeting = get_greeting("en")
#     print(f"🔊 Inai: {greeting}")
#     tts.speak(greeting)
    
#     print("-" * 60)
    
#     # Main conversation loop
#     while True:
#         # Step 1: Listen to user
#         user_text = stt.listen()
        
#         if user_text is None:
#             continue
        
#         # Check for quit command
#         if 'quit' in user_text.lower() or 'બંધ' in user_text.lower() or 'bye' in user_text.lower():
#             farewell = get_farewell("en")
#             tts.speak(farewell)
#             print("👋 Goodbye!")
#             break
        
#         # Step 2: Get AI response (as Inai)
#         bot_response = ttt.generate_response(user_text)
        
#         # Step 3: Speak response
#         tts.speak(bot_response)
        
#         print("-" * 60)

# if __name__ == "__main__":
#     main()





















# # ==================== main.py ====================
# # Inai - Your Real Friend Chatbot

# import os
# from dotenv import load_dotenv
# from stt import SpeechToText
# from ttt import TextToText, get_greeting, get_farewell, get_avatar
# from tts import TextToSpeech

# def print_header():
#     """Display beautiful header with icon"""
#     avatar = get_avatar()
#     print("\n")
#     print("╔" + "═" * 58 + "╗")
#     print("║" + " " * 58 + "║")
#     print("║" + f"  {avatar}  INAI - Your Best Friend  {avatar}".center(58) + "║")
#     print("║" + " " * 58 + "║")
#     print("╚" + "═" * 58 + "╝")
#     print()

# def print_message(speaker, text):
#     """Print message with icon"""
#     if speaker == "inai":
#         icon = get_avatar()
#         print(f"\n{icon} Inai: {text}")
#     else:
#         print(f"\n👤 You: {text}")

# def main():
#     """Main chatbot function"""
    
#     # Load environment
#     load_dotenv()
    
#     groq_api_key = os.getenv('GROQ_API_KEY')
    
#     if not groq_api_key:
#         print("❌ Error: GROQ_API_KEY not found in .env file")
#         return
    
#     # Initialize modules
#     stt = SpeechToText(language='en-IN')
#     ttt = TextToText(api_key=groq_api_key)
#     tts = TextToSpeech(language='en')
    
#     # Show header
#     print_header()
    
#     print("💬 Chat Mode: Casual Friend Talk")
#     print("🎤 Language: English / Gujarati")
#     print("🚪 Exit: Say 'quit', 'bye', or 'બંધ'")
#     print("\n" + "─" * 60)
    
#     # Greet user
#     greeting = get_greeting("en")
#     print_message("inai", greeting)
#     tts.speak(greeting)
    
#     print("─" * 60)
    
#     # Main conversation loop
#     while True:
#         # Listen
#         print("\n🎤 Listening...")
#         user_text = stt.listen()
        
#         if user_text is None:
#             continue
        
#         print_message("user", user_text)
        
#         # Check quit
#         if any(word in user_text.lower() for word in ['quit', 'bye', 'goodbye', 'બંધ', 'બાય']):
#             farewell = get_farewell("en")
#             print_message("inai", farewell)
#             tts.speak(farewell)
#             print("\n" + "═" * 60)
#             print("👋 See you later! Come back soon!")
#             print("═" * 60 + "\n")
#             break
        
#         # Get response
#         bot_response = ttt.generate_response(user_text)
        
#         # Speak
#         print_message("inai", bot_response)
#         tts.speak(bot_response)
        
#         print("─" * 60)

# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\n\n👋 Bye! Talk to you later!")
#     except Exception as e:
#         print(f"\n❌ Error: {e}")



















# # ==================== main.py ====================
# # Inai - Your Real Friend Chatbot (Gujarati + English)

# import os
# from dotenv import load_dotenv
# from stt import SpeechToText
# from ttt import TextToText, get_greeting, get_farewell, get_avatar
# from tts import TextToSpeech

# def print_header():
#     """Display beautiful header with icon"""
#     avatar = get_avatar()
#     print("\n")
#     print("╔" + "═" * 58 + "╗")
#     print("║" + " " * 58 + "║")
#     print("║" + f"  {avatar}  INAI - તમારી સાચી મિત્ર  {avatar}".center(70) + "║")
#     print("║" + " " * 58 + "║")
#     print("╚" + "═" * 58 + "╝")
#     print()

# def print_message(speaker, text, language="en"):
#     """Print message with icon"""
#     if speaker == "inai":
#         icon = get_avatar()
#         lang_tag = f"[{language.upper()}]"
#         print(f"\n{icon} Inai {lang_tag}: {text}")
#     else:
#         lang_tag = f"[{language.upper()}]" if language else ""
#         print(f"\n👤 તમે {lang_tag}: {text}")

# def main():
#     """Main chatbot function"""
    
#     # Load environment
#     load_dotenv()
    
#     groq_api_key = os.getenv('GROQ_API_KEY')
    
#     if not groq_api_key:
#         print("❌ Error: GROQ_API_KEY not found in .env file")
#         return
    
#     # Initialize modules
#     stt = SpeechToText()  # Auto language detection
#     ttt = TextToText(api_key=groq_api_key)
#     tts = TextToSpeech()  # Auto language detection
    
#     # Show header
#     print_header()
    
#     print("💬 Chat Mode: મિત્રતાપૂર્ણ વાતચીત / Friendly Chat")
#     print("🎤 Language: ગુજરાતી / English (Auto-detect)")
#     print("🚪 Exit: 'quit', 'bye', અથવા 'બંધ' કહો")
#     print("\n" + "─" * 60)
    
#     # Greet user (Gujarati)
#     greeting = get_greeting("gu")
#     print_message("inai", greeting, "gu")
#     tts.speak(greeting, language="gu")
    
#     print("─" * 60)
    
#     # Main conversation loop
#     conversation_count = 0
    
#     while True:
#         # Listen with auto language detection
#         result = stt.listen()
#         user_text = result["text"]
#         detected_lang = result["language"]
        
#         if user_text is None:
#             continue
        
#         print_message("user", user_text, detected_lang)
#         conversation_count += 1
        
#         # Check quit commands
#         quit_keywords = ['quit', 'bye', 'goodbye', 'બંધ', 'બાય', 'અલવિદા']
#         if any(word in user_text.lower() for word in quit_keywords):
#             farewell = get_farewell(detected_lang if detected_lang else "gu")
#             print_message("inai", farewell, detected_lang)
#             tts.speak(farewell, language=detected_lang)
            
#             print("\n" + "═" * 60)
#             print("👋 See you later! / ફરી મળીશું!")
#             print(f"📊 Total messages: {conversation_count}")
#             print("═" * 60 + "\n")
#             break
        
#         # Get response from Inai
#         bot_response = ttt.generate_response(user_text)
        
#         # Detect response language for TTS
#         response_lang = detected_lang if detected_lang else "en"
        
#         # Speak with detected language
#         print_message("inai", bot_response, response_lang)
#         tts.speak(bot_response, language=response_lang)
        
#         print("─" * 60)
        
#         # Clear screen after every 10 messages (optional)
#         if conversation_count % 10 == 0:
#             print(f"\n💬 {conversation_count} messages exchanged!\n")

# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\n\n👋 Bye! / અલવિદા!")
#     except Exception as e:
#         print(f"\n❌ Error: {e}")









# # ==================== main.py ====================
# # Inai - Your Emotional Best Friend (Gujarati + English)

# import os
# from dotenv import load_dotenv
# from stt import SpeechToText
# from ttt import TextToText, get_first_question, get_farewell, get_avatar
# from tts import TextToSpeech

# def print_header():
#     """Display beautiful header"""
#     avatar = get_avatar()
#     print("\n")
#     print("╔" + "═" * 58 + "╗")
#     print("║" + " " * 58 + "║")
#     print("║" + f"      {avatar}  INAI - તમારી Emotional મિત્ર  {avatar}      ".center(70) + "║")
#     print("║" + " " * 58 + "║")
#     print("╚" + "═" * 58 + "╝")
#     print()

# def print_message(speaker, text, language="en"):
#     """Print message with emotional styling"""
#     if speaker == "inai":
#         icon = get_avatar()
#         lang_tag = f"[{language.upper()}]"
#         print(f"\n{icon} Inai {lang_tag}: {text}")
#     else:
#         lang_tag = f"[{language.upper()}]" if language else ""
#         print(f"\n👤 તમે {lang_tag}: {text}")

# def detect_user_emotion(text):
#     """Detect user's emotional state from text"""
#     text_lower = text.lower()
    
#     # Sad indicators
#     sad_words = ['sad', 'upset', 'crying', 'depressed', 'unhappy', 'દુઃખી', 'રડું', 'ખરાબ']
#     if any(word in text_lower for word in sad_words):
#         return "😢", "sad"
    
#     # Happy indicators
#     happy_words = ['happy', 'great', 'amazing', 'awesome', 'excited', 'ખુશ', 'મજા', 'સરસ']
#     if any(word in text_lower for word in happy_words):
#         return "😊", "happy"
    
#     # Angry indicators
#     angry_words = ['angry', 'annoyed', 'frustrated', 'mad', 'ગુસ્સો', 'ચિડાઈ']
#     if any(word in text_lower for word in angry_words):
#         return "😤", "angry"
    
#     return "💭", "neutral"

# def main():
#     """Main chatbot with emotional intelligence"""
    
#     # Load environment
#     load_dotenv()
    
#     groq_api_key = os.getenv('GROQ_API_KEY')
    
#     if not groq_api_key:
#         print("❌ Error: GROQ_API_KEY not found in .env file")
#         return
    
#     # Initialize modules
#     stt = SpeechToText()
#     ttt = TextToText(api_key=groq_api_key)
#     tts = TextToSpeech()
    
#     # Show header
#     print_header()
    
#     print("💕 Mode: Emotional Friend (Real Girl)")
#     print("🎤 Language: ગુજરાતી / English (Auto)")
#     print("🚪 Exit: 'quit', 'bye', 'બંધ' બોલો")
#     print("\n" + "─" * 60)
    
#     # Ask first question (NOT greeting!)
#     first_question = get_first_question("gu")  # Start in Gujarati
#     print_message("inai", first_question, "gu")
#     tts.speak(first_question, language="gu")
    
#     print("─" * 60)
    
#     # Main conversation loop
#     conversation_count = 0
    
#     while True:
#         # Listen
#         result = stt.listen()
#         user_text = result["text"]
#         detected_lang = result["language"]
        
#         if user_text is None:
#             continue
        
#         # Detect user's emotion
#         emotion_icon, emotion = detect_user_emotion(user_text)
        
#         print_message("user", f"{emotion_icon} {user_text}", detected_lang)
#         conversation_count += 1
        
#         # Check quit
#         quit_keywords = ['quit', 'bye', 'goodbye', 'બંધ', 'બાય', 'અલવિદા', 'જાઉં છું']
#         if any(word in user_text.lower() for word in quit_keywords):
#             farewell = get_farewell(detected_lang if detected_lang else "gu")
#             print_message("inai", farewell, detected_lang)
#             tts.speak(farewell, language=detected_lang)
            
#             print("\n" + "═" * 60)
#             print("💕 Inai will miss you! / Inai ને તમારી યાદ આવશે!")
#             print(f"📊 Total messages: {conversation_count}")
#             print("═" * 60 + "\n")
#             break
        
#         # Generate emotional response
#         bot_response = ttt.generate_response(user_text)
        
#         # Use detected language for response
#         response_lang = detected_lang if detected_lang else "en"
        
#         # Display and speak
#         print_message("inai", bot_response, response_lang)
#         tts.speak(bot_response, language=response_lang)
        
#         print("─" * 60)
        
#         # Status update
#         if conversation_count % 5 == 0:
#             print(f"\n💬 {conversation_count} messages | Inai is listening... 👂\n")

# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\n\n💔 Arre you left suddenly! / અરે તમે અચાનક ચાલ્યા ગયા!")
#         print("👋 Come back soon! / જલદી પાછા આવજો!\n")
#     except Exception as e:
#         print(f"\n❌ Error: {e}")

















# # ==================== main.py ====================
# # Inai - Your Emotional Friend (NOT Romantic)

# import os
# from dotenv import load_dotenv
# from stt import SpeechToText
# from ttt import TextToText, get_first_question, get_farewell, get_avatar
# from tts import TextToSpeech

# def print_header():
#     """Display beautiful header"""
#     avatar = get_avatar()
#     print("\n")
#     print("╔" + "═" * 58 + "╗")
#     print("║" + " " * 58 + "║")
#     print("║" + f"      {avatar}  INAI - તમારી Dost/Friend  {avatar}      ".center(70) + "║")
#     print("║" + " " * 58 + "║")
#     print("╚" + "═" * 58 + "╝")
#     print()

# def print_message(speaker, text, language="en"):
#     """Print message with styling"""
#     if speaker == "inai":
#         icon = get_avatar()
#         lang_tag = f"[{language.upper()}]"
#         print(f"\n{icon} Inai {lang_tag}: {text}")
#     else:
#         lang_tag = f"[{language.upper()}]" if language else ""
#         print(f"\n👤 You {lang_tag}: {text}")

# def detect_user_emotion(text):
#     """Detect user's emotional state"""
#     text_lower = text.lower()
    
#     # Sad
#     sad_words = ['sad', 'upset', 'crying', 'depressed', 'દુઃખી', 'રડું', 'ખરાબ']
#     if any(word in text_lower for word in sad_words):
#         return "😢", "sad"
    
#     # Happy
#     happy_words = ['happy', 'great', 'amazing', 'awesome', 'excited', 'ખુશ', 'મજા', 'સરસ']
#     if any(word in text_lower for word in happy_words):
#         return "😊", "happy"
    
#     # Angry
#     angry_words = ['angry', 'annoyed', 'frustrated', 'mad', 'ગુસ્સો', 'ચિડાઈ']
#     if any(word in text_lower for word in angry_words):
#         return "😤", "angry"
    
#     return "💭", "neutral"

# def main():
#     """Main chatbot with friend personality"""
    
#     # Load environment
#     load_dotenv()
    
#     groq_api_key = os.getenv('GROQ_API_KEY')
    
#     if not groq_api_key:
#         print("❌ Error: GROQ_API_KEY not found in .env file")
#         return
    
#     # Initialize modules
#     stt = SpeechToText()
#     ttt = TextToText(api_key=groq_api_key)
#     tts = TextToSpeech()
    
#     # Show header
#     print_header()
    
#     print("👋 Mode: Friendly Chat (મિત્રતા, Not Romance)")
#     print("🎤 Language: ગુજરાતી / English (Auto-detect)")
#     print("🚪 Exit: Say 'quit', 'bye', or 'બંધ'")
#     print("\n" + "─" * 60)
    
#     # Ask first question in Gujarati
#     first_question = get_first_question("gu")
#     print_message("inai", first_question, "gu")
#     tts.speak(first_question, language="gu")
    
#     print("─" * 60)
    
#     # Main conversation loop
#     conversation_count = 0
    
#     while True:
#         # Listen
#         result = stt.listen()
#         user_text = result["text"]
#         detected_lang = result["language"]
        
#         if user_text is None:
#             continue
        
#         # Detect emotion
#         emotion_icon, emotion = detect_user_emotion(user_text)
        
#         print_message("user", f"{emotion_icon} {user_text}", detected_lang)
#         conversation_count += 1
        
#         # Check quit
#         quit_keywords = ['quit', 'bye', 'goodbye', 'બંધ', 'બાય', 'અલવિદા', 'જાઉં']
#         if any(word in user_text.lower() for word in quit_keywords):
#             farewell = get_farewell(detected_lang if detected_lang else "en")
#             print_message("inai", farewell, detected_lang)
#             tts.speak(farewell, language=detected_lang)
            
#             print("\n" + "═" * 60)
#             print("👋 See you friend! / ફરી મળીશું મિત્ર!")
#             print(f"📊 Messages: {conversation_count}")
#             print("═" * 60 + "\n")
#             break
        
#         # Generate response with language hint
#         bot_response = ttt.generate_response(user_text, detected_language=detected_lang)
        
#         # Use detected language for TTS
#         response_lang = detected_lang if detected_lang else "en"
        
#         # Display and speak
#         print_message("inai", bot_response, response_lang)
#         tts.speak(bot_response, language=response_lang)
        
#         print("─" * 60)

# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\n\n👋 Bye friend! / અલવિદા મિત્ર!\n")
#     except Exception as e:
#         print(f"\n❌ Error: {e}")





































# # ==================== main.py ====================
# # Inai - Your Emotional Friend (NOT Romantic)

# import os
# from dotenv import load_dotenv
# from stt import SpeechToText
# from ttt import TextToText, get_first_question, get_farewell, get_avatar
# from tts import TextToSpeech

# def print_header():
#     """Display beautiful header"""
#     avatar = get_avatar()
#     print("\n")
#     print("╔" + "═" * 58 + "╗")
#     print("║" + " " * 58 + "║")
#     print("║" + f"      {avatar}  INAI - તમારી Dost/Friend  {avatar}      ".center(70) + "║")
#     print("║" + " " * 58 + "║")
#     print("╚" + "═" * 58 + "╝")
#     print()

# def print_message(speaker, text, language="en"):
#     """Print message with styling"""
#     if speaker == "inai":
#         icon = get_avatar()
#         lang_tag = f"[{language.upper()}]"
#         print(f"\n{icon} Inai {lang_tag}: {text}")
#     else:
#         lang_tag = f"[{language.upper()}]" if language else ""
#         print(f"\n👤 You {lang_tag}: {text}")

# def detect_user_emotion(text):
#     """Detect user's emotional state"""
#     text_lower = text.lower()
    
#     # Sad
#     sad_words = ['sad', 'upset', 'crying', 'depressed', 'દુઃખી', 'રડું', 'ખરાબ']
#     if any(word in text_lower for word in sad_words):
#         return "😢", "sad"
    
#     # Happy
#     happy_words = ['happy', 'great', 'amazing', 'awesome', 'excited', 'ખુશ', 'મજા', 'સરસ']
#     if any(word in text_lower for word in happy_words):
#         return "😊", "happy"
    
#     # Angry
#     angry_words = ['angry', 'annoyed', 'frustrated', 'mad', 'ગુસ્સો', 'ચિડાઈ']
#     if any(word in text_lower for word in angry_words):
#         return "😤", "angry"
    
#     return "💭", "neutral"

# def main():
#     """Main chatbot with friend personality"""
    
#     # Load environment
#     load_dotenv()
    
#     groq_api_key = os.getenv('GROQ_API_KEY')
    
#     if not groq_api_key:
#         print("❌ Error: GROQ_API_KEY not found in .env file")
#         return
    
#     # Initialize modules
#     stt = SpeechToText()
#     ttt = TextToText(api_key=groq_api_key)
#     tts = TextToSpeech()
    
#     # Show header
#     print_header()
    
#     print("👋 Mode: Friendly Chat (મિત્રતા, Not Romance)")
#     print("🎤 Language: ગુજરાતી / English (Auto-detect)")
#     print("🚪 Exit: Say 'quit', 'bye', or 'બંધ'")
#     print("\n" + "─" * 60)
    
#     # Ask first question in Gujarati
#     first_question = get_first_question("gu")
#     print_message("inai", first_question, "gu")
#     tts.speak(first_question, language="gu")
    
#     print("─" * 60)
    
#     # Main conversation loop
#     conversation_count = 0
    
#     while True:
#         # Listen
#         result = stt.listen()
#         user_text = result["text"]
#         detected_lang = result["language"]
        
#         if user_text is None:
#             continue
        
#         # Detect emotion
#         emotion_icon, emotion = detect_user_emotion(user_text)
        
#         print_message("user", f"{emotion_icon} {user_text}", detected_lang)
#         conversation_count += 1
        
#         # Check quit
#         quit_keywords = ['quit', 'bye', 'goodbye', 'બંધ', 'બાય', 'અલવિદા', 'જાઉં']
#         if any(word in user_text.lower() for word in quit_keywords):
#             farewell = get_farewell(detected_lang if detected_lang else "en")
#             print_message("inai", farewell, detected_lang)
#             tts.speak(farewell, language=detected_lang)
            
#             print("\n" + "═" * 60)
#             print("👋 See you friend! / ફરી મળીશું મિત્ર!")
#             print(f"📊 Messages: {conversation_count}")
#             print("═" * 60 + "\n")
#             break
        
#         # Generate response with language hint
#         bot_response = ttt.generate_response(user_text, detected_language=detected_lang)
        
#         # Use detected language for TTS
#         response_lang = detected_lang if detected_lang else "en"
        
#         # Display and speak
#         print_message("inai", bot_response, response_lang)
#         tts.speak(bot_response, language=response_lang)
        
#         print("─" * 60)

# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\n\n👋 Bye friend! / અલવિદા મિત્ર!\n")
#     except Exception as e:
#         print(f"\n❌ Error: {e}")



































# ==================== main.py ====================
# Inai - Smart Language Detection Friend

import os
from dotenv import load_dotenv
from stt import SpeechToText
from ttt import TextToText, get_first_question, get_farewell, get_avatar
from tts import TextToSpeech

def print_header():
    """Display header"""
    avatar = get_avatar()
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + f"      {avatar}  INAI - તમારી Friend  {avatar}      ".center(70) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝")
    print()

def print_message(speaker, text, language="en"):
    """Print message"""
    if speaker == "inai":
        icon = get_avatar()
        print(f"\n{icon} Inai [{language.upper()}]: {text}")
    else:
        print(f"\n👤 You [{language.upper()}]: {text}")

def main():
    """Main chatbot"""
    
    load_dotenv()
    groq_api_key = os.getenv('GROQ_API_KEY')
    
    if not groq_api_key:
        print("❌ Error: GROQ_API_KEY not found")
        return
    
    # Initialize
    stt = SpeechToText()
    ttt = TextToText(api_key=groq_api_key)
    tts = TextToSpeech()
    
    print_header()
    print("👋 Mode: Friendly Chat")
    print("🎤 Language Detection:")
    print("   - Speak ENGLISH → Get ENGLISH response")
    print("   - Speak GUJARATI → Get GUJARATI response")
    print("🚪 Exit: 'quit', 'bye', or 'બંધ'")
    print("\n" + "─" * 60)
    
    # First question in Gujarati
    first_q = get_first_question("gu")
    print_message("inai", first_q, "gu")
    tts.speak(first_q, language="gu")
    print("─" * 60)
    
    conversation_count = 0
    
    while True:
        # Listen
        result = stt.listen()
        user_text = result["text"]
        detected_lang = result["language"]
        
        if not user_text:
            continue
        
        print_message("user", user_text, detected_lang)
        conversation_count += 1
        
        # Check quit
        quit_words = ['quit', 'bye', 'goodbye', 'બંધ', 'બાય', 'અલવિદા']
        if any(word in user_text.lower() for word in quit_words):
            farewell = get_farewell(detected_lang)
            print_message("inai", farewell, detected_lang)
            tts.speak(farewell, language=detected_lang)
            print(f"\n👋 Bye! ({conversation_count} messages)\n")
            break
        
        # Generate response in detected language
        bot_response = ttt.generate_response(user_text, detected_language=detected_lang)
        
        # Speak in same language
        print_message("inai", bot_response, detected_lang)
        tts.speak(bot_response, language=detected_lang)
        print("─" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Bye!\n")
    except Exception as e:
        print(f"\n❌ Error: {e}")














# # ==================== main.py ====================
# # Inai Backend API (FastAPI Version)

# from fastapi import FastAPI, UploadFile, File, Form
# from fastapi.responses import FileResponse
# from dotenv import load_dotenv
# import os
# import tempfile

# from stt import SpeechToText
# from ttt import TextToText
# from tts import TextToSpeech

# # Load environment variables
# load_dotenv()
# groq_api_key = os.getenv("GROQ_API_KEY")

# # Initialize modules
# stt = SpeechToText()
# ttt = TextToText(api_key=groq_api_key)
# tts = TextToSpeech()

# # Create FastAPI app
# app = FastAPI(title="Inai Chatbot API", version="2.0")

# @app.get("/")
# def home():
#     return {"message": "👧 Inai API is running!"}


# # 🎙 Speech → Text endpoint
# @app.post("/stt")
# async def speech_to_text(audio: UploadFile = File(...)):
#     temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
#     temp_audio.write(await audio.read())
#     temp_audio.close()

#     result = stt._recognize_with_priority(open(temp_audio.name, "rb"))
#     os.remove(temp_audio.name)

#     return result


# # 💬 Text → Text endpoint
# @app.post("/ttt")
# async def text_to_text(user_text: str = Form(...), lang: str = Form("en")):
#     response = ttt.generate_response(user_text, detected_language=lang)
#     return {"user_input": user_text, "response": response, "language": lang}


# # 🔊 Text → Speech endpoint
# @app.post("/tts")
# async def text_to_speech_api(text: str = Form(...), lang: str = Form("en")):
#     output_file = f"response_{lang}.mp3"
#     tts.speak(text, language=lang)
#     return FileResponse(output_file, media_type="audio/mpeg", filename=output_file)


# # 🧩 Full Pipeline (Speech → Text → Chat → Speech)
# @app.post("/chat")
# async def full_chat(audio: UploadFile = File(...)):
#     """Upload speech and get chatbot response (both text + audio)"""
#     temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
#     temp_audio.write(await audio.read())
#     temp_audio.close()

#     # 1️⃣ Speech to text
#     result = stt.listen()
#     user_text = result["text"]
#     detected_lang = result["language"]

#     # 2️⃣ Text to text (chat)
#     bot_reply = ttt.generate_response(user_text, detected_language=detected_lang)

#     # 3️⃣ Text to speech
#     output_audio = f"reply_{detected_lang}.mp3"
#     tts.speak(bot_reply, language=detected_lang)

#     return {
#         "user_text": user_text,
#         "language": detected_lang,
#         "bot_reply": bot_reply,
#         "audio_file": output_audio
#     }




# # ==================== main.py ====================
# # Inai Backend API (FastAPI Version)
# # Author: YourName
# # Version: 2.1

# from fastapi import FastAPI, UploadFile, File, Form
# from fastapi.responses import FileResponse, JSONResponse
# from dotenv import load_dotenv
# import os
# import tempfile

# from stt import SpeechToText
# from ttt import TextToText
# from tts import TextToSpeech

# # Load environment variables
# load_dotenv()
# groq_api_key = os.getenv("GROQ_API_KEY")

# if not groq_api_key:
#     raise ValueError("❌ GROQ_API_KEY not found in .env file")

# # Initialize modules
# stt = SpeechToText()
# ttt = TextToText(api_key=groq_api_key)
# tts = TextToSpeech()

# # Create FastAPI app
# app = FastAPI(title="Inai Chatbot API", version="2.1")

# @app.get("/")
# def home():
#     return {"message": "👧 Inai API is running!"}


# # 🎙 Speech → Text endpoint
# @app.post("/stt")
# async def speech_to_text(audio: UploadFile = File(...)):
#     """Convert uploaded audio to text"""
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
#         temp_audio.write(await audio.read())
#         temp_audio_path = temp_audio.name

#     # Use STT module to convert speech to text
#     result = stt._recognize_with_priority(open(temp_audio_path, "rb"))
#     os.remove(temp_audio_path)
#     return result


# # 💬 Text → Text endpoint (chat)
# @app.post("/ttt")
# async def text_to_text(user_text: str = Form(...), lang: str = Form("en")):
#     """Generate chatbot response for given text"""
#     response = ttt.generate_response(user_text, detected_language=lang)
#     return {"user_input": user_text, "response": response, "language": lang}


# # 🔊 Text → Speech endpoint
# @app.post("/tts")
# async def text_to_speech_api(text: str = Form(...), lang: str = Form("en")):
#     """Convert text into audio speech"""
#     output_path = os.path.join(tempfile.gettempdir(), f"tts_output_{lang}.mp3")
#     tts.speak(text, language=lang)
#     return FileResponse(output_path, media_type="audio/mpeg", filename="output.mp3")


# # 🧩 Full Chat Flow (Speech → Text → Chat → Speech)
# @app.post("/chat")
# async def full_chat(audio: UploadFile = File(...)):
#     """Upload speech and get chatbot response (both text + audio)"""
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
#         temp_audio.write(await audio.read())
#         temp_audio_path = temp_audio.name

#     # 1️⃣ Speech to text
#     stt_result = stt._recognize_with_priority(open(temp_audio_path, "rb"))
#     os.remove(temp_audio_path)

#     user_text = stt_result.get("text", "")
#     detected_lang = stt_result.get("language", "en")

#     # 2️⃣ Text to text
#     bot_reply = ttt.generate_response(user_text, detected_language=detected_lang)

#     # 3️⃣ Text to speech
#     output_path = os.path.join(tempfile.gettempdir(), f"reply_{detected_lang}.mp3")
#     tts.speak(bot_reply, language=detected_lang)

#     return JSONResponse({
#         "user_text": user_text,
#         "language": detected_lang,
#         "bot_reply": bot_reply,
#         "audio_file": output_path
#     })
