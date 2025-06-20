// frontend/src/App.jsx

import React from "react";
import { Container, Typography, Button, Box } from "@mui/material";
import TestGenerator from "./components/TestGenerator"; // 👈 Import your core module

function App() {
  return (
    <Container maxWidth="md" sx={{ mt: 8 }}>
      {/* Header Section */}
      <Box textAlign="center">
        <Typography variant="h3" gutterBottom>
          🧠 Trinity QA Autopilot
        </Typography>
        <Typography variant="h6" color="text.secondary" gutterBottom>
          AI-driven Testing | Healing | CI Debugging | Security | Licensing
        </Typography>
        <Button variant="contained" color="primary" size="large" sx={{ mb: 4 }}>
          Start Trinity
        </Button>
      </Box>

      {/* Test Generator Brain */}
      <TestGenerator />
    </Container>
  );
}

export default App;
