import PyPDF2


def extract_pdf(path: str, page: int):
    page -= 1
    count = 0
    data = ''
    pdfFileObj = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page + i)
        text = pageObj.extractText() + '\n'
        data += text
        count += 1
        if count == 5:
            pdfFileObj.close()
            return data
