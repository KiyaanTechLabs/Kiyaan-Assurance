// frontend/src/components/TestGenerator.jsx

import React, { useState, useRef, useEffect } from "react";
import {
  TextField,
  Button,
  Typography,
  CircularProgress,
  Box,
  Paper,
  MenuItem,
} from "@mui/material";
import axios from "axios";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

const TestGenerator = () => {
  const [repoUrl, setRepoUrl] = useState("");
  const [language, setLanguage] = useState("python");
  const [filePath, setFilePath] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const resultRef = useRef();

  useEffect(() => {
    if (result) {
      resultRef.current?.scrollIntoView({ behavior: "smooth" });
    }
  }, [result]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await axios.post("http://localhost:8000/api/tests/generate", {
        repo_url: repoUrl,
        language: language,
        file_path: filePath,
      });
      setResult(response.data.generated_test_code);
    } catch (err) {
      setError(err.response?.data?.detail || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Paper elevation={3} sx={{ p: 4, mt: 4 }}>
      <Typography variant="h5" gutterBottom>
        ⚙️ Generate AI Test Cases
      </Typography>
      <Box
        component="form"
        onSubmit={handleSubmit}
        sx={{ display: "flex", flexDirection: "column", gap: 2 }}
      >
        <TextField
          label="Repository URL"
          value={repoUrl}
          onChange={(e) => setRepoUrl(e.target.value)}
          required
          fullWidth
        />
        <TextField
          select
          label="Language"
          value={language}
          onChange={(e) => setLanguage(e.target.value)}
          fullWidth
        >
          <MenuItem value="python">Python</MenuItem>
          <MenuItem value="java">Java</MenuItem>
        </TextField>
        <TextField
          label="File Path (Optional)"
          value={filePath}
          onChange={(e) => setFilePath(e.target.value)}
          placeholder="e.g. src/utils/helper.py"
          fullWidth
        />
        <Button
          type="submit"
          variant="contained"
          color="secondary"
          disabled={loading}
        >
          {loading ? <CircularProgress size={24} /> : "Generate"}
        </Button>
      </Box>

      {error && (
        <Typography color="error" sx={{ mt: 2 }}>
          {error}
        </Typography>
      )}

      {result && (
        <Box sx={{ mt: 4 }} ref={resultRef}>
          <Typography variant="h6">🧪 Generated Test Code:</Typography>
          <SyntaxHighlighter
            language={language}
            style={oneDark}
            wrapLongLines
            customStyle={{ borderRadius: "8px", padding: "1rem" }}
          >
            {result}
          </SyntaxHighlighter>
        </Box>
      )}
    </Paper>
  );
};

export default TestGenerator;
