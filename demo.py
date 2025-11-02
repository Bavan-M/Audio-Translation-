import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_API_KEY=os.getenv("OPEN_AI_API_KEY")
openai.api_key=OPEN_AI_API_KEY

audio_file=open("demoAudio.mp3","rb")
output=openai.Audio.translate(model="whisper-1",file=audio_file)
print(output)