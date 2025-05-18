import os
from pdf2image import convert_from_path

# Folder paths
pdf_folder = "ai_powered_reader"
output_folder = "ai_powered_reader/images"
os.makedirs(output_folder, exist_ok=True)

# Loop through all PDFs in the folder
for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        images = convert_from_path(pdf_path)

        # Use filename (without extension) to create a unique subfolder
        base_name = os.path.splitext(filename)[0]
        pdf_output_folder = os.path.join(output_folder, base_name)
        os.makedirs(pdf_output_folder, exist_ok=True)

        for i, image in enumerate(images):
            image_path = os.path.join(pdf_output_folder, f"page_{i+1}.png")
            image.save(image_path, "PNG")
            print(f" Saved {image_path}")
