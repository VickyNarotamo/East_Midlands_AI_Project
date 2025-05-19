# East_Midlands_AI_Project
A student-led consultancy project developed by a team of four using Python and Gemini AI to extract and summarize data from scanned PDFs for the East Midlands Chamber. Created as part of De Montfort University’s Lead and Inspire programme.

This project extracts readable text from receipt PDFs using Google's Gemini 2.0 Flash model.

What it does:
- Converts PDF receipts into images
- Sends each image to the Gemini AI API
- Extracts and saves text in `.txt` files with accurate receipt layout

Technologies Used
- Python 3.11+
- [official Google Gen AI SDK for Python.](https://github.com/googleapis/python-genai)
- pdf2image
- Pillow
- python-dotenv
- tqdm (for progress bar)

Setup Instructions
1. **Install dependencies:**

```bash
pip install git+https://github.com/googleapis/python-genai.git
pip install python-dotenv pdf2image pillow tqdm
```

2. **Install Poppler for Windows**

Poppler is required for converting PDFs to images using `pdf2image`.

- Download Poppler from the official release page:  
  [https://github.com/oschwartz10612/poppler-windows/releases](https://github.com/oschwartz10612/poppler-windows/releases)

- Extract the ZIP file to:  
  `C:\poppler`

- Add the `bin` folder to your system's PATH:

  1. Open **System Properties** → Environment Variables  
  2. Under **System variables**, select `Path` and click **Edit**  
  3. Click **New** and add:  
     ```
     C:\poppler\bin
     ```
  4. Click **OK** on all windows to apply

You can verify installation by running this command in your terminal:

```bash
pdftoppm -h
```
---
3. **Create a `.env` file for your API key**

In the root of your project (same location as your Python scripts), create a file named `.env` and add this line:

GOOGLE_API_KEY=your_actual_api_key_here

This keeps your API key private and secure. Do **not** hardcode the key in your Python files.

---
4. **Convert all receipt PDFs to images**

Run the following script to convert each `.pdf` into `.png` images using `pdf2image`:

```bash
python convert_all_pdfs.py
```
---
5. Run the Gemini integration script

This script uploads each .png image to the Gemini 2.0 Flash model and saves the extracted text in matching .txt files.

```bash
python Gemini_Integration.py
```

If everything is set up correctly, you'll see logs like:

Sending image: page_1.png

Gemini Output:
... (extracted text here)

Text saved to ai_powered_reader/images/Food 1/page_1.txt

