import sys
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os
import io

class Pdf2Text:
    
    def __init__(self, pdf):
        """
        pdf selected
        """
        self.pdf = pdf
    
    def convert2text(self):
        pages = convert_from_path(self.pdf, 500)
        text = ""
        page_count = 1
        for page in pages:
            temp = io.BytesIO()
            page.save(temp, 'JPEG')
            text += str(((pytesseract.image_to_string(Image.open(temp), lang="kan+eng"))))
            print("page %d completed."%page_count)
            page_count += 1
        
        with open("OCR_output.txt", "w") as f:
            f.write(text)
            
        print("file saved!")
        
    def main(self):
        if os.path.isfile(self.pdf):
            self.convert2text()
        else:
            print("pdf file does not exist")
if __name__ == "__main__":
    file = sys.argv[1]
    convert_file = Pdf2Text(file)
    convert_file.main()
