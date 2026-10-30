#pacotes
#instalar e importar pacotes externos

#importando o pacote para ser usado
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", style="B", size=16)
for i in range(3):
    texto = input("Digite uma palavra: ")
    pdf.cell(40+i*5, 10+i*5, texto)

pdf.output("tuto1.pdf")
