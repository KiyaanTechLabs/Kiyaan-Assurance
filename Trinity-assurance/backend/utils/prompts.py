# backend/utils/prompts.py

TEST_GEN_PROMPT_TEMPLATE = """
YYou are a senior QA engineer with deep expertise in automated testing. Your task is to generate robust, production-level unit or integration tests for the following code changes written in {language}.

========================
CODE DIFF:
{diff}
========================

Instructions:
1. Identify the functions/classes that were modified or added.
2. Write relevant test cases that verify correctness, edge cases, error handling, and expected outputs.
3. Use the standard test framework for {language} (e.g., PyTest for Python, JUnit/TestNG for Java, Jest for JS).
4. Include appropriate imports.
5. Do NOT describe — just return the complete test file content only.
6. The file must be ready to run, without needing user modifications.

Output Format:
Return a complete single test file as plain code. No markdown, no descriptions.

Be concise, intelligent, and professional.
"""
