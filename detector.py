import cv2
from ultralytics import YOLO
import argparse
import os

def detect_objects(source, model_path='models/yolov8n.pt', output_dir='results'):
    """
    Detects objects in an image or video using YOLOv8.
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the YOLOv8 model (auto-downloads if not found)
    print(f"Loading model: {model_path}...")
    model = YOLO(model_path)

    # Run inference
    print(f"Running detection on: {source}...")
    results = model.predict(source=source, save=True, project=output_dir, name='detection_run', exist_ok=True)

    print(f"Detection complete. Results saved to: {output_dir}/detection_run")
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CCTV Footage Object Detection using YOLOv8")
    parser.add_argument("--source", type=str, default="data/test_image.jpg", help="Path to input image or video")
    parser.add_argument("--model", type=str, default="yolov8n.pt", help="YOLOv8 model version (n, s, m, l, x)")
    
    args = parser.parse_args()

    # Ensure data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    if not os.path.exists(args.source):
        print(f"Error: Source file {args.source} not found.")
        print("Please place a sample image in the 'data' folder or provide a valid path.")
    else:
        detect_objects(args.source, model_path=args.model)
