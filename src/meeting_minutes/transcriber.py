import os
import wave
import json
from pydub import AudioSegment
from pydub.utils import make_chunks
from utils import load_settings
import vosk
import openai

def convert_audio_to_wav(audio_file_path):
    if audio_file_path.endswith('.mp3'):
        audio = AudioSegment.from_mp3(audio_file_path)
        wav_file_path = audio_file_path.replace('.mp3', '.wav')
        audio.export(wav_file_path, format='wav')
        return wav_file_path
    return audio_file_path

def split_audio(audio_file_path, chunk_length_ms=300000):
    audio = AudioSegment.from_wav(audio_file_path)
    chunks = make_chunks(audio, chunk_length_ms)
    chunk_paths = []
    for i, chunk in enumerate(chunks):
        chunk_path = f"{audio_file_path[:-4]}_chunk{i}.wav"
        chunk.export(chunk_path, format="wav")
        chunk_paths.append(chunk_path)
    return chunk_paths

def transcribe_audio_vosk(audio_file_path):
    audio_file_path = convert_audio_to_wav(audio_file_path)
    chunk_paths = split_audio(audio_file_path)
    model = vosk.Model("model/vosk")  # Ensure the Vosk model is in the "model/vosk" directory
    
    transcript = ""
    for chunk_path in chunk_paths:
        wf = wave.open(chunk_path, "rb")
        rec = vosk.KaldiRecognizer(model, wf.getframerate())
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                transcript += result.get("text", "") + " "
        result = json.loads(rec.FinalResult())
        transcript += result.get("text", "")
        os.remove(chunk_path)  # Clean up the chunk file after processing
    return transcript

def transcribe_audio_whisper(audio_file_path):
    settings = load_settings()
    openai.api_key = settings["openai_api_key"]
    audio_file_path = convert_audio_to_wav(audio_file_path)
    chunk_paths = split_audio(audio_file_path, chunk_length_ms=60000)  # 1-minute chunks
    
    transcript = ""
    for chunk_path in chunk_paths:
        with open(chunk_path, 'rb') as audio_file:
            transcription = openai.Audio.transcribe("whisper-1", audio_file)
        transcript += transcription['text'] + " "
        os.remove(chunk_path)  # Clean up the chunk file after processing
    return transcript

def transcribe_all_audios(directory, method="local"):
    transcripts = {}
    for filename in os.listdir(directory):
        if filename.endswith(".wav") or filename.endswith(".mp3"):
            full_path = os.path.join(directory, filename)
            if method == "local":
                transcripts[filename] = transcribe_audio_vosk(full_path)
            elif method == "whisper":
                transcripts[filename] = transcribe_audio_whisper(full_path)
    return transcripts
