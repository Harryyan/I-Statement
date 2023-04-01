import tabula
from tabula import convert_into
from PyPDF2 import PdfReader
import pandas as pd
import re
import json
import os

regex = "[+-]?[0-9]+\.[0-9]+"
# Define a function to
# check Floating point number
def check(floatnum):
    # pass the regular expression
    # and the string in search() method
    if re.search(regex, floatnum):
        return True
    else:
        return False


# Read pdf into list of DataFrame
filename = "pdf_reader/statement.pdf"
df = tabula.read_pdf(filename, pages="all")
pdf = PdfReader(open(filename, "rb"))
pages = len(pdf.pages)
test_area = [388, 59, 638, 567]
test_area1 = [130, 59, 721, 567]

df = pd.DataFrame()
line = []

for pageiter in range(pages):
    if pageiter == 0:
        df = tabula.read_pdf(filename, pages=pageiter + 1, area=test_area, stream=True)
    else:
        df = tabula.read_pdf(
            filename, pages=pageiter + 1, area=test_area1, guess=True, stream=True
        )

    for item in df[0].values:
        a = ",".join(map(str, item))
        b = a.replace("nan,", "")
        c = b.replace(",nan", "")
        count = len(c.split(","))

        print(c)
        if count > 3:
            if re.search("[0-9]+", c.split(",")[0]) and check(c.split(",")[-1]):
                d = c.split(",")[0]
                if len(c) > 2:
                    e = d.split(" ")
                    f = str(e[0]) + " " + e[1]
                    line.append(
                        {
                            "date": f,
                            "location": c.split(",")[2],
                            "price": c.split(",")[-1],
                        }
                    )
                else:
                    line.append(
                        {
                            "date": d,
                            "location": c.split(",")[2],
                            "price": c.split(",")[-1],
                        }
                    )
        else:
            a = c.split(",")[0]
            b = a.split(" ")

            if re.search("[0-9]+", str(b[0])) and check(c.split(",")[-1]):
                line.append(
                    {
                        "date": str(b[0]) + " " + b[1],
                        "location": " ".join(b[4:]),
                        "price": c.split(",")[-1],
                    }
                )
result = {"data": line}
print(json.dumps(result))
