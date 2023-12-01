from pypdf import PdfMerger

pdfs = []

for i in range(1, 11):
    pdfs.append(f'{i}.pdf')

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
