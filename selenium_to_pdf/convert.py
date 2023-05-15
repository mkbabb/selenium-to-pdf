import base64
import json
from typing import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def send_devtools(driver: webdriver.Chrome, cmd: str, params: dict) -> dict:
    resource = f"/session/{driver.session_id}/chromium/send_command_and_get_result"
    url = driver.command_executor._url + resource
    body = json.dumps({"cmd": cmd, "params": params})

    response = driver.command_executor._request("POST", url, body)

    if "status" in response.keys():
        raise Exception(response["value"])
    else:
        return response["value"]


def html_to_pdf(
    url: str, print_options: dict | None = None, executable_path: str = "chromedriver"
) -> bytes:
    """Calls Selenium's DevTools API to print a page.

    Detailed print options can be found here: https://github.com/puppeteer/puppeteer/blob/main/docs/api.md#pagepdfoptions

    Modified from: https://stackoverflow.com/questions/47023842/selenium-chromedriver-printtopdf
    """
    if print_options is None:
        print_options = {}
    webdriver_options = Options()
    webdriver_options.add_argument("--headless")
    webdriver_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(
        executable_path=executable_path, options=webdriver_options
    )
    driver.get(url)

    print_options = {
        "landscape": False,
        "displayHeaderFooter": False,
        "printBackground": True,
        "preferCSSPageSize": True,
        **print_options,
    }
    cmd = "Page.printToPDF"
    result = send_devtools(driver, cmd, print_options)
    driver.quit()

    return base64.b64decode(result["data"])
