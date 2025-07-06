'''
pip install piper-tts

echo 'Welcome to the world of speech synthesis!' | piper \
  --model en_US-lessac-medium \
  --output_file welcome.wav
  it is the code for accssing the piper tts'''

import subprocess
import os

# if not os.path.exists("piper-tts"): 
#     subprocess.run("pip install piper-tts", shell=True)

def run_piper(text: str, model: str = "en_US-lessac-medium", output_file: str = "welcome.wav"):
    try:
        # Run the shell pipe: echo "text" | piper ...
        process = subprocess.run(
            f"echo \"{text}\" | piper --model {model} --output_file {output_file}",
            shell=True,
            check=True
        )
        print(f"[Piper] Saved speech to {output_file}")
    except subprocess.CalledProcessError as e:
        print("[Piper Error]", e)

# Example usage

# audio_player.py
import subprocess
import os

def play_wav(file_path: str):
    if not os.path.exists(file_path):
        print(f"[AudioPlayer] File not found: {file_path}")
        return

    try:
        subprocess.run(
            ["ffplay", "-nodisp", "-autoexit", file_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"[AudioPlayer] Played: {file_path}")
    except Exception as e:
        print(f"[AudioPlayer] Playback error: {e}")

run_piper("Jarvis is your personal AI assistant that greets you, plays music, manages tasks")
play_wav("welcome.wav")
