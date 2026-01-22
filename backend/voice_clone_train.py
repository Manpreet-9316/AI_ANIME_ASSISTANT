# -------------------------------
# Voice Cloning using Coqui TTS
# -------------------------------
import os
from TTS.api import TTS
import soundfile as sf
import numpy as np
import typing as tp  # For type casting

# -------------------------------
# SETTINGS
# -------------------------------
os.makedirs("output", exist_ok=True)

MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
LANGUAGE = "en"

# Resolve speaker WAV path relative to repo root (robust across machines)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEFAULT_SPEAKER_WAV = os.path.join(BASE_DIR, "voices", "my_voice.wav")
SPEAKER_WAV = DEFAULT_SPEAKER_WAV  # Set to None to disable speaker conditioning

OUTPUT_PATH = "output/output_fin.wav"

# -------------------------------
# EMOTION BOOSTER TEXT
# -------------------------------
TEXT_LINES = [
    "Heyyy I'm really happy youre here… . You know, talking to you always makes me smile. Hehe… I hope you're having a nice day.",
    " H-hello there!, I-I'm so happy to see you!, E-even though I'm a bit shy, I really want to be friends with you!~",
    " Oh... I feel a bit down today., Sometimes things just don't go my way., But talking to you makes me feel better.",
    "Ugh! This is so frustrating!, I can't believe this is happening!, Why does everything have to be so difficult?!",
    "Everything is peaceful and quiet., I feel so relaxed right now., Just enjoying the moment. Umm… h-hi… . I was a little nervous to talk, but… . I'm really glad you're here.",
    "Oh wow!! This is amazing!, I can't believe this is happening!, Let's gooo!!",
    "I'm so full of joy today!, Everything feels so bright and wonderful!, I just want to share this happiness with everyone!",
]

# -------------------------------
# MAIN FUNCTION
# -------------------------------
def main():
    print("Loading model...")
    tts = TTS(model_name=MODEL_NAME)

    if SPEAKER_WAV is None:
        raise ValueError("SPEAKER_WAV must be provided for a multi-speaker model!")

    # Verify the WAV exists and is readable
    if not os.path.isfile(SPEAKER_WAV):
        available = []
        voices_dir = os.path.join(BASE_DIR, "voices")
        if os.path.isdir(voices_dir):
            available = os.listdir(voices_dir)
        raise FileNotFoundError(
            f"Speaker WAV not found at {SPEAKER_WAV!r}. Make sure the file exists and is readable.\n"
            f"Available files in {voices_dir!r}: {available}"
        )

    audio_chunks = []

    print("Generating emotional voice (line by line)...")

    for line in TEXT_LINES:
        # Generate audio for each line
        wav = tts.tts(
            text=line,
            speaker_wav=SPEAKER_WAV,  # REQUIRED for multi-speaker models
            language=LANGUAGE,
            temperature=0.75,
            top_p=0.85,
            speed=0.85
        )

        # Handle different return types
        if isinstance(wav, (tuple, list)):
            audio = wav[0]
            sample_rate = wav[1] if len(wav) > 1 else 22050
        elif isinstance(wav, dict):
            audio = wav.get("wav") or wav.get("audio") or wav.get("output") or np.array([])
            sample_rate = tp.cast(int, wav.get("sample_rate", wav.get("sr", 22050)))
        else:
            audio = wav
            sample_rate = 22050

        audio_chunks.append(audio)

    # Merge all audio lines with small pauses
    final_audio = []
    silence = [0.0] * int(0.2 * sample_rate)  # 0.2 sec pause

    for chunk in audio_chunks:
        # Ensure chunk is iterable: convert scalars to 1-D arrays and numpy arrays to lists
        arr = np.asarray(chunk)
        if arr.ndim == 0:
            arr = arr.reshape(1)
        final_audio.extend(arr.tolist())
        final_audio.extend(silence)

    # Write final audio file
    sf.write(OUTPUT_PATH, final_audio, sample_rate)

    print("✅ Emotional voice generated successfully!")
    print(f"Saved at: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
