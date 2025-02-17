from fastapi import FastAPI, File, UploadFile, WebSocket
import whisper
import io
import uvicorn

app = FastAPI()

# Load the OpenAI Whisper model (Tiny model for speed)
model = whisper.load_model("tiny")

@app.post("/api/voice-to-text")
async def voice_to_text(audio: UploadFile = File(...)):
    audio_data = await audio.read()
    audio_file = io.BytesIO(audio_data)
    result = model.transcribe(audio_file)
    return {"text": result["text"]}

@app.get("/api/autocomplete")
async def autocomplete(q: str):
    suggestions = [
        f"{q} red shoes",
        f"{q} blue jeans",
        f"{q} latest trends"
    ]
    return {"suggestions": suggestions}

@app.websocket("/ws/speech-to-search")
async def speech_to_search(websocket: WebSocket):
    await websocket.accept()
    while True:
        audio_chunk = await websocket.receive_bytes()
        audio_file = io.BytesIO(audio_chunk)
        result = model.transcribe(audio_file)
        await websocket.send_text(result["text"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
