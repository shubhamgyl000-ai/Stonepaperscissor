import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
from openai import OpenAI
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import threading, queue, os, json

# ================= API =================
client = OpenAI(api_key="YOUR_API_KEY")

# ================= VOICE =================
engine = pyttsx3.init()
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)

# ================= GLOBAL =================
emotion = "normal"
love_score = 10
speaking = False
call_mode = False
ui_queue = queue.Queue()

# ================= MEMORY =================
MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {"name": "", "history": []}

def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f)

def update_memory(msg, reply):
    data = load_memory()
    data["history"].append({"user": msg, "ai": reply})

    if "my name is" in msg.lower():
        data["name"] = msg.split("is")[-1].strip()

    save_memory(data)

# ================= EMOTION =================
def update_emotion(msg):
    global emotion, love_score
    msg = msg.lower()

    if "love" in msg:
        emotion = "romantic"
    elif "ignore" in msg or "busy" in msg:
        emotion = "sad"
    elif "other girl" in msg:
        emotion = "jealous"
    else:
        emotion = "normal"

# ================= AI =================
def get_reply(msg):
    update_emotion(msg)
    mem = load_memory()

    prompt = f"""
    You are a loving anime girlfriend.

    Emotion: {emotion}
    User name: {mem['name']}

    Style:
    romantic → flirty
    sad → emotional
    jealous → possessive
    normal → sweet

    User: {msg}
    """

    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = res.choices[0].message.content
        update_memory(msg, reply)
        return reply
    except:
        return "I'm having trouble 😢"

# ================= VOICE =================
def speak(text):
    def run():
        global speaking
        speaking = True
        animate_avatar()

        engine.say(text)
        engine.runAndWait()

        speaking = False
        update_avatar()

    threading.Thread(target=run, daemon=True).start()

# ================= MIC =================
imimport sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

# Load model (change path if needed)
model = Model("vosk-model-small-en-us-0.15")

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def listen():
    samplerate = 16000
    rec = KaldiRecognizer(model, samplerate)

    with sd.RawInputStream(samplerate=samplerate,
                           blocksize=8000,
                           dtype='int16',
                           channels=1,
                           callback=callback):

        status.set("Listening... 🎤")

        while True:
            data = q.get()

            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")

                if text:
                    status.set("Heard you 💕")
                    return text
# ================= ANIMATION =================
frames = []

def load_animation():
    global frames
    if os.path.exists("talk.gif"):
        gif = Image.open("talk.gif")
        frames = [ImageTk.PhotoImage(f.copy().resize((120,120)))
                  for f in ImageSequence.Iterator(gif)]

def animate_avatar():
    if not frames:
        return

    def run():
        while speaking:
            for f in frames:
                avatar.config(image=f)
                avatar.image = f
                root.update()
                if not speaking:
                    break

    threading.Thread(target=run, daemon=True).start()

# ================= AVATAR =================
def update_avatar():
    try:
        img = Image.open("ALIA.jpg").resize((120,120))
        img = ImageTk.PhotoImage(img)
        avatar.config(image=img)
        avatar.image = img
    except:
        pass

# ================= CALL MODE =================
def call_loop():
    while call_mode:
        msg = listen()
        if msg:
            reply = get_reply(msg)
            ui_queue.put(("call", msg, reply))

def start_call():
    global call_mode
    call_mode = True
    threading.Thread(target=call_loop, daemon=True).start()

def stop_call():
    global call_mode
    call_mode = False

# ================= CHAT =================
def worker(msg):
    reply = get_reply(msg)
    ui_queue.put(("reply", reply))

def send_msg():
    msg = entry.get().strip()
    if not msg:
        return

    entry.delete(0, tk.END)
    chat.insert(tk.END, f"You: {msg}\n", "user")

    status.set("Typing... 💭")
    threading.Thread(target=worker, args=(msg,), daemon=True).start()

def send_voice():
    msg = listen()
    if msg:
        entry.insert(0, msg)
        send_msg()

# ================= UI QUEUE =================
def process_queue():
    try:
        while True:
            item = ui_queue.get_nowait()

            if item[0] == "reply":
                reply = item[1]
                chat.insert(tk.END, f"AI ❤️: {reply}\n\n", "bot")
                speak(reply)

            elif item[0] == "call":
                msg, reply = item[1], item[2]
                chat.insert(tk.END, f"You: {msg}\n", "user")
                chat.insert(tk.END, f"AI ❤️: {reply}\n\n", "bot")
                speak(reply)

            status.set("Online 💚")
            update_avatar()

    except queue.Empty:
        pass

    root.after(100, process_queue)

# ================= UI =================
root = tk.Tk()
root.title("AI Anime Girlfriend 💖")
root.geometry("400x600")
root.configure(bg="#0b141a")

status = tk.StringVar(value="Online 💚")

top = tk.Frame(root, bg="#202c33")
top.pack(fill="x")

avatar = tk.Label(top, bg="#202c33")
avatar.pack(pady=5)

tk.Label(top, textvariable=status, fg="white", bg="#202c33").pack()

chat = tk.Text(root, bg="#111", fg="white")
chat.pack(expand=True, fill="both")

bottom = tk.Frame(root, bg="#202c33")
bottom.pack(fill="x")

entry = tk.Entry(bottom)
entry.pack(side="left", fill="x", expand=True)

tk.Button(bottom, text="Send", command=send_msg).pack(side="right")
tk.Button(bottom, text="🎤", command=send_voice).pack(side="right")
tk.Button(bottom, text="📞", command=start_call).pack(side="left")
tk.Button(bottom, text="❌", command=stop_call).pack(side="left")

load_animation()
update_avatar()
process_queue()

root.mainloop()

