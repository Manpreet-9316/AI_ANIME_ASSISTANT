# 🎀 AI Anime Assistant - Backend

<div align="center">

[![Offline](https://img.shields.io/badge/🔒-100%25%20Offline-brightgreen?style=for-the-badge)](https://github.com)
[![Privacy](https://img.shields.io/badge/🛡️-Privacy%20First-blue?style=for-the-badge)](https://github.com)
[![No APIs](https://img.shields.io/badge/✅-Zero%20APIs-success?style=for-the-badge)](https://github.com)
[![License](https://img.shields.io/badge/📄-MIT-yellow?style=for-the-badge)](https://github.com)

An advanced **fully offline** voice-enabled AI assistant backend with emotional intelligence, real-time speech processing, and intelligent action handling. This system powers an anime-style conversational AI that understands and responds to user emotions through natural language and voice.

🔒 **100% Offline & Privacy-Focused** - No cloud APIs, no external services, no data collection. All processing happens locally on your machine.

[Features](#-features) • [Setup](#-configuration) • [Usage](#-usage) • [Architecture](#-architecture) • [Offline](#-offline--privacy-features)

</div>

---

---

## 🎯 Features

<table>
<tr>
<td>
  
🔒 **Fully Offline**
- No external APIs
- No cloud dependency
- Complete privacy

</td>
<td>

🎙️ **Voice I/O**
- Real-time capture
- Emotional synthesis
- Local processing

</td>
<td>

😊 **Emotion Detection**
- AI-powered analysis
- Transformer models
- Fallback detection

</td>
</tr>
<tr>
<td>

🧠 **Local LLM**
- Ollama integration
- Runs on localhost
- No API keys

</td>
<td>

🎵 **Voice Cloning**
- On-device synthesis
- XTTS model
- Emotion-aware

</td>
<td>

💾 **Memory**
- Local storage
- Context-aware
- Multi-turn dialogue

</td>
</tr>
<tr>
<td>

⚡ **Action Control**
- System actions
- Permission guards
- Safe defaults

</td>
<td>

🔍 **Intent Recognition**
- Local NLP
- Pattern matching
- Security checks

</td>
<td>

🔐 **Permission Guard**
- Security-focused
- Whitelist/blacklist
- Prevents abuse

</td>
</tr>
</table>

---

## 📁 Project Structure

```
🎀 AI Anime Assistant Backend
│
├── 🎙️ Voice & Audio Processing
│   ├── voice_chat.py              ⭐ Main orchestrator
│   ├── vad_listener.py            🔊 Voice Activity Detection
│   └── audio_input.py             🎵 Audio capture
│
├── 🧠 AI & Language
│   ├── llm_engine.py              🤖 Local LLM (Ollama)
│   ├── emotion_engine.py          😊 Emotion detection
│   ├── emotion_state.py           💭 Emotion tracking
│   └── intent_parser.py           🔍 Intent recognition
│
├── 💬 Response Generation
│   ├── response_engine.py         📝 Response pipeline
│   ├── voice_emotion_map.py       🎚️ Voice parameters
│   ├── voice_clone.py             🎤 TTS synthesis
│   └── voice_clone_train.py       🏋️ Model training
│
├── 💾 Memory & Context
│   └── memory.py                  📚 Conversation history
│
├── 🔐 Security & Actions
│   ├── permission_guard.py        🛡️ Permission checks
│   ├── action_controller.py       ⚙️ Action execution
│   └── system_actions.py          🖥️ System handlers
│
├── 📦 Models & Data
│   ├── tts/                       🗂️ Voice models
│   ├── output/                    📁 Generated audio
│   └── logs/                      📊 Debug logs
│
└── 🧪 Testing
    ├── mic_test.py               🎙️ Audio testing
    ├── whisper_test.py           🗣️ Speech testing
    └── test_email.py             📧 Email testing
```

---

## 🚀 Core Modules

### 🎙️ Voice & Audio Processing

#### `voice_chat.py` ⭐
Main orchestrator combining voice and text input processing with emotional responses.

**🎯 Key Functions:**
- 🎙️ `process_input(text)` - Handles both voice and text input
- 🔊 Real-time VAD (Voice Activity Detection) listening
- 😊 Emotion-aware response generation
- 🎵 Voice synthesis with emotional parameters

#### `vad_listener.py` 🔊
Voice Activity Detection for capturing speech input when user is speaking.

#### `audio_input.py` 🎵
Raw audio input capture and preprocessing for voice analysis.

---

### 🧠 AI & Language Understanding

#### `llm_engine.py` 🤖
Integrates Ollama-based language models (Mistral, Phi3) for conversation.

**🔒 100% Local & Offline:**
```
✅ Ollama running on http://localhost:11434 (no internet required)
✅ Model: Mistral (configurable, runs locally)
✅ No API keys needed
✅ No external service calls
✅ All inference happens on your machine
✅ Complete privacy - conversations never leave your computer
```

**🎯 Key Functions:**
- 🤖 `generate_ai_reply(user_text, emotion, memory_context)` - Generate contextual responses locally

#### `emotion_engine.py` 😊
Detects and analyzes emotions using local transformer models.

**🔒 100% Local & Offline:**
```
✅ Uses DistilBERT emotion classifier (runs locally)
✅ Downloaded once on first use (~500MB)
✅ No API calls to cloud services
✅ Processes emotions on your device
✅ Fallback keyword detection for offline robustness
```

**🎯 Features:**
- 😊 Maps emotions: joy, sadness, anger, fear, surprise, disgust
- 🔄 Fallback detection for model unavailability
- 📊 Returns emotion scores and primary emotion

**🎯 Key Functions:**
- 😊 `detect_emotion(text)` - Returns `(emotion, scores_dict)` - all local processing

#### `emotion_state.py` 💭
Manages current emotion state and state transitions.

#### `intent_parser.py` 🔍
Parses user intent for action triggering.

**🎯 Supported Intents:**
- 🌐 `open_browser` - Launch web browser
- 📝 `open_notepad` - Open text editor
- 🚫 `dangerous` - Blocked for security
- 💬 `chat` - General conversation

---

### 💬 Response Generation

#### `response_engine.py` 📝
Orchestrates the full response generation pipeline combining emotion, intent, and memory.

#### `voice_emotion_map.py` 🎚️
Maps emotional states to voice synthesis parameters (pitch, speed, etc.).

#### `voice_clone.py` 🎤
Text-to-speech synthesis with custom voice cloning using XTTS model.

**🔒 100% Local & Offline:**
```
✅ XTTS model runs on your machine
✅ No cloud TTS services (unlike Google, Azure, AWS TTS)
✅ Voice synthesis happens locally
✅ No audio is sent to external servers
✅ Complete privacy for voice generation
```

**🎯 Key Functions:**
- 🎤 `speak(text, emotion, voice_settings)` - Generate and play emotional speech locally

#### `voice_clone_train.py` 🏋️
Training pipeline for custom voice cloning models.

---

### 💾 Memory & Context

#### `memory.py` 📚
Manages conversation history and contextual memory for coherent multi-turn conversations.

**🎯 Key Functions:**
- 📝 Store and retrieve conversation context
- 📚 Maintain user interaction history

---

### 🔐 Security & Actions

#### `permission_guard.py` 🛡️
Security verification system preventing unauthorized system actions.

**🎯 Features:**
- 🔐 Permission checking for system actions
- ⚡ Safety enforcement
- 📋 Whitelist/blacklist management

#### `action_controller.py` ⚙️
Executes permitted system actions based on user requests.

#### `system_actions.py` 🖥️
Handlers for various system actions (open apps, control settings, etc.).

---

## 🔧 Configuration

### ✅ Required Local Services

**🤖 Ollama LLM Service (Local - 100% Offline)**
```bash
ollama serve  # Start Ollama server on localhost:11434 (OFFLINE MODE)
```

**📦 Supported Models** (Downloaded once, cached locally):
- 🚀 `mistral` - Balanced performance
- ⚡ `phi3` - Faster responses (3.8B params)
- 💬 `neural-chat` - Optimized for conversation
- 🔧 Others supported by Ollama

> ✅ All models run 100% offline once downloaded to your local system.

---

### 📥 Environment Setup

**1️⃣ Install Local Dependencies** (No external API calls)
```bash
pip install requests          # For local Ollama communication
pip install transformers      # Local emotion detection models
pip install torch             # Local ML framework
pip install librosa           # Local audio processing
pip install soundfile         # Local audio I/O
pip install numpy             # Local numerical computing
```

**2️⃣ Download Models (One-time setup)**

**🤖 Ollama Models** (Runs locally, ~4GB for Mistral):
```bash
ollama pull mistral      # Download to ~/.ollama/models/ (offline use)
ollama pull phi3         # Lightweight alternative (~2GB)
```

**😊 Emotion Detection Model** (Auto-downloads, ~500MB):
```
✅ DistilBERT emotion classifier downloads on first run
✅ Cached locally in ~/.cache/huggingface/
✅ No API calls to Hugging Face servers
```

**🎤 Voice Synthesis Model** (XTTS):
```
✅ Download XTTS model files to tts/ directory
✅ Models are loaded on-demand by voice_clone.py
✅ No streaming or external calls needed
```

**3️⃣ Audio Setup** (Local)
```
✅ Ensure microphone is configured on system
✅ Test audio input with mic_test.py
```

---

## 📚 Usage

### ✅ No API Keys Required

This project requires **zero external API keys** or subscriptions:

```
✅ No OpenAI API          ✅ No commercial TTS services
✅ No Google Cloud API    ✅ No cloud storage
✅ No Azure API           ✅ No analytics or tracking
✅ No AWS API             ✅ 100% FREE & OPEN
```

---

### 🎙️ Basic Voice Chat (100% Offline)

```python
from voice_chat import process_input

# Process voice or text input
process_input("Hello, how are you?")
```

### 😊 Emotion Detection

```python
from emotion_engine import detect_emotion

emotion, scores = detect_emotion("I'm so happy!")
print(f"Emotion: {emotion}, Scores: {scores}")
```

### 🤖 Generate LLM Response

```python
from llm_engine import generate_ai_reply

response = generate_ai_reply(
    user_text="Tell me a joke",
    emotion="happy",
    memory_context="User likes programming"
)
print(response)
```

### 🎤 Text-to-Speech

```python
from voice_clone import speak
from voice_emotion_map import get_voice_settings

voice_params = get_voice_settings("happy")
speak("That's wonderful!", emotion="happy", voice_settings=voice_params)
```

---

## 🧪 Testing Utilities

| 🔧 Tool | 📝 Purpose |
|:-------:|:----------:|
| 🎙️ `mic_test.py` | Microphone functionality testing |
| 🗣️ `whisper_test.py` | Speech recognition testing |
| 📧 `test_email.py` | Email integration testing |

---

##  Security Features

```
🔒 Permission Guards: Prevents unauthorized system access
✅ Intent Validation: Validates user intent before execution
🚫 Action Blocking: Blocks shutdown/restart requests
⚡ Safe Defaults: All actions are whitelisted, not blacklisted
```

---

```python
from voice_chat import process_input

# Process voice or text input
process_input("Hello, how are you?")
```

### Emotion Detection

```python
from emotion_engine import detect_emotion

emotion, scores = detect_emotion("I'm so happy!")
print(f"Emotion: {emotion}, Scores: {scores}")
```

### Generate LLM Response

```python
from llm_engine import generate_ai_reply

response = generate_ai_reply(
    user_text="Tell me a joke",
    emotion="happy",
    memory_context="User likes programming"
)
print(response)
```

### Text-to-Speech

```python
from voice_clone import speak
from voice_emotion_map import get_voice_settings

voice_params = get_voice_settings("happy")
speak("That's wonderful!", emotion="happy", voice_settings=voice_params)
```

## 🧪 Testing Utilities

- `mic_test.py` - Microphone functionality testing
- `whisper_test.py` - Speech recognition testing
- `test_email.py` - Email integration testing

## 📊 Logging

Logs are stored in:
- `logs/action_controller_log.txt` - Action execution logs
- `output/` - Generated audio files and debug output

## 🔐 Security Features

- **Permission Guards**: Prevents unauthorized system access
- **Intent Validation**: Validates user intent before execution
- **Dangerous Action Blocking**: Blocks shutdown/restart requests
- **Safe Defaults**: All actions are whitelisted, not blacklisted

## 🔒 Offline & Privacy Features

### 🎯 Zero External Calls

```
✅ No API keys required          ✅ No cloud dependency
✅ No data transmission           ✅ No tracking/telemetry  
✅ No subscriptions              ✅ Complete privacy
✅ No analytics                  ✅ Conversations stay local
```

### 📊 What Happens Offline

| 🎯 Feature | 🏠 Where It Runs | 🔒 Data Privacy |
|:----------:|:----------------:|:----------------:|
| 🧠 **Language Model (LLM)** | Local Ollama server | Stays on device ✅ |
| 😊 **Emotion Detection** | Local DistilBERT model | Stays on device ✅ |
| 🎤 **Voice Synthesis** | Local XTTS model | Stays on device ✅ |
| 💾 **Memory Storage** | Local file system | Stays on device ✅ |
| 🎵 **Audio Processing** | Local PyAudio/Librosa | Stays on device ✅ |
| 🔍 **Intent Detection** | Local regex/patterns | Stays on device ✅ |

### 🌐 Internet Connection

```
❌ NOT required after setup
🌟 Only needed for INITIAL model downloads
🔐 NO data is transmitted even if connected
🛡️ NO tracking or telemetry
```

### 🎯 Perfect For

```
🔒 Privacy-conscious users           🎓 Local development/testing
🚫 Restricted network environments   🛡️ Security-sensitive applications
💻 Offline machines                  👨‍💼 Enterprise deployments
```

---

## 🐛 Troubleshooting

### Ollama Connection Failed
- Ensure Ollama is running: `ollama serve`
- Check URL: `http://localhost:11434`
- Verify model availability: `ollama list`

### Emotion Detection Issues
- If DistilBERT model fails, system uses keyword-based fallback
- Models auto-download on first use (~500MB)

### Audio Issues
- Test microphone with `mic_test.py`
- Check system audio settings
- Verify PyAudio installation

### Voice Synthesis Issues
- Ensure XTTS model files exist in `tts/`
- Check audio output device configuration
- Review `output/` directory for generated files

## 🎨 Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    🎀 AI ANIME ASSISTANT                    │
└─────────────────────────────────────────────────────────────┘

User Input (Voice 🎙️ / Text 💬)
         ↓
    ┌─────────────┐
    │ VAD Listener│  ← 🎧 Voice Activity Detection
    │ Text Parser │  ← 📝 Parse User Input
    └──────┬──────┘
           ↓
    ┌─────────────────┐
    │ Emotion Engine  │  ← 😊 Detect emotion
    │ (DistilBERT)   │
    └──────┬──────────┘
           ↓
    ┌─────────────────┐
    │ Intent Parser   │  ← 🔍 What does user want?
    └──────┬──────────┘
           ↓
    ┌─────────────────┐
    │ Permission Guard│  ← 🛡️ Is action allowed?
    └──────┬──────────┘
           ↓
    ┌─────────────────┐
    │ LLM Engine      │  ← 🤖 Generate response
    │ (Ollama Local)  │    (Mistral/Phi3)
    └──────┬──────────┘
           ↓
    ┌─────────────────┐
    │ Response Engine │  ← 📝 Build response
    └──────┬──────────┘
           ↓
    ┌─────────────────────┐
    │ Voice Emotion Map    │  ← 🎚️ Set voice params
    │ (Pitch/Speed/Tone)  │
    └──────┬──────────────┘
           ↓
    ┌──────────────────┐
    │ Voice Synthesis  │  ← 🎤 Generate audio
    │ (XTTS Local)     │
    └──────┬───────────┘
           ↓
    ┌──────────────────────────┐
    │ 🔊 Audio Output          │
    │ 💾 Memory Storage        │
    │ 📊 Action Logging        │
    └──────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  ✅ Everything stays local • 🔒 100% Privacy • ⚡ Offline  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚦 State Management

**😊 Emotion State:**
```
• Current emotion: happy, sad, angry, calm, fear, surprise
• Intensity: 0.0 - 1.0 (scale)
• Auto-updates: Based on user input
```

**💾 Memory State:**
```
• Conversation history (stored locally)
• User preferences
• Context windows for multi-turn dialogue
```

---

## 📦 Dependencies

### ✅ Core (All Local Processing)

| 📦 Package | 🎯 Purpose |
|:----------:|:----------:|
| `requests` | HTTP requests to **local** Ollama (not external services) |
| `transformers` | Local emotion classification models |
| `torch` | Local deep learning framework |
| `librosa` | Local audio processing |
| `soundfile` | Local audio I/O |
| `numpy` | Local numerical computing |

### 🔧 Optional

- `ollama-python` - Alternative local Ollama client
- `pyttsx3` - Local text-to-speech fallback
- `pyaudio` - Local audio device management

### ✅ Zero External Dependencies
```
❌ No cloud SDKs (AWS, Azure, Google Cloud)
❌ No API client libraries
❌ No telemetry/tracking libraries
❌ No subscription-based services
```

---

## 📝 License

This project is part of the AI Anime Assistant suite.

---

## 🤝 Contributing

Contributions welcome! Please ensure:
- ✅ Code follows existing style conventions
- ✅ Emotion detection maintains accuracy
- ✅ Voice output quality is tested
- ✅ Security features remain intact
- ✅ Documentation is updated with changes

---

## 🐛 Troubleshooting

### ❌ Ollama Connection Failed
```bash
# Solution:
ollama serve                    # Ensure Ollama is running
# Check URL: http://localhost:11434
ollama list                    # Verify model availability
```

### ❌ Emotion Detection Issues
```
✅ If DistilBERT model fails, system uses keyword-based fallback
✅ Models auto-download on first use (~500MB)
```

### ❌ Audio Issues
```bash
# Solutions:
python mic_test.py            # Test microphone
# Check system audio settings
# Verify PyAudio installation
```

### ❌ Voice Synthesis Issues
```
✅ Ensure XTTS model files exist in tts/
✅ Check audio output device configuration
✅ Review output/ directory for generated files
```

---

## 📞 Support & Resources

For issues or questions:

| 🔧 Resource | 📝 Details |
|:----------:|:----------:|
| 📊 **Logs** | Check `logs/` directory for debugging |
| 🧪 **Test Utilities** | Run provided test scripts |
| 🔍 **Model Check** | Verify Ollama & model availability |
| 📖 **Documentation** | Review this README for detailed info |

---

<div align="center">

## 🌟 Status & Info

[![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=flat-square)](https://github.com)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-January%202026-blue?style=flat-square)](https://github.com)
[![Python](https://img.shields.io/badge/Python-3.8%2B-informational?style=flat-square)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://github.com)

### 🎯 Key Stats

```
✅ 100% Offline        🔒 Privacy-First       ⚡ No APIs
💻 Local Processing    🎵 Voice Enabled       🤖 AI-Powered
🛡️ Secure            📱 Multi-Device        🚀 Production Ready
```

---

**Made with ❤️ for privacy-conscious users**  
**AI Anime Assistant Backend v1.0**

</div>
