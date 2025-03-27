import requests  # To fetch webpage content
from bs4 import BeautifulSoup  # For parsing HTML and extracting text
from sumy.parsers.plaintext import PlaintextParser  # To parse raw text
from sumy.nlp.tokenizers import Tokenizer  # Tokenizer for summarization
from sumy.summarizers.lsa import LsaSummarizer  # LSA-based text summarizer
import textwrap  # For formatting output with indentation

def summarize_webpage(url, sentences=3):  
    # Fetch webpage content
    html = requests.get(url).text  

    # Parse HTML using BeautifulSoup and extract all paragraph (<p>) text
    soup = BeautifulSoup(html, "html.parser")  
    text = " ".join(p.text for p in soup.find_all("p"))  

    # Prepare the text for summarization
    parser = PlaintextParser.from_string(text, Tokenizer("english"))  
    summarizer = LsaSummarizer()  # Create LSA summarizer instance

    # Generate summary with the specified number of sentences
    summary = summarizer(parser.document, sentences)  

    # Format and print each sentence with indentation
    for sentence in summary:  
        indented_text = textwrap.fill(str(sentence), 
                                      width=75,  # Wrap text at 75 characters
                                      initial_indent="    ",  # Indent first line
                                      subsequent_indent="    ")  # Indent following lines
        print(indented_text, "\n")  # Print formatted summary

# Example Usage
url = "https://en.wikipedia.org/wiki/Natural_language_processing"  
print("Summary of the above webpage: \n")
summarize_webpage(url)  # Call function to fetch and summarize webpage
