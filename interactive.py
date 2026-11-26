import time

MAGIC_BALL_THINKING_SECONDS = 3
MAGIC_BALL_REVEAL_DELAY_SECONDS = 2


def magicball():
    print("Шар думает над ответом...")
    time.sleep(MAGIC_BALL_THINKING_SECONDS)
    print("И ответ...")
    time.sleep(MAGIC_BALL_REVEAL_DELAY_SECONDS)
