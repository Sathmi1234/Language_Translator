from deep_translator import GoogleTranslator
from langdetect import detect

def translate_text(text, target_lang):
    source_lang = detect(text)
    translated = GoogleTranslator(
        source=source_lang,
        target=target_lang
    ).translate(text)
    return {
        "source_language": source_lang,
        "target_language": target_lang,
        "translated_text": translated
    }
