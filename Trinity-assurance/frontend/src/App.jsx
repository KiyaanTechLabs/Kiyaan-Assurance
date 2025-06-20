import React from "react";
import { Container, Typography, Button, Box } from "@mui/material";

function App() {
  return (
    <Container maxWidth="md" sx={{ mt: 8 }}>
      <Box textAlign="center">
        <Typography variant="h3" gutterBottom>
          🧠 Trinity QA Autopilot
        </Typography>
        <Typography variant="h6" color="text.secondary" gutterBottom>
          AI-driven Testing | Healing | CI Debugging | Security | Licensing
        </Typography>
        <Button variant="contained" color="primary" size="large">
          Start Trinity
        </Button>
      </Box>
    </Container>
  );
}

export default App;
