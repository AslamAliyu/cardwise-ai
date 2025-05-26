from paddleocr import PaddleOCR
import os

# Correct image path
image_path = os.path.join(os.path.dirname(__file__), 'receipt1.png')

# Recommended init config
ocr = PaddleOCR(use_textline_orientation=True, lang='en')

# Run OCR (no `cls=True`)
results = ocr.ocr(image_path)

# ✅ Extract and print recognized text
print("\n✅ Extracted Text:")
for text in results[0]['rec_texts']:
    print(text)
