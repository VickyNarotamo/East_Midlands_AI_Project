import os
from pdf2image import convert_from_path

# Folder where your input PDFs are stored
pdf_folder = "ai_powered_reader"

# Folder where images will be saved
output_root = os.path.join(pdf_folder, "images")

# Ensure output root exists
os.makedirs(output_root, exist_ok=True)

# Loop through all PDF files
for pdf_file in sorted(os.listdir(pdf_folder)):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, pdf_file)

        # Create a folder based on the PDF name (e.g., "Food 1")
        folder_name = os.path.splitext(pdf_file)[0]  # removes ".pdf"
        output_folder = os.path.join(output_root, folder_name)
        os.makedirs(output_folder, exist_ok=True)

        # Convert PDF to images
        images = convert_from_path(pdf_path)

        # Save each image
        for i, image in enumerate(images):
            image_path = os.path.join(output_folder, f"page_{i + 1}.png")
            image.save(image_path, format="PNG")
            print(f" Saved {image_path}")
