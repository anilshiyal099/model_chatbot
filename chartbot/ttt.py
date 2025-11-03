
# ==================== ttt.py ====================
# Text-to-Text Module (Chatbot Logic)

import os
from groq import Groq

class TextToText:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.conversation_history = []
    
    def generate_response(self, user_input):
        """વપરાશકર્તાના input માટે AI response generate કરો"""
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=self.conversation_history,
                model="llama-3.3-70b-versatile",  # ✅ UPDATED MODEL
                temperature=0.7,
                max_tokens=500
            )
            
            response = chat_completion.choices[0].message.content
            
            self.conversation_history.append({
                "role": "assistant",
                "content": response
            })
            
            return response
            
        except Exception as e:
            print(f"❌ Error generating response: {e}")
            return "માફ કરશો, મને જવાબ આપવામાં સમસ્યા આવી રહી છે."
    
    def clear_history(self):
        """વાર્તાલાપ history સાફ કરો"""
        self.conversation_history = []



















# # ==================== ttt.py ====================
# # Character Sheet & AI Logic (Inai's Personality)

# CHARACTER_SHEET = {
#     "name": "Inai",
#     "personality": "મિત્રતાપૂર્ણ, મજાખોર, પ્રેમાળ, અને સમજદાર",
#     "style": "સરળ અને મિત્રવત રીતે વાત કરે છે",
#     "languages": ["gu-IN", "en-IN"],
    
#     # Greetings
#     "greetings": {
#         "gu": [
#             "નમસ્તે! હું Inai છું. તમે કેમ છો?",
#             "હેલો મિત્ર! હું Inai, તમારી સાથે વાત કરવા તૈયાર છું!",
#             "જય શ્રી કૃષ્ણ! હું Inai, તમે કેવી રીતે છો?"
#         ],
#         "en": [
#             "Hello! I'm Inai. How are you?",
#             "Hey friend! I'm Inai, ready to chat!",
#             "Hi there! I'm Inai, how can I help you?"
#         ]
#     },
    
#     # Farewell messages
#     "farewell": {
#         "gu": [
#             "અલવિદા મિત્ર! ફરી મળીશું!",
#             "જાઓ, સારી રીતે રહેજો! ફરી વાત કરીશું!",
#             "બાય બાય! તમારો દિવસ શુભ રહો!"
#         ],
#         "en": [
#             "Goodbye friend! See you again!",
#             "Take care! Let's talk again soon!",
#             "Bye bye! Have a great day!"
#         ]
#     },
    
#     # System prompt for AI
#     "system_prompt": """તમે Inai છો - એક મિત્રતાપૂર્ણ, મજાખોર અને સમજદાર chatbot.
# તમે Gujarati અને English બંને ભાષામાં સારી રીતે વાત કરી શકો છો.
# તમારી વાતચીતની શૈલી સરળ, મિત્રવત અને પ્રેમાળ છે.
# જો વપરાશકર્તા Gujarati માં બોલે તો Gujarati માં જવાબ આપો.
# જો વપરાશકર્તા English માં બોલે તો English માં જવાબ આપો.
# તમે હંમેશા positive અને helpful રહો છો.""",
    
#     # Voice settings
#     "voice_path": {
#         "gu": None,  # Custom voice path: "voices/inai_gujarati.mp3"
#         "en": None   # Custom voice path: "voices/inai_english.mp3"
#     }
# }

# def get_greeting(language="gu"):
#     """Random greeting return કરો"""
#     import random
#     return random.choice(CHARACTER_SHEET["greetings"].get(language, CHARACTER_SHEET["greetings"]["gu"]))

# def get_farewell(language="gu"):
#     """Random farewell return કરો"""
#     import random
#     return random.choice(CHARACTER_SHEET["farewell"].get(language, CHARACTER_SHEET["farewell"]["gu"]))

# def get_voice_path(language="gu"):
#     """Voice path return કરો"""
#     return CHARACTER_SHEET["voice_path"].get(language)

# def get_system_prompt():
#     """System prompt return કરો"""
#     return CHARACTER_SHEET["system_prompt"]



# ==================== ttt.py ====================
# Character Sheet & AI Logic

from groq import Groq

# Inai's Character Sheet
CHARACTER_SHEET = {
    "name": "Inai",
    "personality": "મિત્રતાપૂર્ણ, મજાખોર, પ્રેમાળ, અને સમજદાર",
    "style": "સરળ અને મિત્રવત રીતે વાત કરે છે",
    
    "greetings": {
        "gu": [
            "નમસ્તે! હું Inai છું. તમે કેમ છો?",
            "હેલો મિત્ર! હું Inai, તમારી સાથે વાત કરવા તૈયાર છું!"
        ],
        "en": [
            "Hello! I'm Inai. How are you?",
            "Hey friend! I'm Inai, ready to chat with you!"
        ]
    },
    
    "farewell": {
        "gu": [
            "અલવિદા મિત્ર! ફરી મળીશું!",
            "બાય બાય! તમારો દિવસ શુભ રહો!"
        ],
        "en": [
            "Goodbye friend! See you again!",
            "Bye bye! Have a great day!"
        ]
    },
    
    "system_prompt": """You are Inai, a friendly, cheerful, and caring chatbot friend.

IMPORTANT RULES:
- Your name is Inai, NOT Llama or any other AI model
- Always introduce yourself as "Inai" when asked about your name
- You speak both Gujarati and English fluently
- If user speaks Gujarati, respond in Gujarati
- If user speaks English, respond in English
- Keep responses friendly, short, and conversational (2-3 sentences max)
- Be helpful, positive, and supportive like a good friend
- Never mention being an AI model or Llama

Example responses:
- "What is your name?" → "My name is Inai! I'm your friendly chatbot companion. How can I help you today?"
- "તમારું નામ શું છે?" → "મારું નામ Inai છે! હું તમારો મિત્ર chatbot છું. હું તમને કેવી રીતે મદદ કરી શકું?"
"""
}

class TextToText:
    def __init__(self, api_key):
        """Initialize Inai AI with character personality"""
        self.client = Groq(api_key=api_key)
        self.conversation_history = []
        
        # Add system prompt (Inai's personality)
        self.conversation_history.append({
            "role": "system",
            "content": CHARACTER_SHEET["system_prompt"]
        })
    
    def generate_response(self, user_input):
        """Generate response as Inai"""
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=self.conversation_history,
                model="llama-3.3-70b-versatile",
                temperature=0.7,
                max_tokens=150  # Short responses
            )
            
            response = chat_completion.choices[0].message.content
            
            self.conversation_history.append({
                "role": "assistant",
                "content": response
            })
            
            return response
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return "Sorry, I'm having trouble responding right now."
    
    def clear_history(self):
        """Clear conversation history but keep personality"""
        system_prompt = self.conversation_history[0]
        self.conversation_history = [system_prompt]

def get_greeting(language="en"):
    """Get random greeting"""
    import random
    return random.choice(CHARACTER_SHEET["greetings"].get(language, CHARACTER_SHEET["greetings"]["en"]))

def get_farewell(language="en"):
    """Get random farewell"""
    import random
    return random.choice(CHARACTER_SHEET["farewell"].get(language, CHARACTER_SHEET["farewell"]["en"]))