import os
import pandas as pd
from src.image_processing import extract_text_from_image
from src.text_comparison import check_for_duplicates
from src.excel_report import create_excel_report

def main(image_dir, output_file):
    
    # Zbieranie ścieżek do wszystkich obrazów w katalogu
    image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        print("Brak plików do analizy.")
        return
    
    # Przechowywanie wyników analizy
    results = []
    
    # Przetwarzanie każdego obrazu
    extracted_texts = {}
    for image_path in image_files:
        print(f"Przetwarzanie obrazu: {image_path}")
        text = extract_text_from_image(image_path)
        extracted_texts[image_path] = text
    
    # Porównanie każdego obrazu z pozostałymi w celu sprawdzenia, czy są duplikatami
    for i, (image_path_1, text_1) in enumerate(extracted_texts.items()):
        duplicate_found = False
        duplicate_image = None
        for j, (image_path_2, text_2) in enumerate(extracted_texts.items()):
            if i != j and check_for_duplicates(text_1, text_2):
                duplicate_found = True
                duplicate_image = image_path_2
                break
        
        results.append({
            'Image': os.path.basename(image_path_1),
            'Is Duplicate': duplicate_found,
            'Duplicate Of': os.path.basename(duplicate_image) if duplicate_image else None
        })
    
    # Tworzenie raportu w Excelu
    create_excel_report(results, output_file)
    print(f"Raport został zapisany w: {output_file}")

if __name__ == "__main__":
    main(image_dir='images', output_file='output/duplicates_report.xlsx')
