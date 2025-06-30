import argparse
from interpolation import interpolate_frames
from video_utils import create_video_from_frames
import cv2
import os

def main():
    parser = argparse.ArgumentParser(description="AI Video Generator: Interpolate between two frames.")
    parser.add_argument('frame1', type=str, help='Path to the first image frame')
    parser.add_argument('frame2', type=str, help='Path to the second image frame')
    parser.add_argument('--num_interpolations', type=int, default=8, help='Number of intermediate frames to generate')
    parser.add_argument('--output', type=str, default='output.mp4', help='Output video file name')
    args = parser.parse_args()

    img1 = cv2.imread(args.frame1)
    img2 = cv2.imread(args.frame2)
    frames = interpolate_frames(img1, img2, args.num_interpolations)
    frames = [img1] + frames + [img2]
    create_video_from_frames(frames, args.output)
    print(f"Video saved to {args.output}")

if __name__ == "__main__":
    main()
