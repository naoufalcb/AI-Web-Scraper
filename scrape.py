from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


load_dotenv()  # Ensure your .env file has SBR_WEBDRIVER defined

# importing the SBR_WEBDRIVER environment variable
SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")

# Function to scrape the website using Bright Data Scraping Browser (to surpass captcha)
# https://docs.brightdata.com/scraping-automation/scraping-browser
def scrape_website(website):
    print("Connecting to Scraping Browser...")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print("Waiting captcha to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
            },
        )
        print("Captcha solve status:", solve_res["value"]["status"])
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html

# Extracting the body content from the HTML
def extract_content(html):
    soup = BeautifulSoup(html, "html.parser")
    body_content = soup.find("body")
    if body_content:
        return str(body_content)
    return "No content found"

# Cleaning the body content from Scripts and Styles
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")
    for script_and_style in soup(["script", "style"]):
        script_and_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

# Splitting the DOM content into chunks to give it to the LLM ()
def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length]
        for i in range(0, len(dom_content), max_length)
    ]