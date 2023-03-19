from google.transliteration import transliterate_word
suggestions = transliterate_word('important', lang_code='ar')
print(suggestions)