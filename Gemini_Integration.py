from google import genai
from dotenv import load_dotenv
import os
from tqdm import tqdm

# Step 1: Load environment variables from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")  # Use the variable name here

# Step 2: Authenticate with the Gemini API
client = genai.Client(api_key=api_key)

# Base directory where image folders are stored
image_root_folder = "ai_powered_reader/images"

# Loop through each PDF subfolder (e.g., Food 1, Food 2...)
for folder in os.listdir(image_root_folder):
    folder_path = os.path.join(image_root_folder, folder)
    if os.path.isdir(folder_path):
        print(f"\n Processing folder: {folder}")

        # Loop through each image in the folder
        for image_file in tqdm(sorted(os.listdir(folder_path)), desc=f"Processing {folder}"):

            if image_file.endswith(".png") or image_file.endswith(".jpg"):
                image_path = os.path.join(folder_path, image_file)
                print(f" Sending image: {image_file}")

                # Upload image to Gemini
                uploaded_file = client.files.upload(file=image_path)

                # Send image to Gemini with a prompt
                response = client.models.generate_content(
                    model="gemini-2.0-flash-001",
                    contents=[
                        uploaded_file,
                         """Extract the text exactly as it appears visually in the image, preserving alignment and spacing.
                            Output it using markdown-style formatting with monospaced layout, as if it were printed text."""
                    ]
                )

                # Print the response
                print("\n Gemini Output:")
                print(response.text)

                # Save extracted text to .txt file
                output_text_path = image_path.replace(".png", ".txt")  # Change extension
                with open(output_text_path, "w", encoding="utf-8") as f:
                    f.write(response.text)
                print(f" Text saved to {output_text_path}")