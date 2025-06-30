import cv2
import numpy as np

def create_video_from_frames(frames, output_path, fps=15):
    height, width, layers = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    for frame in frames:
        video.write(frame)
    video.release()
