import fitz  # PyMuPDF
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

doc = fitz.open("research.pdf")
text = " ".join(page.get_text() for page in doc)
summary = LsaSummarizer()(PlaintextParser.from_string
                          (text, 
                           Tokenizer("english")).document, 
                           5) # no of sentences

print("Summary of PDF: \n")
print("\n\n".join(str(sentence) for sentence in summary))
