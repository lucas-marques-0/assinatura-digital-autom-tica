import fitz  
import cv2
from PIL import Image
import datetime

doc = fitz.open("modelo_contrato.pdf")  

def add_image_to_page(doc, page_num, image_path, x, y, width, height):
    page = doc[page_num]
    img = fitz.Pixmap(image_path)
    rect = fitz.Rect(x, y, x + width, y + height)
    page.insert_image(rect, pixmap=img)

rubrica_path = "rubrica.png" 
add_image_to_page(doc, 0, rubrica_path, 50, 700, 100, 50)
add_image_to_page(doc, 1, rubrica_path, 50, 700, 100, 50)

assinatura_path = "assinatura.png"  
add_image_to_page(doc, 2, assinatura_path, 100, 125, 100, 50)

page3 = doc[2]
date_str = datetime.datetime.now().strftime("%d/%m/%Y")
page3.insert_text((105, 115), date_str, fontsize=12, color=(0, 0, 0))

doc.save("contrato_assinado.pdf")
doc.close()
