from fastapi import APIRouter, HTTPException
from models import CodeRequest, CodeResponse
from services import CodeAnalyzerService

router = APIRouter()
analyzer_service = CodeAnalyzerService()

@router.post("/solve-error", response_model=CodeResponse)
async def solve_error(request: CodeRequest):
    """
    Analyze code for errors and provide fixes
    
    Args:
        request: CodeRequest object containing code and language
        
    Returns:
        CodeResponse with analysis results
    """
    try:
        result = await analyzer_service.analyze_code(
            code=request.code,
            language=request.language
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing request: {str(e)}"
        )

@router.get("/health")
async def health_check():
    """Check API health status"""
    return {
        "status": "healthy",
        "service": "Error Solving Chatbot",
        "version": "1.0.0"
    }