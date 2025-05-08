from google import genai
from dotenv import load_dotenv
import os

# Step 1: Load environment variables from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")  # ✅ Use the variable name here

# Step 2: Authenticate with the Gemini API
client = genai.Client(api_key=api_key)

# Step 3: Use the Gemini 2.0 Flash model
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents="Summarise the benefits of using AI in business."
)

# Step 4: Print the output
print("\nGemini Response:")
print(response.text)
