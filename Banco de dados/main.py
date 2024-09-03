import config
from ultralytics import YOLO
from utils import detect_webcam_video
from utils import update_daily_totals
import utils
from PIL import Image
import cv2
from time import sleep

import os

HOME = os.getcwd()
print(HOME)

# conn, cursor = config.connect()
# breakpoint()

# Load a model
model = YOLO("best_training_n8.pt")
# breakpoint()
print("Bem vindo ao AI Food!")
sleep(2)

# print("Você já possui cadastro? Digite a opção correspondente")
# print("1 - Sim")
# print("2 - Não")

# is_signed_up = input()

# if is_signed_up not in ["1", "2"]:
#     print("Opção inválida")
#     exit()

is_signed_up = "1"

if is_signed_up == "1":

    # email = input("Insira seu email: ")
    # password = input("Insira sua senha: ")

    # user = utils.user_login(email, password)
    conn, cursor = config.connect()
    update_daily_totals(conn, cursor)
    detect_webcam_video(model, conn, cursor)

# breakpoint()


# test = {1: utils.create_user}
