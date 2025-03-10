import json
from googletrans import Translator

path = "dictionary.json"
with open(path, "r", encoding="utf-8") as file:
    dictionary = json.load(file)


def googletranslate(kannada_text, dest):
    translator = Translator()
    try:
        translation = translator.translate(kannada_text, src='kn', dest=dest)
        return translation.text
    except Exception as e:
        print(f"Error translating to English: {e}")
        return "Translation failed."


def translate_word_or_sentence(dictionary, halegannada_text):
    words = halegannada_text.split()
    kannada_translations = []

    # Translate each word from Halegannada to Hosagannada (Kannada)
    for word in words:
        kannada_translation = dictionary.get(word, [word])[0] # Default to the word itself if not in dictionary
        if isinstance(kannada_translation, list):  # If there are multiple meanings
            kannada_translations.append(' or '.join(kannada_translation))  # Show multiple meanings
        else:
            kannada_translations.append(kannada_translation)

    # Join Kannada translations into a sentence
    kannada_text = " ".join(kannada_translations)
    kannada_text = googletranslate(kannada_text ,"kn")

    # Translate the full Kannada sentence to English
    english_translation = googletranslate(kannada_text,"en")

    return kannada_text, english_translation


def main():
    halegannada_input = input("Enter a Halegannada word/sentence: ").strip()

    # Get translations
    kannada_translation, english_translation = translate_word_or_sentence(
        dictionary, halegannada_input
    )

    # Display translations
    print(f"Kannada (Hosagannada) translation: {kannada_translation}")
    print(f"English translation: {english_translation}")


if __name__ == "__main__":
    main()
