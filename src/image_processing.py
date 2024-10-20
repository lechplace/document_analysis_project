import pytesseract
import cv2

def extract_text_from_image(image_path):
    """Funkcja ekstrakcji tekstu z obrazu za pomocą Tesseract OCR"""
    # Wczytanie obrazu
    img = cv2.imread(image_path)
    
    # Konwersja obrazu na odcienie szarości dla lepszej jakości OCR
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Ekstrakcja tekstu z obrazu z ustawieniem języka na polski
    text = pytesseract.image_to_string(gray, lang='pol')
    
    return text
