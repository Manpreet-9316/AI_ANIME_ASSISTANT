# voice_chat.py
# =========================================
# Emily AI - Voice + Text Chat (Stable)
# =========================================

# ---- SILENCE ALL WARNINGS & NOISE ----
import os
import warnings
import logging

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["PYTHONWARNINGS"] = "ignore"

logging.getLogger().setLevel(logging.ERROR)

# -------------------------------------

import time
import traceback
import threading

from vad_listener import VADListener
from emotion_engine import detect_emotion
from emotion_state import update_emotion
from response_engine import generate_reply
from voice_emotion_map import get_voice_settings
from voice_clone import speak
from memory import Memory
from action_controller import ActionController


memory = Memory()
controller = ActionController()
running = True


def process_input(text: str):
    """Handles BOTH voice and typed input"""
    if not text:
        return

    text = text.strip()
    if not text:
        return

    print(f"🧑 You: {text}")

    # -------------------------
    # Emotion Detection
    # -------------------------
    try:
        emotion, scores = detect_emotion(text)
        update_emotion(emotion, scores.get(emotion, 0.5))
    except Exception:
        emotion = "neutral"

    print(f"🤖 Emily senses: {emotion}")
    voice_settings = get_voice_settings(emotion)

    # -------------------------
    # ACTION HANDLING
    # -------------------------
    try:
        cmd_dict = controller.normalize_command(text)

        if cmd_dict["intent"] != "unknown" and controller.can_execute(cmd_dict):
            speak("Okay, doing that now.", voice_settings)
            time.sleep(0.3)

            success, msg = controller.execute_command(cmd_dict)
            reply = msg if success else "Sorry, I couldn't do that."

            print(f"🤖 Emily: {reply}")
            speak(reply, voice_settings)

            memory.add(text, reply)
            print("────────────────────────")
            return

    except Exception as action_error:
        print("⚠️ Action error:", action_error)

    # -------------------------
    # NORMAL CHAT
    # -------------------------
    try:
        reply = generate_reply(text, emotion, memory.context())
    except Exception:
        reply = "Sorry, I had a small brain freeze 😅"

    memory.add(text, reply)

    print(f"🤖 Emily: {reply}")
    speak(reply, voice_settings)
    print("────────────────────────")


def text_input_loop():
    """Keyboard input loop"""
    global running
    while running:
        try:
            user_text = input("⌨️ Type here (or 'exit'): ").strip()
            if user_text.lower() == "exit":
                running = False
                break
            process_input(user_text)
        except EOFError:
            break


def main():
    global running
    print("\n🎙️ Emily AI started.")
    print("👉 Speak OR type your commands.")
    print("👉 Type 'exit' to quit.\n")

    listener = VADListener()

    # Start text input in separate thread
    text_thread = threading.Thread(target=text_input_loop, daemon=True)
    text_thread.start()

    try:
        listener.listen(process_input)

    except KeyboardInterrupt:
        pass

    except Exception as e:
        print("❌ Fatal error:", e)
        traceback.print_exc()

    finally:
        running = False
        controller.shutdown()
        print("\n👋 Emily: Bye! Talk soon.")


if __name__ == "__main__":
    main()
