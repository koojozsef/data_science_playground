# AI Video Generator from Two Frames

This project uses AI (currently linear interpolation, can be replaced with a deep learning model) to generate a video by interpolating between two input images.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the script:
   ```bash
   python main.py path/to/frame1.jpg path/to/frame2.jpg --num_interpolations 8 --output output.mp4
   ```

## Files
- `main.py`: CLI entry point
- `interpolation.py`: Frame interpolation logic (replace with AI model as needed)
- `video_utils.py`: Video creation utilities
