from ultralytics import YOLO
from PIL import Image
import cv2
import utils

import os

model = YOLO("best.pt")

VALID_TAGS = [
    "lettuce",
    "rice",
    "banana",
    "potato",
    "meat",
    "onion",
    "beans",
    "chicken",
    "orange",
    "milk",
    "apple",
    "watermelon",
    "strawberry",
    "egg",
    "tomato",
]

accepted_extensions = ["jpg", "jpeg", "png"]

base_path = os.getcwd()

for tag in VALID_TAGS:
    destination_path = f"/data/images/test/{tag}"
    try:
        os.chdir(base_path + destination_path)
    except Exception:
        print(f'\nthe current directory path "{destination_path}" is not valid!!\n')
        # print(
        #     f"make sure this script is inserted where the following folders for the mode {selected_mode} would be for example: /data/images/{selected_mode}/{selected_tag}"
        # )
        exit()

    for filename in os.listdir(os.getcwd()):
        _, _, extension = filename.partition(".")

        if extension.lower() not in accepted_extensions:
            continue
        image = Image.open(filename)
        results = model.predict(image, save=True)

    os.chdir(base_path)
