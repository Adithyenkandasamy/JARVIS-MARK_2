import pyaudio
import numpy as np
import wave
import time
import os
from faster_whisper import WhisperModel

def listen_and_transcribe(model_size="base", seconds=3):
    model = WhisperModel(model_size, compute_type="int8")
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    audio_buffer = []
    running = True

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    chunk_count = int(RATE / CHUNK * seconds)
    for _ in range(chunk_count):
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_buffer.append(data)

    filename = "temp_input.wav"
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pyaudio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(audio_buffer))
    wf.close()

    segments, _ = model.transcribe(filename)
    full_text = " ".join([seg.text.strip() for seg in segments if seg.text.strip()])
    stream.stop_stream()
    stream.close()
    os.remove(filename) # delete the audio file
    return full_text

# === USAGE EXAMPLE ===
if __name__ == "__main__":
    print("\n[ ] Listening for 3 seconds...")
    transcript = listen_and_transcribe()
    if transcript:
        print(" Jarvis Heard:", transcript)
