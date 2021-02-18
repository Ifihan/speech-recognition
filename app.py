from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""

    if request.method == "POST":
        print("Data submitted!")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer
            audio_file = sr.AudioFile(file)
            with audio_file as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)


    return render_template("index.html", transcript=transcript)



if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=5000)