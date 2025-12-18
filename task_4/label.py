import subprocess

input_path = "detections_video.py.mp4"
output_path = "detections_video_compressed.mp4"

# Compress using libx264 and CRF 28
subprocess.run([
    "ffmpeg",
    "-i", input_path,
    "-vcodec", "libx264",
    "-crf", "28",
    output_path
])
print("Video compression complete:", output_path)
