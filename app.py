import openai
import os
from dotenv import load_dotenv
from flask import Flask,request,redirect,url_for,jsonify,render_template

load_dotenv()
OPEN_AI_API_KEY=os.getenv("OPEN_AI_API_KEY")
openai.api_key=OPEN_AI_API_KEY

app=Flask(__name__)
app.config["UPLOAD_FOLDER"]="static"

@app.route('/',methods=['GET','POST'])
def main():
    if request.method=='POST':
        language=request.form["language"]
        file=request.files['file']
        if file:
            filename=file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

            audio_file=open("static/Recording.mp3","rb")
            trnascript=openai.Audio.translate(model="whisper-1",file=audio_file)

            response=openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role":"system","content":f"You will be provided with a sentence in English,and your task is to translate it into {language}"},
                    {"role":"user","content":trnascript.text},
                ],
                temperature=0,
                max_tokens=100
            )
            return jsonify(response)
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True,port=8080)
