import cv2
import math
import supervision as sv
import random
from ingredients_crud import get_foods_by_name
from food_diary_crud import create_diary_entry
from food_diary_crud import read_daily_totals
from users_crud import read_user

annotator = sv.BoxAnnotator()

CLASS_NAMES_PTBR = [
    "alface",
    "arro",
    "banana",
    "batata",
    "carne",
    "cebola",
    "feijão",
    "frango",
    "laranja",
    "leite",
    "maçã",
    "melancia",
    "morango",
    "ovo",
    "tomate",
]

CLASS_NAMES_FOR_SEARCH = {
    "lettuce": "alface",
    "rice": "arroz",
    "banana": "banana",
    "potato": "batata",
    "meat": "carne",
    "onion": "cebola",
    "beans": "feijão",
    "chicken": "frango",
    "orange": "laranja",
    "milk": "leite",
    "apple": "maçã",
    "watermelon": "melancia",
    "strawberry": "morango",
    "egg": "ovo",
    "tomato": "tomate",
}

FOOD_TYPE_OPTIONS = {}


CONFIDENCE_THRESHOLD = 0.90
LAST_DETECTED_INGREDIENT = ""
IS_INGREDIENT_DETECTED = False
global TOTAL_DAILY_CALORIC_INTAKE
TOTAL_DAILY_CALORIC_INTAKE = 0
FONT = cv2.FONT_HERSHEY_SIMPLEX


def get_foodscale_reading():
    return random.randint(50, 500)


# Example usage:
def draw_ingredient_options_text(image):
    text_Y_position = 270
    # breakpoint()
    if not IS_INGREDIENT_DETECTED:
        return

    cv2.putText(
        image,
        "Selecione o tipo do alimento",
        (20, text_Y_position),
        FONT,
        1,
        (0, 255, 255),
        2,
        cv2.LINE_4,
    )

    text_Y_position = text_Y_position + 50

    global LAST_DETECTED_INGREDIENT
    # breakpoint()
    for index, food_option in enumerate(FOOD_TYPE_OPTIONS[LAST_DETECTED_INGREDIENT], 1):
        cv2.putText(
            image,
            f"{index}: {food_option.food_name} {food_option.variety}",
            (20, text_Y_position),
            FONT,
            1,
            (0, 255, 255),
            2,
            cv2.LINE_4,
        )

        text_Y_position = text_Y_position + 50


def draw_bounding_boxes(image, boxes, conn, cursor):
    global IS_INGREDIENT_DETECTED

    if IS_INGREDIENT_DETECTED:
        draw_ingredient_options_text(image)
        return

    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = (
            int(x1),
            int(y1),
            int(x2),
            int(y2),
        )
        food_id = int(box.cls[0])

        confidence = math.ceil((box.conf[0] * 100)) / 100

        if food_id and confidence >= CONFIDENCE_THRESHOLD:
            global LAST_DETECTED_INGREDIENT

            food_options = get_foods_by_name(CLASS_NAMES_PTBR[food_id], conn, cursor)
            # breakpoint()
            IS_INGREDIENT_DETECTED = True
            LAST_DETECTED_INGREDIENT = CLASS_NAMES_PTBR[food_id]
            FOOD_TYPE_OPTIONS[LAST_DETECTED_INGREDIENT] = food_options

        confidence = math.ceil((box.conf[0] * 100)) / 100
        print("Confidence --->", confidence)

        if confidence >= CONFIDENCE_THRESHOLD:
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 255), 3)

            org = [x1, y1]
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            box_text = f"{CLASS_NAMES_PTBR[food_id]} - {confidence*100}%"
            cv2.putText(image, box_text, org, FONT, fontScale, color, thickness)


def detect_webcam_video(model, conn, cursor):
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        _, image = cap.read()
        results = model(image, stream=True)
        global TOTAL_DAILY_CALORIC_INTAKE

        for result in results:
            draw_bounding_boxes(image, result.boxes, conn, cursor)
            cv2.putText(
                image,
                f"Total de Calorias: {TOTAL_DAILY_CALORIC_INTAKE}",
                (250, 460),
                FONT,
                1,
                (0, 255, 255),
                2,
                cv2.LINE_4,
            )

        cv2.imshow("Webcam", image)

        key = cv2.waitKey(1)
        global IS_INGREDIENT_DETECTED
        if key == ord("q"):
            break
        elif key == ord("1") and IS_INGREDIENT_DETECTED:
            food_amount = get_foodscale_reading()

            selected_food = FOOD_TYPE_OPTIONS[LAST_DETECTED_INGREDIENT][0]

            create_diary_entry(
                food_amount,
                selected_food.food_name,
                selected_food.variety,
                2,
                conn,
                cursor,
            )

            update_daily_totals(conn, cursor)
        elif key == ord("2") and IS_INGREDIENT_DETECTED:
            food_amount = get_foodscale_reading()
            # breakpoint()
            if len(FOOD_TYPE_OPTIONS[LAST_DETECTED_INGREDIENT]) >= 2:
                selected_food = FOOD_TYPE_OPTIONS[LAST_DETECTED_INGREDIENT][1]

                create_diary_entry(
                    food_amount,
                    selected_food.food_name,
                    selected_food.variety,
                    2,
                    conn,
                    cursor,
                )

                update_daily_totals(conn, cursor)

        elif key == ord("3") and IS_INGREDIENT_DETECTED:
            food_amount = get_foodscale_reading()

            if len(FOOD_TYPE_OPTIONS[LAST_DETECTED_INGREDIENT]) >= 3:
                selected_food = FOOD_TYPE_OPTIONS[LAST_DETECTED_INGREDIENT][2]

                create_diary_entry(
                    food_amount,
                    selected_food.food_name,
                    selected_food.variety,
                    2,
                    conn,
                    cursor,
                )

                update_daily_totals(conn, cursor)

        elif key == ord("4") and IS_INGREDIENT_DETECTED:
            if len(FOOD_TYPE_OPTIONS[LAST_DETECTED_INGREDIENT]) >= 4:
                food_amount = get_foodscale_reading()

                selected_food = FOOD_TYPE_OPTIONS[LAST_DETECTED_INGREDIENT][3]

                create_diary_entry(
                    food_amount,
                    selected_food.food_name,
                    selected_food.variety,
                    2,
                    conn,
                    cursor,
                )

                update_daily_totals(conn, cursor)

    cap.release()
    cv2.destroyAllWindows()


def user_login(email: str, password: str):
    user = read_user(email, password)
    if not user:
        print(
            f"Não foi encontrado nenhum usuário com o email '{email}' e a senha fornecida. Tente novamente"
        )
        return None
    return user


def initialize_food_scale():
    pass


def update_daily_totals(conn, cursor):
    daily_totals = read_daily_totals(user_id=2, conn=conn, cursor=cursor)

    if not daily_totals:
        return
    global TOTAL_DAILY_CALORIC_INTAKE
    TOTAL_DAILY_CALORIC_INTAKE = daily_totals["total_calories"]

    print(f"Total Protein: {daily_totals['total_protein']}")
    print(f"Total Carbs: {daily_totals['total_carbs']}")
    print(f"Total Fats: {daily_totals['total_fats']}")
    print(f"Total Calories: {daily_totals['total_calories']}")

    global IS_INGREDIENT_DETECTED
    IS_INGREDIENT_DETECTED = False
