from pdfminer.high_level import extract_text,extract_pages
from pdfminer.layout import LTTextContainer 
from pikepdf import Pdf
import os

pdf = Pdf.new()

# Como combinar 2(ou mais) PDFs em um
caminho_absoluto = 'O:\Clientes\Kuchak\Dpto Pessoal\\2023\\2031 MATRIZ\\012023\RESCISÕES\ANELISE TOEBE\\'
for arquivo_pdf in os.listdir(caminho_absoluto):
    arquivo_pdf = caminho_absoluto + os.sep + arquivo_pdf
    # for page_layout in extract_pages(arquivo_pdf):
    #     for element in page_layout:
    #         if isinstance(element,LTTextContainer):
    #             if '92.607.571/0001-07' in element.get_text():
    arquivo_juntar = Pdf.open(arquivo_pdf)
    pdf.pages.extend(arquivo_juntar.pages)
    pdf.save(caminho_absoluto + os.sep + 'RESCISAO.pdf')
    arquivo_juntar.close()
    pdf.close()
    print(arquivo_pdf)
    try:
        os.remove(arquivo_pdf)
    except:
        pass
                    
                    # print(arquivo_pdf)
                    # os.remove(arquivo_pdf)
# fonte1.close()
# fonte2.close()
# pdf.close(