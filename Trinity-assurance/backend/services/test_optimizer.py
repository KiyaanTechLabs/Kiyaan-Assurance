# backend/services/test_optimizer.py

import os
import logging
from backend.utils.git_ops import get_changed_files

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class TestOptimizer:
    def __init__(self, repo_path: str, language: str):
        self.repo_path = repo_path
        self.language = language

    def get_relevant_tests(self, test_dir="tests/", src_dir="src/") -> list:
        """
        Determine which tests to run based on changed source files.
        """
        logger.info(f"[Trinity] Fetching changed files from repo: {self.repo_path}")
        changed_files = get_changed_files(self.repo_path)

        if not changed_files:
            logger.info("[Trinity] No changed files detected. Returning all tests.")
            return self._collect_all_tests(test_dir)

        relevant_tests = []

        for file in changed_files:
            if not file.endswith((".py", ".js", ".ts", ".java")):
                continue

            test_file_guess = self._map_source_to_test(file, test_dir, src_dir)
            if test_file_guess:
                relevant_tests.append(test_file_guess)

        logger.info(f"[Trinity] Selected optimized tests: {relevant_tests}")
        return relevant_tests if relevant_tests else self._collect_all_tests(test_dir)

    def _map_source_to_test(self, source_file: str, test_dir: str, src_dir: str) -> str:
        """
        Map a source file path to its likely test file.
        Example: src/foo/bar.py → tests/test_bar.py
        """
        file_name = os.path.basename(source_file)
        test_name = f"test_{file_name}" if self.language in ["python"] else file_name.replace(".js", ".test.js")

        test_path = os.path.join(test_dir, test_name)
        return test_path if os.path.exists(os.path.join(self.repo_path, test_path)) else None

    def _collect_all_tests(self, test_dir: str) -> list:
        """
        Return all tests in the directory if no optimization is possible.
        """
        test_path = os.path.join(self.repo_path, test_dir)
        return [
            os.path.join(test_dir, f)
            for f in os.listdir(test_path)
            if f.startswith("test_") or f.endswith(".test.js") or f.endswith("Test.java")
        ]
