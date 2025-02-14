# AI Web Scraper
##  [👉 View Demo](https://github.com/naoufalcb/AI-Web-Scraper?tab=readme-ov-file#demo)
## Overview
This project is an AI-powered web scraper that utilizes OpenAI's API, BrightData's Scraping Browser, Selenium, and other libraries to extract and process website data. It is designed to bypass CAPTCHA challenges and interact with web pages dynamically. The extracted content can be processed with a large language model (LLM) for structured data extraction.

## Features
- **Automated Web Scraping**: Uses Selenium and BrightData's Scraping Browser to access and extract content.
- **CAPTCHA Handling**: Overcomes website CAPTCHA challenges using BrightData's Scraping Browser.
- **Content Cleaning**: Removes unnecessary elements such as scripts and styles from the extracted HTML.
- **AI-Powered Parsing**: Uses OpenAI's API to process and analyze extracted content.
- **Streamlit UI**: Provides a simple user interface for inputting website URLs and processing scraped data.

## Installation
### Prerequisites
Ensure you have Python installed (version 3.7+ recommended).

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/naoufalcb/AI-Web-Scraper
   cd ai-web-scraper
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Adjust the `.env` file in the root directory.
   - Add your [BrightData](https://brightdata.com/) Scraping Browser WebDriver URL:
     ```env
     SBR_WEBDRIVER=your_scraping_browser_webdriver_url
     ```
   - Add your OpenAI API key:
     ```env
     SBR_WEBDRIVER=your_scraping_browser_webdriver_url
     ```

## Demo
### **1. Run the Streamlit app:**
   ```bash
   streamlit run main.py
   ```
### **2. Chose a website to scrape.**
<img src="https://raw.githubusercontent.com/naoufalcb/AI-Web-Scraper/refs/heads/main/demo/step1.png" width='800'>

### **3. Enter a website URL in the input field and click "Scrape".**
<img src="https://raw.githubusercontent.com/naoufalcb/AI-Web-Scraper/refs/heads/main/demo/step2.png" width='800'>

### **3. Review the extracted content.**
<img src="https://raw.githubusercontent.com/naoufalcb/AI-Web-Scraper/refs/heads/main/demo/step3.png" width='800'>

### **4. Provide instructions on what data to extract and click "Parse" to process it with AI.**
<img src="https://raw.githubusercontent.com/naoufalcb/AI-Web-Scraper/refs/heads/main/demo/step4.png" width='800'>

### **5. Results will be displayed in the Streamlit app.**
<img src="https://raw.githubusercontent.com/naoufalcb/AI-Web-Scraper/refs/heads/main/demo/step5.png" width='800'>

## Project Structure
```
├── scrape.py       # Web scraping functions
├── main.py         # Streamlit UI
├── llm.py          # AI-powered parsing functions
├── requirements.txt # Required dependencies
├── .env            # Environment variables
```

## Dependencies
- **Streamlit**: UI for interacting with the scraper.
- **Selenium**: Automates browser interactions.
- **BeautifulSoup4**: Parses and cleans HTML content.
- **BrightData Scraping Browser**: Enables CAPTCHA bypass and advanced scraping.
- **OpenAI API (via LangChain)**: Processes extracted content.
- **Python-dotenv**: Manages environment variables.

## Notes
- Ensure that your BrightData Scraping Browser and OpenAI API credentials are correctly set up in the `.env` file.

## License
This project is licensed under the MIT License.

## Author
[Naoufal CHABAA](https://www.linkedin.com/in/naoufal-chabaa/)

📧 Email: [nchabaa3@gmail.com](mailto:nchabaa3@gmail.com)
