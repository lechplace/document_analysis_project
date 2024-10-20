from difflib import SequenceMatcher

def check_for_duplicates(text1, text2, threshold=0.9):
    """Funkcja sprawdzająca, czy dwa fragmenty tekstu są wystarczająco podobne, aby uznać je za duplikaty"""
    similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
    return similarity_ratio >= threshold
