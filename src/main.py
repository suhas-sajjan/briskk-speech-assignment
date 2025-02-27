from fastapi import FastAPI, UploadFile, File
import whisper
import os

app = FastAPI()

# Load the Whisper model (using "base" as you tested)
model = whisper.load_model("base")

@app.get("/")
def check_server():
    """See if the server is on."""
    return {"message": "Server is on"}

@app.post("/api/voice-to-text")
async def transcribe_audio(audio: UploadFile = File(...)):
    """Turn audio into text using Whisper."""
    # Save the uploaded file temporarily with a clean name
    temp_path = os.path.join("temp_audio.wav")
    with open(temp_path, "wb") as f:
        f.write(await audio.read())  # Save the uploaded audio

    # Transcribe the audio using the loaded model
    result = model.transcribe(temp_path)
    text = result["text"]  # Get the transcribed text

    # Clean up the temporary file
    os.remove(temp_path)

    return {"text": text}