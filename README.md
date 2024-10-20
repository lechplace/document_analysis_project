# Document Analysis Project

This project uses Python and Tesseract OCR to analyze images of documents in Polish, compare their content, and generate an Excel report showing whether the documents are duplicates or not.

## Requirements

1. Python 3.x
2. Tesseract OCR with Polish language support

### Installing Tesseract

#### Windows:

1. Download and install the Tesseract OCR from [this link](https://github.com/tesseract-ocr/tesseract/releases).
2. During installation, select additional language support, including Polish.
3. Add Tesseract to the system's PATH environment variable.
4. Verify installation by running `tesseract --version` in Command Prompt.

#### Linux (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-pol
```

#### MacOS:

```bash
brew install tesseract
brew install tesseract-lang
```

# How to Run the Project

1.  Place your document images in the images/ folder.

1.  Run the main script to process the images and generate the Excel report:

```bash
python main.py
```

1.  The output Excel file will be saved in the output/ folder, and it will contain information on whether the images are duplicates.

# How it Works

1.  Image Processing: The script reads images from the images/ folder and uses Tesseract to extract text from each image.
1.  Text Comparison: The extracted text is compared between images to detect whether any two documents are duplicates based on a similarity threshold.
1.  Excel Report: An Excel report is generated listing all analyzed images, indicating which ones are duplicates and the corresponding duplicate image.

# License

This project is licensed under the MIT License.
