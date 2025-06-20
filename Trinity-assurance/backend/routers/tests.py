from fastapi import APIRouter, HTTPException
from backend.models.schemas import TestGenerationRequest, TestGenerationResponse
from backend.services.test_generator import TestGenerator
import os

router = APIRouter()
generator = TestGenerator()  # OpenAI key from .env by default

@router.post("/generate", response_model=TestGenerationResponse)
async def generate_tests(request: TestGenerationRequest):
    try:
        test_code = generator.generate_tests_from_repo(
            repo_url=request.repo_url,
            language=request.language,
            file_path=request.file_path
        )
        return TestGenerationResponse(status="success", generated_test_code=test_code)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Test generation failed: {str(e)}")
