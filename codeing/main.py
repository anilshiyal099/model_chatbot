from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
import uvicorn

app = FastAPI(
    title="Error Solving Chatbot API",
    description="AI-powered code error detection and fixing",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)

@app.get("/")
async def root():
    return {
        "message": "Error Solving Chatbot API",
        "version": "1.0.0",
        "endpoints": {
            "/solve-error": "POST - Submit code for error analysis",
            "/health": "GET - Check API health"
        }
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
    
    
    
    
    
    
    
# {
#   "original_code": "...",
#   "has_error": true/false,
#   "error_explanation": "Markdown formatted analysis",
#   "fixed_code": "```language\ncode here\n```",
#   "suggestions": "Markdown formatted suggestions"
# }