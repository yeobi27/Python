# import googletrans
from googletrans import Translator

translator = Translator()

# print(translator.translate('안녕하세요'))

# print(translator.translate('안녕하세요').text)

# print(googletrans.LANGUAGES)

print(translator.detect('이 언어는 한국어입니다.'))
print(translator.detect('veritas lux mea'))
# result
# Detected(lang=ko, confidence=1)
# Detected(lang=la, confidence=0.66786897)