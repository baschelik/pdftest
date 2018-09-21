# -*- coding: utf-8 -*-

import PyPDF2   # need to install first pip3 install PyPDF2


class Pdf2Text(object):

    def __init__(self, path):
        self.path = path

    def extract_text_from_page(self, file, page_num):
        page = file.getPage(page_num)
        return str(page.extractText())

    def get_file_and_read(self):
        pdf_file = open(self.path, 'rb')
        return PyPDF2.PdfFileReader(pdf_file)