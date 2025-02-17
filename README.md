# 🗣️ Briskk Speech-to-Text Assignment

## 📌 Introduction

Welcome to the **Briskk AI Speech-to-Text Assignment**! 🎤  
This challenge will test your **AI integration, API development, and problem-solving skills** through a **structured sequence of tasks**.  

🚀 **Your Goal:** Build a **real-time, noise-resilient voice-based search assistant** that:
✅ Converts voice input (audio file or live mic input) into text.  
✅ Suggests **smart search autocompletions** based on user intent.  
✅ Handles **noisy background audio** and improves speech accuracy.  
✅ Supports **real-time speech-to-search via WebSockets**.  

---

## 📋 **Assignment Structure**
To ensure a smooth progression, complete each **task in sequence**:  

### **🔹 Task 1: Speech Recognition API (Baseline)**
✅ Implement a **FastAPI service** that:  
- Accepts an **audio file** and converts speech to text using **OpenAI Whisper or Mozilla DeepSpeech**.  
- Returns JSON output `{ "text": "<transcribed text>" }`.  
- **Test Input:** `sample_data/clean_audio/sample_english.wav`  
- **Expected Output:** `"Find me a red dress"`  

**📌 API:**  
```http
POST /api/voice-to-text
Content-Type: multipart/form-data
```  

---

### **🔹 Task 2: Handle Noisy Audio (Advanced AI Processing)**
✅ Enhance speech recognition by:  
- **Filtering background noise** using **RNNoise, DeepFilterNet, or PyDub**.  
- Comparing accuracy with and without noise removal.  
- **Test Input:** `sample_data/noisy_audio/sample_noisy.wav`  
- **Expected Output (after denoising):** `"Find me a red dress"`  

**📌 Evaluation Criteria:**  
✔ Speech accuracy **before vs after** noise removal.  
✔ Processing **time must remain <1s**.  

---

### **🔹 Task 3: Smart Search Autocomplete (AI Ranking)**
✅ Implement an API that:  
- **Suggests relevant results** based on user **intent & previous searches**.  
- **Ranks results dynamically** based on **popularity & trends**.  
- **Test Input:** `"find me"`  
- **Expected Output:** `[ "find me a red dress", "find me a jacket" ]`  

**📌 API:**  
```http
GET /api/autocomplete?q=find+me
```  

**📌 How to Improve?**  
- Store previous searches in **Redis** for ranking.  
- Use **AI embeddings (OpenAI or BERT)** for better matching.  

---

### **🔹 Task 4(optional): Real-Time Speech-to-Search (WebSockets)**
✅ Upgrade the system to **process live speech queries** via WebSockets:  
- Accept **real-time audio streams**.  
- **Continuously transcribe & autocomplete** results dynamically.  
- **Test:** Use a **live microphone** input.  

**📌 API WebSocket:**  
```ws
/ws/speech-to-search
```  

✔ **Bonus**: Deploy the system using **Docker & AWS Lambda**.  

---

## 🔬 **Test Cases** (For Self-Validation)

| **Test Case** | **Input** | **Expected Output** |
|--------------|----------|----------------|
| **Speech Recognition** | `sample_data/clean_audio/sample_english.wav` | `"Find me a red dress"` |
| **Noisy Speech** | `sample_data/noisy_audio/sample_noisy.wav` | `"Find me a red dress"` |
| **Autocomplete Query** | `"find me"` | `["find me a red dress", "find me a jacket"]` |
| **Live Streaming** | Microphone | Real-time suggestions |

📂 All **sample audio files** are provided in `sample_data/`.  

---

## 🏗️ **Setup & Running Instructions**

### **1️⃣ Install Dependencies**
```bash
pip install fastapi uvicorn openai-whisper soundfile numpy scipy
```

### **2️⃣ Run the API**
```bash
uvicorn src.main:app --reload
```

### **3️⃣ Test API**
- Open **Swagger Docs** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- Upload `sample_audio_english.wav` and check transcription accuracy.  

---

## 🚀 **Submission Guidelines**

📌 **Fork this repo & create a new branch `candidate-<yourname>`**.  
📌 **Push your implementation & submit a Pull Request (PR)**.  
📌 **Explain your approach in a README**.  

For questions, contact us at: **wizard@briskk.one**  

---

## 📩 **Contact & Discussion**

📢 Have questions? Drop an email at **wizard@briskk.one** 🚀
