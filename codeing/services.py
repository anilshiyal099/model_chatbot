# from groq import Groq
# from character import CHARACTER_PROMPT
# from config import settings
# from models import CodeResponse
# import re

# class CodeAnalyzerService:
#     """Service for analyzing and fixing code using Groq AI"""
    
#     def __init__(self):
#         self.client = Groq(api_key=settings.GROQ_API_KEY)
#         self.model = settings.GROQ_MODEL
#         self.temperature = settings.TEMPERATURE
#         self.max_tokens = settings.MAX_TOKENS
    
#     async def analyze_code(self, code: str, language: str) -> CodeResponse:
#         """
#         Analyze code for errors and provide fixes
        
#         Args:
#             code: Code to analyze
#             language: Programming language
            
#         Returns:
#             CodeResponse with analysis results
#         """
#         # Create user prompt
#         user_prompt = self._create_prompt(code, language)
        
#         # Get AI response
#         response_text = await self._get_ai_response(user_prompt)
        
#         # Parse response
#         return self._parse_response(code, response_text, language)
    
#     def _create_prompt(self, code: str, language: str) -> str:
#         """Create prompt for AI"""
#         return f"""
# Please analyze this {language} code for errors:
# ```{language}
# {code}
# ```

# Follow these steps:
# 1. Check if there are any syntax or logical errors
# 2. If errors exist, explain them clearly in simple terms
# 3. Provide the fixed code in markdown format
# 4. Give practical suggestions for improvement

# Respond in this exact format:
# ERROR_STATUS: [YES/NO]
# ERROR_EXPLANATION: [Your explanation or "No errors found"]
# FIXED_CODE:
# ```{language}
# [Fixed code here or original code if no errors]
# ```
# SUGGESTIONS: [Your suggestions]
# """
    
#     async def _get_ai_response(self, user_prompt: str) -> str:
#         """Get response from Groq AI"""
#         chat_completion = self.client.chat.completions.create(
#             messages=[
#                 {"role": "system", "content": CHARACTER_PROMPT},
#                 {"role": "user", "content": user_prompt}
#             ],
#             model=self.model,
#             temperature=self.temperature,
#             max_tokens=self.max_tokens,
#         )
#         return chat_completion.choices[0].message.content
    
#     def _parse_response(self, original_code: str, response_text: str, language: str) -> CodeResponse:
#         """Parse AI response into structured format"""
#         # Check error status
#         has_error = "ERROR_STATUS: YES" in response_text
        
#         # Extract error explanation
#         error_explanation = self._extract_section(
#             response_text,
#             "ERROR_EXPLANATION:",
#             "FIXED_CODE:"
#         )
        
#         # Extract fixed code
#         fixed_code = self._extract_code_block(response_text, language)
        
#         # Extract suggestions
#         suggestions = self._extract_section(
#             response_text,
#             "SUGGESTIONS:",
#             None
#         )
        
#         return CodeResponse(
#             original_code=original_code,
#             has_error=has_error,
#             error_explanation=error_explanation if has_error else "No errors found. Code looks good!",
#             fixed_code=fixed_code if fixed_code else f"```{language}\n{original_code}\n```",
#             suggestions=suggestions if suggestions else "Keep up the good work!"
#         )
    
#     def _extract_section(self, text: str, start_marker: str, end_marker: str = None) -> str:
#         """Extract text between markers"""
#         if start_marker not in text:
#             return None
        
#         start_idx = text.find(start_marker) + len(start_marker)
        
#         if end_marker:
#             end_idx = text.find(end_marker, start_idx)
#             if end_idx == -1:
#                 end_idx = len(text)
#         else:
#             end_idx = len(text)
        
#         return text[start_idx:end_idx].strip()
    
#     def _extract_code_block(self, text: str, language: str) -> str:
#         """Extract code block in markdown format"""
#         # Find code block
#         pattern = f"```{language}.*?```"
#         match = re.search(pattern, text, re.DOTALL)
        
#         if match:
#             return match.group(0).strip()
        
#         # Fallback: find any code block
#         pattern = "```.*?```"
#         match = re.search(pattern, text, re.DOTALL)
        
#         if match:
#             return match.group(0).strip()
        
#         return None













from groq import Groq
from character import CHARACTER_PROMPT
from config import settings
from models import CodeResponse
import re

class CodeAnalyzerService:
    """Service for analyzing and fixing code using Groq AI"""
    
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
        self.model = settings.GROQ_MODEL
        self.temperature = settings.TEMPERATURE
        self.max_tokens = settings.MAX_TOKENS
    
    async def analyze_code(self, code: str, language: str) -> CodeResponse:
        """
        Analyze code for errors and provide fixes
        
        Args:
            code: Code to analyze
            language: Programming language
            
        Returns:
            CodeResponse with analysis results
        """
        # Create user prompt
        user_prompt = self._create_prompt(code, language)
        
        # Get AI response
        response_text = await self._get_ai_response(user_prompt)
        
        # Parse response
        return self._parse_response(code, response_text, language)
    
    def _create_prompt(self, code: str, language: str) -> str:
        """Create prompt for AI"""
        return f"""Please analyze this {language} code and provide a comprehensive analysis:
```{language}
{code}
```

Follow the response structure defined in your character prompt. Provide:
1. Language detection confirmation
2. Error analysis (if errors exist)
3. Clear explanations in simple terms
4. Fixed code (only if errors found)
5. Suggestions for improvement

Use proper Markdown formatting with emojis and clear sections."""
    
    async def _get_ai_response(self, user_prompt: str) -> str:
        """Get response from Groq AI"""
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": CHARACTER_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        return chat_completion.choices[0].message.content
    
    def _parse_response(self, original_code: str, response_text: str, language: str) -> CodeResponse:
        """Parse AI response into structured format"""
        
        # Check if errors were found
        has_error = any(keyword in response_text.lower() for keyword in 
                       ['error', 'mistake', 'incorrect', 'fix', 'corrected solution'])
        
        # If "no errors" or "correct" is mentioned, it's likely correct code
        if any(phrase in response_text.lower() for phrase in 
               ['no errors', 'code is correct', 'looks good', 'working correctly']):
            has_error = False
        
        # Extract sections from markdown response
        error_explanation = self._extract_explanation_section(response_text)
        fixed_code = self._extract_code_blocks(response_text, language)
        suggestions = self._extract_suggestions_section(response_text)
        
        # If no fixed code found, use original
        if not fixed_code:
            fixed_code = f"```{language}\n{original_code}\n```"
        
        # Create default messages if sections not found
        if not error_explanation:
            error_explanation = "Analysis completed. Check the detailed response below."
        
        if not suggestions:
            suggestions = "Keep up the good work! Continue following best practices."
        
        return CodeResponse(
            original_code=original_code,
            has_error=has_error,
            error_explanation=error_explanation,
            fixed_code=fixed_code,
            suggestions=suggestions
        )
    
    def _extract_explanation_section(self, text: str) -> str:
        """Extract error explanation or analysis section"""
        patterns = [
            r'## .*?(?:Error Analysis|Analysis|Explanation).*?\n(.*?)(?=\n##|\n```|$)',
            r'### .*?(?:Explanation|Analysis).*?\n(.*?)(?=\n##|###|\n```|$)',
            r'\*\*.*?(?:Error|Analysis).*?\*\*\n(.*?)(?=\n\*\*|\n```|$)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        # Fallback: return first major paragraph
        paragraphs = text.split('\n\n')
        for para in paragraphs:
            if len(para) > 50 and not para.startswith('```'):
                return para.strip()
        
        return text[:500]  # Return first 500 chars as fallback
    
    def _extract_code_blocks(self, text: str, language: str) -> str:
        """Extract code blocks from markdown response"""
        # Try to find code block with language
        pattern = f"```{language}(.*?)```"
        match = re.search(pattern, text, re.DOTALL)
        
        if match:
            code = match.group(1).strip()
            return f"```{language}\n{code}\n```"
        
        # Try any code block
        pattern = r"```(\w*)\n(.*?)```"
        matches = re.findall(pattern, text, re.DOTALL)
        
        if matches:
            # Return the last code block (likely the fixed version)
            lang, code = matches[-1]
            return f"```{lang if lang else language}\n{code.strip()}\n```"
        
        return None
    
    def _extract_suggestions_section(self, text: str) -> str:
        """Extract suggestions or improvements section"""
        patterns = [
            r'## .*?(?:Suggestions|Improvements|Enhancements).*?\n(.*?)(?=\n##|$)',
            r'### .*?(?:Suggestions|Improvements).*?\n(.*?)(?=\n##|###|$)',
            r'🚀.*?\n(.*?)(?=\n\*\*|##|$)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return None