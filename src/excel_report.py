import pandas as pd

def create_excel_report(data, output_file):
    """Funkcja tworząca raport w formacie Excel na podstawie wyników analizy"""
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
