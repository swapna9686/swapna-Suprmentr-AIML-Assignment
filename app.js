require("dotenv").config();
const axios = require("axios");

const API_KEY = process.env.API_KEY;

async function generateResponse(prompt) {
  try {

    const response = await axios.post(
      "https://api.groq.com/openai/v1/chat/completions",
      {
        model: "llama-3.3-70b-versatile",
        messages: [
          { role: "user", content: prompt }
        ]
      },
      {
        headers: {
          "Authorization": `Bearer ${API_KEY}`,
          "Content-Type": "application/json"
        }
      }
    );

    console.log("Response received ✅");
    console.log(response.data.choices[0].message.content);

  } catch (error) {
    console.error("Error ❌:");
    console.error(error.response?.data || error.message);
  }
}

generateResponse("You are a teacher, Explain APIs with a real life example");