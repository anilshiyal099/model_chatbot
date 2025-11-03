from pydantic import BaseModel, Field
from typing import Optional

class CodeRequest(BaseModel):
    """Request model for code analysis"""
    code: str = Field(..., description="Code to analyze for errors")
    language: Optional[str] = Field(
        default="python",
        description="Programming language of the code"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "code": "def hello()\n    print('Hello World')",
                "language": "python"
            }
        }

class CodeResponse(BaseModel):
    """Response model with analysis results"""
    original_code: str = Field(..., description="Original code submitted")
    has_error: bool = Field(..., description="Whether errors were found")
    error_explanation: Optional[str] = Field(
        None,
        description="Detailed explanation of errors found"
    )
    fixed_code: Optional[str] = Field(
        None,
        description="Corrected code in markdown format"
    )
    suggestions: Optional[str] = Field(
        None,
        description="Suggestions for improvement"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "original_code": "def hello()\n    print('Hello')",
                "has_error": True,
                "error_explanation": "Missing colon after function definition",
                "fixed_code": "```python\ndef hello():\n    print('Hello')\n```",
                "suggestions": "Always add colon after function definitions"
            }
        }