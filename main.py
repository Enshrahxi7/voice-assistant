import os
import sys
import threading
from tkinter import Tk, Label, Canvas, Toplevel
from tkinter.font import Font
# Ensure system encoding is UTF-8
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np
import cohere
from gtts import gTTS
import pygame
from io import BytesIO

# --- Constants and Configurations ---
DURATION = 5  # seconds
SAMPLE_RATE = 16000  # Hz

# Colors
BG_COLOR = "#121212"
TEXT_COLOR = "#E0E0E0"
ACCENT_COLOR = "#8A2BE2"

# --- Model and Client Initialization ---
model = WhisperModel("medium", compute_type="int8")
co = cohere.Client("")
pygame.mixer.init()

# --- Functions ---
def record_audio():
    """Records audio from the microphone for a specified duration without any UI messages."""
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    return audio

def transcribe_audio(audio):
    """Transcribes recorded audio to text using the Whisper model."""
    audio = audio.flatten().astype(np.float32) / 32768.0
    segments, _ = model.transcribe(audio, language="ar", beam_size=1)
    text = "".join([seg.text for seg in segments])
    return text

def generate_reply(prompt):
    """Generates a short Arabic reply using Cohere."""
    response = co.chat(
        message=prompt,
        temperature=0.5,
        chat_history=[
            {"role": "SYSTEM", "message": "أجب بالعربية فقط، وباختصار شديد."}
        ]
    )
    return response.text.strip()

def speak(text, slow=False):
    """Converts text to speech and plays the audio directly using gTTS and Pygame."""
    tts = gTTS(text, lang='ar', slow=slow)
    audio_stream = BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def run_main_process():
    try:
        # Disable the button visually
        canvas.itemconfig(mic_circle, fill="grey")
        canvas.itemconfig(mic_icon, fill="white")
        
        audio = record_audio()
        text = transcribe_audio(audio)
        
        if not text.strip():
            # If no speech is detected, the assistant will inform the user
            speak("لم يتم اكتشاف أي كلام. الرجاء المحاولة مرة أخرى.")
            return

        reply = generate_reply(text)
        speak(reply, slow=False)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Re-enable the button visually
        canvas.itemconfig(mic_circle, fill=ACCENT_COLOR)
        canvas.itemconfig(mic_icon, fill="white")

def on_mic_click(event):
    if canvas.itemconfig(mic_circle, 'fill')[-1] == ACCENT_COLOR:
        thread = threading.Thread(target=run_main_process)
        thread.start()

# --- Main GUI Setup ---
app = Tk()
app.title("Voice Assistant")
app.geometry("600x400")
app.config(bg=BG_COLOR)

# Welcome message label
welcome_label = Label(app, text="Hello, how can I help you?", font=("Arial", 20), bg=BG_COLOR, fg=TEXT_COLOR)
welcome_label.pack(pady=(80, 20))

# Microphone button using Canvas for a circular shape
canvas = Canvas(app, width=100, height=100, bg=BG_COLOR, highlightthickness=0)
canvas.pack(pady=20)
mic_circle = canvas.create_oval(10, 10, 90, 90, fill=ACCENT_COLOR, outline="")
mic_icon = canvas.create_text(50, 50, text="🎤", font=("Arial", 30), fill="white")
canvas.bind("<Button-1>", on_mic_click)

app.mainloop()

pygame.mixer.quit()