import sys
import os
import subprocess
import whisper

video_path = sys.argv[1]
model = whisper.load_model("small")  # 可改成 "medium" 或 "large"

print(f"[INFO] 正在为 {video_path} 生成字幕...")
result = model.transcribe(video_path, verbose=True)

srt_path = os.path.splitext(video_path)[0] + ".srt"
with open(srt_path, "w", encoding="utf-8") as f:
    for i, seg in enumerate(result["segments"], 1):
        start = seg["start"]
        end = seg["end"]
        text = seg["text"].strip()
        f.write(f"{i}\n")
        f.write(f"{start:.3f} --> {end:.3f}\n")
        f.write(f"{text}\n\n")

print(f"[INFO] 字幕已保存到 {srt_path}")
