from ultralytics import YOLO
from utils import detect_webcam_video
from PIL import Image
import cv2

import os

HOME = os.getcwd()
print(HOME)

# Load a model
model = YOLO("best_training_n8.pt")
# breakpoint()
detect_webcam_video(model)
