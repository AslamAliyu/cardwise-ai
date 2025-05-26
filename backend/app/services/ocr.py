from paddleocr import PaddleOCR


ocr = PaddleOCR(use_textline_orientation=True, lang='en')  # Updated: no deprecated flag

# Initialize once (when app starts)
ocr_engine = PaddleOCR(use_textline_orientation=True, lang='en')

def extract_text(image_path: str) -> list[str]:
    result = ocr_engine.ocr(image_path)
    return result[0]['rec_texts'] if result else []


def extract_text_from_image(image_path: str) -> list[str]:
    result = ocr.predict(image_path)
    texts = result[0]['rec_texts']
    return texts
