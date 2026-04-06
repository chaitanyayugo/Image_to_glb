import torch
import cv2
import numpy as np
from transformers import pipeline

# Uses Depth Anything V2 (free, HuggingFace)
depth_pipeline = pipeline(
    task="depth-estimation",
    model="depth-anything/Depth-Anything-V2-Small-hf"
)

def get_depth_map(image_path: str) -> np.ndarray:
    from PIL import Image
    image = Image.open(image_path).convert("RGB")
    result = depth_pipeline(image)
    depth = np.array(result["depth"])
    # Normalize to 0-255
    depth = (depth - depth.min()) / (depth.max() - depth.min()) * 255
    return depth.astype(np.uint8)
