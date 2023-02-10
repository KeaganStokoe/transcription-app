from flask import Flask, request, render_template
import whisper
import os

app = Flask(__name__)
model = whisper.load_model("base")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio_file" not in request.files:
        return "No file found", 400
    audio_file = request.files["audio_file"]
    audio_file.save(os.path.join("audio_files", "file_to_transcribe.mp3"))
    print ("File saved successfully")
    model = whisper.load_model("base")
    result = model.transcribe('./audio_files/file_to_transcribe.mp3')
    os.remove("audio_files/file_to_transcribe.mp3")
    return render_template("transcribe.html", transcribed_text=result["text"])


    
if __name__ == "__main__":
    app.run(debug=False)

