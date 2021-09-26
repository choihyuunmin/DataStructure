from gtts import gTTS
import os

my_text = '안녕하세요. 최현민입니다.'
language = 'ko'
myobj = gTTS(text=my_text, lang=language, slow=False)
myobj.save('./gtts_test.mp3')