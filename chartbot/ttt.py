
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