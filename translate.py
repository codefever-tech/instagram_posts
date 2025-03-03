from googletrans import Translator
import asyncio

# create an asynchronous function
async def translate_text():
    translator = Translator() # get an instance of translator
    # take input
    text = input("Enter text to translate: ") 
    lang = input("Enter target language (e.g., 'es' for Spanish, 'fr' for French): ")
    translation = await translator.translate(text, dest=lang) # translate
    print("Translated:", translation.text)

# running the asynchronous function
asyncio.run(translate_text())
