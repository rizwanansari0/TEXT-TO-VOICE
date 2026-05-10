from flask import Flask, request, send_file
import requests

app = Flask(__name__)

ELEVENLABS_API = "sk_8e1e1cdd1689318487212a2527895d399b9c50e3de55482a"

VOICE_ID = "EXAVITQu4vr4xnSDxMaL"

@app.route("/")
def home():
    return "Voice API Running"

@app.route("/voice")
def voice():

    prompt = request.args.get("prompt")

    if not prompt:
        return "Prompt Missing"

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": ELEVENLABS_API,
        "Content-Type": "application/json"
    }

    payload = {
        "text": prompt,
        "model_id": "eleven_multilingual_v2"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    if response.status_code == 200:

        with open("/tmp/voice.mp3", "wb") as f:
            f.write(response.content)

        return send_file(
            "/tmp/voice.mp3",
            mimetype="audio/mpeg"
        )

    return response.text

app = app