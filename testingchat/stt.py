# # ==================== stt.py ====================
# # Speech-to-Text Module

# import speech_recognition as sr

# class SpeechToText:
#     def __init__(self, language='en-IN'):
#         """
#         Initialize Speech Recognition
        
#         Args:
#             language: 'gu-IN' (Gujarati) or 'en-IN' (English)
#         """
#         self.recognizer = sr.Recognizer()
#         self.language = language
    
#     def listen(self):
#         """Listen from microphone and convert to text"""
#         with sr.Microphone() as source:
#             print("🎤 બોલો...")
#             self.recognizer.adjust_for_ambient_noise(source, duration=1)
#             audio = self.recognizer.listen(source)
            
#         try:
#             print("🔄 Processing...")
#             text = self.recognizer.recognize_google(audio, language=self.language)
#             print(f"✅ તમે કહ્યું: {text}")
#             return text
#         except sr.UnknownValueError:
#             print("❌ સમજાયું નહીં. ફરીથી પ્રયાસ કરો.")
#             return None
#         except sr.RequestError as e:
#             print(f"❌ Error: {e}")
#             return None


























# # ==================== stt.py ====================
# # Speech-to-Text Module (Auto Language Detection)

# import speech_recognition as sr

# class SpeechToText:
#     def __init__(self, language='en-IN'):
#         """
#         Initialize Speech Recognition
        
#         Args:
#             language: 'gu-IN' (Gujarati) or 'en-IN' (English) or 'auto'
#         """
#         self.recognizer = sr.Recognizer()
#         self.language = language
#         self.recognizer.energy_threshold = 4000  # Better detection
#         self.recognizer.dynamic_energy_threshold = True
    
#     def listen(self):
#         """
#         Listen from microphone with auto language detection
        
#         Returns:
#             dict: {"text": "...", "language": "gu/en"}
#         """
#         with sr.Microphone() as source:
#             print("🎤 બોલો... (Gujarati અથવા English)")
#             self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
#             try:
#                 audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
#             except sr.WaitTimeoutError:
#                 print("❌ કંઈ સંભળાયું નહીં")
#                 return {"text": None, "language": None}
        
#         return self._recognize_auto(audio)
    
#     def _recognize_auto(self, audio):
#         """
#         Try both Gujarati and English recognition
        
#         Returns:
#             dict: {"text": "...", "language": "gu/en"}
#         """
#         print("🔄 Processing...")
        
#         # Try Gujarati first
#         try:
#             text_gu = self.recognizer.recognize_google(audio, language="gu-IN")
#             if text_gu and len(text_gu.strip()) > 0:
#                 print(f"✅ [GU] {text_gu}")
#                 return {"text": text_gu, "language": "gu"}
#         except (sr.UnknownValueError, sr.RequestError):
#             pass
        
#         # Try English
#         try:
#             text_en = self.recognizer.recognize_google(audio, language="en-IN")
#             if text_en and len(text_en.strip()) > 0:
#                 print(f"✅ [EN] {text_en}")
#                 return {"text": text_en, "language": "en"}
#         except (sr.UnknownValueError, sr.RequestError):
#             pass
        
#         print("❌ સમજાયું નહીં. ફરીથી પ્રયાસ કરો.")
#         return {"text": None, "language": None}
    
#     def detect_language(self, text):
#         """
#         Detect if text is Gujarati or English
        
#         Args:
#             text: Input text
            
#         Returns:
#             str: "gu" or "en"
#         """
#         # Check for Gujarati Unicode characters
#         gujarati_chars = set('અઆઇઈઉઊઋએઐઓઔકખગઘચછજઝઞટઠડઢણતથદધનપફબભમયરલવશષસહળક્ષજ્ઞ')
        
#         for char in text:
#             if char in gujarati_chars:
#                 return "gu"
        
#         return "en"



























# # ==================== stt.py ====================
# # Speech-to-Text Module (Auto Language Detection)

# import speech_recognition as sr

# class SpeechToText:
#     def __init__(self, language='en-IN'):
#         """
#         Initialize Speech Recognition
        
#         Args:
#             language: 'gu-IN' (Gujarati) or 'en-IN' (English) or 'auto'
#         """
#         self.recognizer = sr.Recognizer()
#         self.language = language
#         self.recognizer.energy_threshold = 4000  # Better detection
#         self.recognizer.dynamic_energy_threshold = True
    
#     def listen(self):
#         """
#         Listen from microphone with auto language detection
        
#         Returns:
#             dict: {"text": "...", "language": "gu/en"}
#         """
#         with sr.Microphone() as source:
#             print("🎤 બોલો... (Gujarati અથવા English)")
#             self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
#             try:
#                 audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
#             except sr.WaitTimeoutError:
#                 print("❌ કંઈ સંભળાયું નહીં")
#                 return {"text": None, "language": None}
        
#         return self._recognize_auto(audio)
    
#     def _recognize_auto(self, audio):
#         """
#         Try both Gujarati and English recognition
        
#         Returns:
#             dict: {"text": "...", "language": "gu/en"}
#         """
#         print("🔄 Processing...")
        
#         # Try Gujarati first
#         try:
#             text_gu = self.recognizer.recognize_google(audio, language="gu-IN")
#             if text_gu and len(text_gu.strip()) > 0:
#                 print(f"✅ [GU] {text_gu}")
#                 return {"text": text_gu, "language": "gu"}
#         except (sr.UnknownValueError, sr.RequestError):
#             pass
        
#         # Try English
#         try:
#             text_en = self.recognizer.recognize_google(audio, language="en-IN")
#             if text_en and len(text_en.strip()) > 0:
#                 print(f"✅ [EN] {text_en}")
#                 return {"text": text_en, "language": "en"}
#         except (sr.UnknownValueError, sr.RequestError):
#             pass
        
#         print("❌ સમજાયું નહીં. ફરીથી પ્રયાસ કરો.")
#         return {"text": None, "language": None}
    
#     def detect_language(self, text):
#         """
#         Detect if text is Gujarati or English
        
#         Args:
#             text: Input text
            
#         Returns:
#             str: "gu" or "en"
#         """
#         # Check for Gujarati Unicode characters
#         gujarati_chars = set('અઆઇઈઉઊઋએઐઓઔકખગઘચછજઝઞટઠડઢણતથદધનપફબભમયરલવશષસહળક્ષજ્ઞ')
        
#         for char in text:
#             if char in gujarati_chars:
#                 return "gu"
        
#         return "en"

























# # ==================== stt.py ====================
# # Speech-to-Text with Smart Language Detection

# import speech_recognition as sr
# import re

# class SpeechToText:
#     def __init__(self):
#         """Initialize Speech Recognition with smart detection"""
#         self.recognizer = sr.Recognizer()
#         self.recognizer.energy_threshold = 4000
#         self.recognizer.dynamic_energy_threshold = True
    
#     def listen(self):
#         """
#         Listen from microphone with smart language detection
        
#         Returns:
#             dict: {"text": "...", "language": "gu/en"}
#         """
#         with sr.Microphone() as source:
#             print("🎤 બોલો... (Gujarati અથવા English)")
#             self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
#             try:
#                 audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
#             except sr.WaitTimeoutError:
#                 print("❌ કંઈ સંભળાયું નહીં")
#                 return {"text": None, "language": None}
        
#         return self._recognize_smart(audio)
    
#     def _recognize_smart(self, audio):
#         """
#         Smart recognition with proper language detection
        
#         Strategy:
#         1. Try English first (most common for mixed input)
#         2. Then try Gujarati
#         3. Use smart logic to determine actual language
#         """
#         print("🔄 Processing...")
        
#         results = {}
        
#         # Try English recognition
#         try:
#             text_en = self.recognizer.recognize_google(audio, language="en-IN")
#             if text_en and len(text_en.strip()) > 0:
#                 results['en'] = text_en
#         except:
#             pass
        
#         # Try Gujarati recognition
#         try:
#             text_gu = self.recognizer.recognize_google(audio, language="gu-IN")
#             if text_gu and len(text_gu.strip()) > 0:
#                 results['gu'] = text_gu
#         except:
#             pass
        
#         # No results
#         if not results:
#             print("❌ સમજાયું નહીં. ફરીથી પ્રયાસ કરો.")
#             return {"text": None, "language": None}
        
#         # Determine actual language using smart logic
#         final_text, final_lang = self._determine_language(results)
        
#         print(f"✅ [{final_lang.upper()}] {final_text}")
#         return {"text": final_text, "language": final_lang}
    
#     def _determine_language(self, results):
#         """
#         Intelligently determine which language was actually spoken
        
#         Args:
#             results: dict with 'en' and/or 'gu' keys
            
#         Returns:
#             tuple: (text, language)
#         """
#         # If only one result, use it
#         if len(results) == 1:
#             lang = list(results.keys())[0]
#             return results[lang], lang
        
#         # Both results available - use smart detection
#         text_en = results.get('en', '')
#         text_gu = results.get('gu', '')
        
#         # Check Gujarati Unicode characters in Gujarati result
#         gujarati_chars = set('અઆઇઈઉઊઋએઐઓઔકખગઘચછજઝઞટઠડઢણતથદધનપફબભમયરલવશષસહળક્ષજ્ઞ')
#         gu_has_gujarati = any(char in gujarati_chars for char in text_gu)
        
#         # Check English-like patterns in English result
#         english_words = ['how', 'are', 'you', 'what', 'is', 'your', 'name', 'the', 'hello', 'hi', 'bye']
#         en_has_english = any(word in text_en.lower() for word in english_words)
        
#         # Decision logic
#         # If Gujarati result has actual Gujarati script → it's Gujarati
#         if gu_has_gujarati:
#             return text_gu, 'gu'
        
#         # If English result has common English words → it's English
#         if en_has_english:
#             return text_en, 'en'
        
#         # Check for transliterated English in Gujarati script
#         # "હાવ આર યુ" should be detected as English
#         transliteration_patterns = [
#             'હાવ', 'આર', 'યુ', 'બાય', 'હેલો', 'થેન્ક', 'યુ'
#         ]
#         if any(pattern in text_gu for pattern in transliteration_patterns):
#             # User said English words, use English result if available
#             if text_en:
#                 return text_en, 'en'
        
#         # Default: prefer English for ambiguous cases
#         if text_en:
#             return text_en, 'en'
        
#         return text_gu, 'gu'
    
#     def detect_language_from_text(self, text):
#         """
#         Detect language from text content
        
#         Args:
#             text: Input text
            
#         Returns:
#             str: "gu" or "en"
#         """
#         # Check for Gujarati Unicode characters
#         gujarati_chars = set('અઆઇઈઉઊઋએઐઓઔકખગઘચછજઝઞટઠડઢણતથદધનપફબભમયરલવશષસહળક્ષજ્ઞ')
        
#         # Count Gujarati characters
#         gujarati_count = sum(1 for char in text if char in gujarati_chars)
        
#         # If more than 20% Gujarati characters, it's Gujarati
#         if len(text) > 0 and (gujarati_count / len(text)) > 0.2:
#             return "gu"
        
#         return "en"

























# ==================== stt.py ====================
# Speech-to-Text with Forced Language Priority

import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        """Initialize Speech Recognition"""
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000
        self.recognizer.dynamic_energy_threshold = True
        
        # Common English words/phrases for detection
        self.english_indicators = [
            'how', 'are', 'you', 'what', 'is', 'your', 'name', 
            'hello', 'hi', 'bye', 'thank', 'thanks', 'please',
            'yes', 'no', 'okay', 'ok', 'the', 'and', 'or',
            'i', 'am', 'my', 'me', 'can', 'will', 'do'
        ]
        
        # Gujarati transliteration patterns (English words in Gujarati script)
        self.transliteration_patterns = [
            'હાવ', 'આર', 'યુ', 'વોટ', 'ઇઝ', 'યોર', 'નેમ',
            'હેલો', 'હાય', 'બાય', 'થેન્ક', 'યસ', 'નો', 'ઓકે'
        ]
    
    def listen(self):
        """
        Listen with English priority detection
        
        Returns:
            dict: {"text": "...", "language": "gu/en"}
        """
        with sr.Microphone() as source:
            print("🎤 બોલો... (Gujarati or English)")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                print("❌ Nothing heard")
                return {"text": None, "language": None}
        
        return self._recognize_with_priority(audio)
    
    def _recognize_with_priority(self, audio):
        """
        Recognize with ENGLISH FIRST priority
        
        Strategy:
        1. Try English API first
        2. If English result has real English words → USE IT
        3. Otherwise try Gujarati
        4. Smart detection for final decision
        """
        print("🔄 Processing...")
        
        english_result = None
        gujarati_result = None
        
        # STEP 1: Try ENGLISH first (priority)
        try:
            text_en = self.recognizer.recognize_google(audio, language="en-IN")
            if text_en and len(text_en.strip()) > 0:
                english_result = text_en.strip()
        except:
            pass
        
        # STEP 2: Try Gujarati
        try:
            text_gu = self.recognizer.recognize_google(audio, language="gu-IN")
            if text_gu and len(text_gu.strip()) > 0:
                gujarati_result = text_gu.strip()
        except:
            pass
        
        # No results
        if not english_result and not gujarati_result:
            print("❌ સમજાયું નહીં / Not understood")
            return {"text": None, "language": None}
        
        # DECISION LOGIC
        final_text, final_lang = self._smart_decision(english_result, gujarati_result)
        
        print(f"✅ [{final_lang.upper()}] {final_text}")
        return {"text": final_text, "language": final_lang}
    
    def _smart_decision(self, en_text, gu_text):
        """
        Smart decision with ENGLISH PRIORITY
        
        Args:
            en_text: English recognition result
            gu_text: Gujarati recognition result
            
        Returns:
            tuple: (final_text, final_language)
        """
        # CASE 1: Only English result
        if en_text and not gu_text:
            return en_text, 'en'
        
        # CASE 2: Only Gujarati result
        if gu_text and not en_text:
            # Check if it's transliterated English
            if self._is_transliterated_english(gu_text):
                # It's English spoken, but written in Gujarati script
                # Force to English (we'll handle translation)
                return gu_text, 'en'  # Mark as English even though text is Gujarati script
            # Real Gujarati
            return gu_text, 'gu'
        
        # CASE 3: Both results available
        # Check if English result has real English words
        if self._has_english_words(en_text):
            # English detected - USE ENGLISH
            return en_text, 'en'
        
        # Check if Gujarati has real Gujarati Unicode
        if self._has_gujarati_unicode(gu_text):
            # Real Gujarati - USE GUJARATI
            return gu_text, 'gu'
        
        # Check for transliteration in Gujarati result
        if self._is_transliterated_english(gu_text):
            # User spoke English, use English result
            if en_text:
                return en_text, 'en'
        
        # Default: Prefer English
        return en_text if en_text else gu_text, 'en' if en_text else 'gu'
    
    def _has_english_words(self, text):
        """Check if text contains real English words"""
        if not text:
            return False
        
        text_lower = text.lower()
        # Check for common English words
        return any(word in text_lower for word in self.english_indicators)
    
    def _has_gujarati_unicode(self, text):
        """Check if text has Gujarati Unicode characters"""
        if not text:
            return False
        
        gujarati_chars = set('અઆઇઈઉઊઋએઐઓઔકખગઘચછજઝઞટઠડઢણતથદધનપફબભમયરલવશષસહળક્ષજ્ઞ')
        
        # Count Gujarati characters
        gu_count = sum(1 for char in text if char in gujarati_chars)
        
        # If more than 30% Gujarati → Real Gujarati
        return len(text) > 0 and (gu_count / len(text)) > 0.3
    
    def _is_transliterated_english(self, text):
        """Check if Gujarati text is actually transliterated English"""
        if not text:
            return False
        
        # Check for transliteration patterns
        return any(pattern in text for pattern in self.transliteration_patterns)