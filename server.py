const express = require('express');
const axios = require('axios');
const app = express();

app.use(express.json());

app.post('/api/generate-ai-app-idea', async (req, res) => {
  try {
    const response = await axios.post('https://api.anthropic.com/v1/chat/completions', {
      model: "claude-3-5-sonnet-20240620",
      messages: [
        {
          role: "user",
          content: "Generate a unique and innovative AI app idea. Describe it in one or two sentences."
        }
      ],
      max_tokens: 150
    }, {
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': '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'
      }
    });

    const idea = response.data.choices[0].message.content;
    res.json({ idea });
  } catch (error) {
    console.error('Error calling Claude API:', error);
    res.status(500).json({ error: 'An error occurred while generating the idea' });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
