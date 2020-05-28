import urllib
from googletrans import Translator


def read_text():
    file = open("file-to-check.txt")
    content = file.read()
    file.close()
    translated_content = translate_to_english(content)
    check_profanity(translated_content)


def translate_to_english(text_to_translate):
    translator = Translator()
    return translator.translate(text_to_translate, src='auto', dest='en').text


def check_profanity(text_to_check):
    text_to_check = urllib.parse.quote(text_to_check)
    url = "http://wdylike.appspot.com/?q="+text_to_check
    connection = urllib.request.urlopen(url)
    output = connection.read().decode('utf-8')
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")


read_text()
