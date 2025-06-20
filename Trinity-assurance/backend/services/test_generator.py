import os
import re
import logging
from backend.utils.git_ops import get_repo_diff, clone_or_pull_repo
from backend.utils.prompts import TEST_GEN_PROMPT_TEMPLATE
from groq import Groq  # ✅ Switched from openai to groq

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class TestGenerator:
    def __init__(self, api_key=None, model="llama3-8b-8192"):  # ✅ Default to LLaMA 3
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.model = model
        self.client = Groq(api_key=self.api_key)

    def sanitize_filename(self, name):
        """Remove unsafe characters from filename"""
        return re.sub(r'[^a-zA-Z0-9_\-]', '_', name)

    def generate_tests_from_repo(self, repo_url: str, language: str, file_path: str = "") -> str:
        """Main method to generate tests from the repo and return the generated code as a string."""

        logger.info(f"[Trinity] Cloning repo: {repo_url}")
        repo_path = clone_or_pull_repo(repo_url)

        logger.info(f"[Trinity] Getting git diff for latest commit")
        diff_output = get_repo_diff(repo_path, file_path)

        if not diff_output:
            return "No significant code changes detected. Test generation skipped."

        prompt = TEST_GEN_PROMPT_TEMPLATE.format(
            language=language,
            diff=diff_output,
        )

        logger.info("[Trinity] Sending prompt to Groq for test generation...")
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=1000
            )
            test_code = response.choices[0].message.content
            logger.info("[Trinity] Test code successfully generated.")

            # Save test file
            os.makedirs("tests", exist_ok=True)
            safe_name = self.sanitize_filename(file_path or repo_url.split("/")[-1])
            test_file_name = f"test_{safe_name}.py"
            test_file_path = os.path.join("tests", test_file_name)

            with open(test_file_path, "w") as f:
                f.write(test_code.strip())

            logger.info(f"[Trinity] Test code saved to: {test_file_path}")

            return test_code.strip()

        except Exception as e:
            logger.error(f"Error while generating test: {e}")
            return "Error while generating test."
