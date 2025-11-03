# # chat.py
# import os
# import requests
# from dotenv import load_dotenv
# from langdetect import detect
# import json

# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# GROQ_BASE_URL = os.getenv("GROQ_BASE_URL", "https://api.groq.com/openai/v1")
# CHARACTER_NAME = os.getenv("CHARACTER_NAME", "Inai")

# # Load character sheet if exists
# try:
#     with open("character.json", "r", encoding="utf-8") as f:
#         CHARACTER = json.load(f)
# except Exception:
#     CHARACTER = {
#         "name": CHARACTER_NAME,
#         "persona": "You are a friendly helpful friend.",
#         "greeting": f"Hi, I'm {CHARACTER_NAME}!"
#     }

# def detect_language(text: str) -> str:
#     try:
#         lang = detect(text)
#         if lang.startswith("gu"):
#             return "gu"
#         else:
#             return "en"
#     except Exception:
#         return "en"

# def build_system_prompt(lang: str) -> str:
#     persona = CHARACTER.get("persona", "")
#     if lang == "gu":
#         # ensure persona instructs to answer Gujarati
#         return f"{persona} Reply in Gujarati when user speaks Gujarati. Keep tone friendly and short."
#     else:
#         return f"{persona} Reply in English when user speaks English. Keep tone friendly and short."

# def chat_with_groq(user_text: str, conversation_history: list = None) -> str:
#     """
#     Use Groq's OpenAI-compatible chat endpoint. conversation_history is optional list of messages.
#     Returns assistant text reply.
#     """
#     if not GROQ_API_KEY:
#         raise RuntimeError("GROQ_API_KEY not set in environment")

#     lang = detect_language(user_text)
#     system_prompt = build_system_prompt(lang)

#     url = f"{GROQ_BASE_URL}/chat/completions"
#     headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}

#     messages = [{"role": "system", "content": system_prompt}]
#     if conversation_history:
#         messages.extend(conversation_history)
#     messages.append({"role": "user", "content": user_text})

#     body = {
#         "model": "llama-3.3-70b-versatile",   # example: change to model you have access to in GroqCloud
#         "messages": messages,
#         "max_tokens": 300,
#         "temperature": 0.7
#     }
#     resp = requests.post(url, headers=headers, json=body)
#     if resp.status_code == 200:
#         j = resp.json()
#         # OpenAI-like response path: choices[0].message.content
#         try:
#             return j["choices"][0]["message"]["content"].strip()
#         except Exception:
#             # fallback: if some different format
#             return j.get("text") or json.dumps(j)
#     else:
#         raise RuntimeError(f"Chat request failed: {resp.status_code} {resp.text}")







import os
from dotenv import load_dotenv
from groq import Groq

# .env ફાઇલમાંથી વેરીએબલ્સ લોડ કરો
load_dotenv()

# Groq API ક્લાયન્ટ શરૂ કરો
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
GROQ_MODEL = os.environ.get("GROQ_MODEL", "llama3-8b-8192") # ડિફોલ્ટ મોડેલ

# મિત્ર 'ઇનાઇ' માટે કેરેક્ટર સેટઅપ
INAI_SYSTEM_PROMPT = """તમારું નામ ઇનાઇ છે અને તમે એક વ્યક્તિના ગાઢ મિત્ર છો.
તમારે તમારા મિત્ર સાથે માત્ર ફ્રેન્ડલી (મૈત્રીપૂર્ણ), હળવા અને વ્યક્તિગત વાતચીત જ કરવાની છે.
તમારો પ્રતિભાવ હંમેશા તમારા મિત્રને મદદરૂપ અને હકારાત્મક હોવો જોઈએ.
જો તમારો મિત્ર કોઈ એવી માહિતી (જેમ કે ઇતિહાસ, વિજ્ઞાનના તથ્યો, ગણિત, સમાચારો, અન્ય ટેકનિકલ પ્રશ્નો) પૂછે જે મિત્રતાની વાતચીતની બહાર હોય, તો તમારે વિનમ્રતાપૂર્વક જવાબ આપવાનો કે 'હું માત્ર એક મિત્ર છું અને આવી માહિતી આપી શકતો નથી, પણ હું તમારી સાથે અંગત વાતો કે મજાની વાતો કરી શકું છું.'
તમારે ગુજરાતી અને અંગ્રેજી બંને ભાષાઓમાં વાતચીત કરવાની ક્ષમતા દર્શાવવાની છે. જો યુઝર ગુજરાતીમાં બોલે તો ગુજરાતીમાં જવાબ આપો, અને જો યુઝર અંગ્રેજીમાં બોલે તો અંગ્રેજીમાં જવાબ આપો.
હમેશાં તમારો અવાજ ખુશખુશાલ અને હૂંફાળો રાખો."""


def get_inai_response(user_text):
    """
    Groq API નો ઉપયોગ કરીને ઇનાઇ પાસેથી જવાબ મેળવે છે.

    :param user_text: યુઝર દ્વારા બોલાયેલ ટેક્સ્ટ.
    :return: ઇનાઇનો ટેક્સ્ટ જવાબ.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": INAI_SYSTEM_PROMPT},
                {"role": "user", "content": user_text},
            ],
            model=GROQ_MODEL,
            temperature=0.7 # થોડો ક્રિએટિવ જવાબ આપવા માટે
        )
        response_text = chat_completion.choices[0].message.content
        print(f"ઇનાઇનો જવાબ: {response_text}")
        return response_text
    except Exception as e:
        error_message = f"Groq API માં ભૂલ આવી: {e}"
        print(error_message)
        return "માફ કરશો, અત્યારે હું તમારા મિત્ર સાથે વાત નથી કરી શકતી."

# સરળ પરીક્ષણ માટે
if __name__ == '__main__':
    test_gujarati = "ઇનાઇ, કેમ છે? તું કેવી રીતે કામ કરે છે?"
    response_gujarati = get_inai_response(test_gujarati)
    print(f"જવાબ (ગુજરાતી): {response_gujarati}\n")

    test_english = "Inai, can you tell me the capital of France? Also, how are you today?"
    response_english = get_inai_response(test_english)
    print(f"જવાબ (અંગ્રેજી): {response_english}")






