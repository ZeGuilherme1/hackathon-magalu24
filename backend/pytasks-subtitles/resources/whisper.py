from faster_whisper import WhisperModel
from datetime import timedelta
import os

#config
task = "transcribe" # tasks: translate, transcribe

def format_time(seconds: int):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    milliseconds = (seconds - int(seconds)) * 1000
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d},{int(milliseconds):03d}"

def transcribe_video(input_file: str):
    model_size = "medium"  # other models: small, medium, large-v2, tiny

    # Run on CPU with INT8
    model = WhisperModel(model_size, device="cpu", cpu_threads=12, compute_type="int8")

    # Remove task="translate" if you want the original language
    segments, info = model.transcribe(input_file, beam_size=5, task=task, vad_filter=True)

    srt_string = ""
    
    for segment in segments:
        start_time = format_time(segment.start)
        end_time = format_time(segment.end)
        text = segment.text
        segment_id = segment.id + 1
        line_out = f"{segment_id}\n{start_time} --> {end_time}\n{text.lstrip()}\n\n"
        srt_string += f"{segment_id}\n{start_time} --> {end_time}\n{text.lstrip()}\n\n"
        
    return str(info), srt_string