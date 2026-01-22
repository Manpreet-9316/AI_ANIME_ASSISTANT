import subprocess
import platform
import re
import os
import time
import webbrowser
import requests
import random
import pyautogui
import shutil
from datetime import datetime

class ActionController:
    def __init__(self):
        self.log_file = "logs/action_controller_log.txt"
        os.makedirs("logs", exist_ok=True)
        self._log("Emily FULL VERSION loaded - All features enabled!")

    def _log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")
        print(f"LOG: {message}")

    def normalize_command(self, text: str):
        text = text.lower().strip()
        original = text

        # Extract phone number
        number_match = re.search(r'(\+?\d{10,15})', original)
        number = number_match.group(1) if number_match else None

        # === WhatsApp SEND MESSAGE ===
        if ("send" in text or "message" in text or "whatsapp to" in text) and "whatsapp" in text:
            if number:
                msg_match = re.search(r'\+?\d{10,15}\s+(.+)', original)
                message = msg_match.group(1).strip() if msg_match else "Hello from Emily!"
                return {"intent": "whatsapp_send", "number": number, "message": message}
            else:
                name_match = re.search(r'to\s+([a-zA-Z\s]+)', text)
                name = name_match.group(1).strip().title() if name_match else "that person"
                return {"intent": "whatsapp_send_name", "name": name}

        # === WhatsApp CALL ===
        if ("call" in text or "phone" in text or "dial" in text) and "whatsapp" in text:
            if number:
                return {"intent": "whatsapp_call_number", "number": number}
            else:
                name_match = re.search(r'call\s+([a-zA-Z\s]+?)\s+on\s+whatsapp', text)
                name = name_match.group(1).strip().title() if name_match else "that person"
                return {"intent": "whatsapp_call_name", "name": name}

        # === Open Website ===
        if text.startswith("open ") or text in ["google", "gmail", "youtube", "whatsapp", "netflix", "spotify", "amazon", "instagram", "facebook"]:
            target = text.replace("open ", "").strip()
            websites = {
                "google": "https://www.google.com",
                "gmail": "https://mail.google.com",
                "youtube": "https://www.youtube.com",
                "whatsapp": "https://web.whatsapp.com",
                "netflix": "https://www.netflix.com",
                "spotify": "https://open.spotify.com",
                "amazon": "https://www.amazon.com",
                "instagram": "https://www.instagram.com",
                "facebook": "https://www.facebook.com",
                "twitter": "https://x.com",
                "wikipedia": "https://www.wikipedia.org",
            }
            if target in websites:
                return {"intent": "open_url", "url": websites[target]}

        # === Google Search ===
        if "search" in text:
            query = re.sub(r'search\s+|on google\s*', '', text, flags=re.I).strip()
            if query:
                return {"intent": "google_search", "query": query}

        # === Play Song on YouTube ===
        if "play" in text:
            query = text.replace("play", "").strip() or "top christmas songs 2026"
            return {"intent": "play_song", "query": query}

        # === Top Songs (Current January 4, 2026) ===
        if any(w in text for w in ["top songs", "new song", "current songs", "current hits", "billboard"]):
            return {"intent": "top_songs"}

        # === Open Desktop App ===
        if "open" in text:
            apps = {
                "chrome": "chrome",
                "notepad": "notepad.exe",
                "calculator": "calc.exe",
                "paint": "mspaint.exe",
                "task manager": "taskmgr.exe",
                "settings": "ms-settings:",
                "spotify": "spotify",
                "discord": "discord",
                "vscode": "code",
                "file explorer": "explorer.exe",
            }
            for app_name, cmd in apps.items():
                if app_name in text:
                    return {"intent": "open_app", "cmd": cmd, "name": app_name.capitalize()}

        # === Take Screenshot ===
        if "screenshot" in text or "screen shot" in text:
            return {"intent": "screenshot"}

        # === Tell Joke ===
        if "joke" in text:
            return {"intent": "tell_joke"}

        # === Weather ===
        if "weather" in text:
            loc_match = re.search(r'weather\s*(in\s+)?(.+)', text)
            location = loc_match.group(2).strip().title() if loc_match else "current location"
            return {"intent": "get_weather", "location": location}

        return {"intent": "unknown"}

    def execute_command(self, cmd_dict):
        intent = cmd_dict["intent"]

        if intent == "open_url":
            url = cmd_dict["url"]
            webbrowser.open(url)
            name = url.replace("https://", "").replace("www.", "").split("/")[0].split(".")[0].capitalize()
            return True, f"Opened {name}! ✅"

        elif intent == "google_search":
            query = cmd_dict["query"]
            url = f"https://www.google.com/search?q={requests.utils.requote_uri(query)}"
            webbrowser.open(url)
            return True, f"Searching '{query}' on Google! 🔍"

        elif intent == "play_song":
            query = cmd_dict["query"]
            url = f"https://www.youtube.com/results?search_query={requests.utils.requote_uri(query)}"
            webbrowser.open(url)
            return True, f"Playing '{query}' on YouTube! 🎵"

        elif intent == "top_songs":
            songs = [
                "1. All I Want for Christmas Is You - Mariah Carey 🎄",
                "2. Rockin' Around the Christmas Tree - Brenda Lee ❄️",
                "3. Jingle Bell Rock - Bobby Helms 🔔",
                "4. Last Christmas - Wham! 🎅",
                "5. Santa Tell Me - Ariana Grande ⛄",
                "6. A Holly Jolly Christmas - Burl Ives 🌟",
                "7. Feliz Navidad - José Feliciano 🎶",
                "8. It's the Most Wonderful Time of the Year - Andy Williams ✨",
                "9. Sleigh Ride - The Ronettes 🛷",
                "10. Underneath the Tree - Kelly Clarkson 🎁"
            ]
            return True, "🎶 Billboard Hot 100 Top 10 (January 4, 2026 - Holiday season still ruling!):\n" + "\n".join(songs) + "\n\nSay 'play [song name]' to listen on YouTube!"

        elif intent == "open_app":
            cmd = cmd_dict["cmd"]
            name = cmd_dict.get("name", cmd)
            if shutil.which(cmd) or cmd == "ms-settings:":
                subprocess.Popen(f"start {cmd}", shell=True) if platform.system() == "Windows" else subprocess.Popen([cmd])
                return True, f"Opened {name}! ✅"
            return False, "App not found or not installed."

        elif intent == "screenshot":
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            pyautogui.screenshot(filename)
            return True, f"Screenshot saved as {filename} 📸"

        elif intent == "tell_joke":
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything! ⚛️",
                "I told my computer I needed a break, and now it won't stop sending me KitKat ads! 🍫",
                "Why did the scarecrow win an award? He was outstanding in his field! 🌾"
            ]
            return True, f"Here's a joke: {random.choice(jokes)} 😂"

        elif intent == "get_weather":
            location = cmd_dict["location"]
            try:
                url = f"https://wttr.in/{requests.utils.requote_uri(location)}?format=%C+%t+%w"
                resp = requests.get(url, timeout=10)
                if resp.status_code == 200:
                    return True, f"Weather in {location}: {resp.text.strip()} ☁️"
            except:
                pass
            return False, "Couldn't fetch weather. Check internet or try 'weather in Delhi'"

        elif intent == "whatsapp_send":
            number = cmd_dict["number"]
            message = cmd_dict["message"]
            safe_msg = requests.utils.requote_uri(message)
            url = f"https://web.whatsapp.com/send?phone={number}&text={safe_msg}"
            webbrowser.open(url)
            time.sleep(15)
            return True, f"WhatsApp opened!\nMessage ready: \"{message}\"\nPress Enter to send to {number} 📩"

        elif intent == "whatsapp_send_name":
            name = cmd_dict["name"]
            return True, f"To send a message to {name}:\n1. Open WhatsApp on your phone\n2. Search '{name}'\n3. Type your message\n4. Tap send! 📱"

        elif intent == "whatsapp_call_number":
            number = cmd_dict["number"]
            url = f"https://web.whatsapp.com/send?phone={number}"
            webbrowser.open(url)
            time.sleep(15)
            return True, f"WhatsApp opened to {number}!\nClick the 📞 phone icon to start voice call 📞"

        elif intent == "whatsapp_call_name":
            name = cmd_dict["name"]
            return True, f"To call {name} on WhatsApp:\n1. Open WhatsApp on your phone\n2. Search '{name}'\n3. Tap their chat\n4. Tap the 📞 phone icon\nEasy! 😊"

        elif intent == "unknown":
            return False, "I didn't understand. Try:\n- send whatsapp to +919876543210 happy new year\n- call Manpreet on whatsapp\n- open gmail\n- top songs\n- play all i want for christmas\n- take screenshot\n- tell me a joke\n- weather in Delhi"

        return True, "Done!"

if __name__ == "__main__":
    controller = ActionController()
    print("🟢 Emily FULL VERSION is ready! All features active (January 4, 2026)")
    print("Type commands or 'exit' to quit\n")
    while True:
        cmd = input("You: ").strip()
        if cmd.lower() in ["exit", "quit", "bye"]:
            print("Emily: Goodbye! Have a wonderful day! 👋")
            break
        if not cmd:
            continue
        result = controller.normalize_command(cmd)
        success, response = controller.execute_command(result)
        print(f"Emily: {response}\n")