import PyPDF2


def extract_pdf(path: str, page: int):
    page -= 1
    # creating a pdf file object
    pdfFileObj = open(path, 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # creating a page object
    pageObj = pdfReader.getPage(page)
    # extracting text from page
    text = pageObj.extractText()
    # closing the pdf file object
    pdfFileObj.close()
    return text
