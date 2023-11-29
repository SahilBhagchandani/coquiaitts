from app import app
import io
from flask import render_template, request, send_file
from app.tts import synthesizer

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/call/martha", methods=["POST"])
def call_martha():
    if "text" in request.form:
        text = request.form["text"]
        print("Text from form:", text)
        
        # Adjust pitch and speak rate as needed
        pitch = 0.0  # Adjust as needed, 0.0 is the default
        speak_rate = 1.0  # Adjust as needed, 1.0 is the default
        
        outputs = synthesizer.tts(text, pitch=pitch, speak_rate=speak_rate)
        out = io.BytesIO()
        synthesizer.save_wav(outputs, out)
        return send_file(out, mimetype="audio/wav")
    else:
        return {"error": "Please provide the text"}, 400
