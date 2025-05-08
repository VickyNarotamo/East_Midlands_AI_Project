from google import genai

# Step 1: Authenticate the Gemini client with your API key
client = genai.Client(api_key='AIzaSyBLR73JCyQDl1NNPcCm1Tqbsgydtxw9wIY')

# Step 2: Generate content using the Gemini 2.0 Flash model
# This sends a prompt to the model and gets a generated response
response = client.models.generate_content(
    model='gemini-2.0-flash-001',  # Use the Gemini 2.0 Flash model variant
    contents='Summarise the benefits of using AI in business.'
)

# Step 3: Output the model's response
print("\nGemini Response:")
print(response.text)  # Display the generated text
