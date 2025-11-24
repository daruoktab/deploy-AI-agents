
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import run_agent
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Utility Agent API",
    description="An intelligent agent with various utility tools powered by GPT-4 and LangGraph",
    version="1.0.0"
)

# Add CORS middleware for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

# Request model
class AgentRequest(BaseModel):
    """Request model for agent invocation."""
    prompt: str

    class Config:
        json_schema_extra = {
            "example": {
                "prompt": "Calculate 25 * 48 + sqrt(144)"
            }
        }


# Response model
class AgentResponse(BaseModel):
    """Response model for agent invocation."""
    response: str
    

@app.get("/")
async def home(request: Request):
    """Serve the main HTML interface."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy", "service": "AI Utility Agent"}


@app.post("/agent", response_model=AgentResponse)
async def invoke_agent(request: AgentRequest):
    """
    Invoke the AI agent with a prompt.
    
    The agent can perform various utility tasks:
    - Mathematical calculations
    - Text analysis
    - JSON formatting
    - Date/time queries
    - Case conversions
    
    Args:
        request: AgentRequest with prompt field
        
    Returns:
        AgentResponse with the agent's response
        
    Raises:
        HTTPException: If the prompt is empty or agent execution fails
    """
    try:
        # Validate prompt
        if not request.prompt.strip():
            raise HTTPException(status_code=400, detail="Prompt cannot be empty")
        
        logger.info(f"Processing request: {request.prompt[:100]}...")
        
        # Run the agent with the user's prompt
        result = run_agent(request.prompt)
        
        logger.info("Request processed successfully")
        
        return AgentResponse(response=result)
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error invoking agent: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred while processing your request. Please try again."
        )
