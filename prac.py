# from gtts import gTTS
# import os

# my_text = '안녕하세요. 최현민입니다.'
# language = 'ko'
# myobj = gTTS(text=my_text, lang=language, slow=False)
# myobj.save('./gtts_test.mp3')



a = [1,2,3,4,0,4,5,0,4,5,2,6]

for i in a:
    if i == 0:
        a.remove(i)
        
print(a)