from PyPDF2 import PdfFileWriter, PdfFileReader
import io

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Roboto', 'Roboto-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Robotomono', 'RobotoMono-Medium.ttf'))
packet = io.BytesIO()

# create a new PDF with Reportlab
def creatpdf(name, event):
    mid = 559

    end = 841
    size =13
    can = canvas.Canvas(packet )
    namesize =(len(name)/2)*size
    can.setFont('Roboto', 20)
    can.drawString(mid-namesize, 300, name)
    can.setFont('Roboto', 20)
    can.drawString(245, 210, event)
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("document.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page2 = new_pdf.getPage(0)
    page.mergePage(page2)
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("certificate.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

if __name__=="__main__":
    creatpdf("SAHIL","MAKE-A-TON")