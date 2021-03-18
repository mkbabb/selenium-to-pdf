from selenium_to_pdf import html_to_pdf

path = "https://www.gutenberg.org/files/1001/1001-h/1001-h.htm#CantoV"

pdf = html_to_pdf(path)

with open("tests/canto-5.pdf", "wb") as file:
    file.write(pdf)