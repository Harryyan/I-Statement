import tabula
import pandas as pd
import re
import json

from tabula import convert_into
from PyPDF2 import PdfFileReader


class PDFAnalyzer:
    def check(self, floatnum):
        regex = "[+-]?[0-9]+\.[0-9]+"
        if re.search(regex, floatnum):
            return True
        else:
            return False

    def __init__(self, filename):
        self.filename = filename
        self.pdf = PdfFileReader(open(filename, "rb"))
        self.pages = pdf.getNumPages()
        self.firstPageArea = [388, 59, 638, 567]
        self.otherPageArea = [130, 59, 721, 567]

    def scan():
        df = pd.DataFrame()
        line = []
