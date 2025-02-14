import streamlit as st

from scrape import scrape_website, extract_content, clean_body_content, split_dom_content
from llm import parse_with_llm


# Streamlit UI
st.title('AI Web Scraper')
url = st.text_input('Enter a Website URL')

# Scrape the website
if st.button('Scrape'):
    st.write('Scraping...')
    result = scrape_website(url)
    body_content = extract_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander('Show content'):
        st.text_area("DOM Content", cleaned_content, height=300)

# Ask question to the LLM about the DOM content
if "dom_content" in st.session_state:
    parse_description = st.text_area('What data do you want to scrape?')

    if st.button('Parse'):
        if parse_description:
            st.write('Parsing...')
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_llm(dom_chunks, parse_description)
            st.write(result)

