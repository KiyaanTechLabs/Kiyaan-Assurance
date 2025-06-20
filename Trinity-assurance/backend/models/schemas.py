from pydantic import BaseModel
from typing import Optional

# Request model: input to test generation
class TestGenerationRequest(BaseModel):
    repo_url: str
    language: str
    file_path: Optional[str] = ""  # Optional: Specific file or leave blank for full repo

# Response model: output from AI test generator
class TestGenerationResponse(BaseModel):
    status: str  # Example: "success" or "error"
    generated_test_code: str  # AI-generated test code as a string
