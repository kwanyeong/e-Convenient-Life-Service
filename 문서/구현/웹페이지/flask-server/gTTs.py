from gtts import gTTS
import playsound
import os

text = "반납이 완료되었습니다."

tts = gTTS(text=text, lang='ko')

# 변환된 오디오 파일을 저장합니다. 여기에 파일 이름과 경로를 입력하세요.
tts.save("audio_file.mp3")