# selenium-to-pdf

Given an HTML document, converts thereupon to a PDF using Selenium's DevTools.

Requires selenium and ChromeDriver. For more information on how to install ChromeDriver,
see [here](https://sites.google.com/a/chromium.org/chromedriver/getting-started).

## Example

```python
from selenium_to_pdf import convert

url = "https://www.fulltextarchive.com/book/dante-s-inferno/#CANTO-1-2"

pdf_data = convert.html_to_pdf(url=url)

with open("dante.pdf", "wb") as f:
    f.write(pdf_data)
```
