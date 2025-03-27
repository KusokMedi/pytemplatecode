import time
import sys

def timer(seconds):
    if not isinstance(seconds, int):
        raise ValueError("Ошибка: Введите целое число секунд. Если нужно дробное время, используйте библиотеку time.")

    for i in range(seconds, 0, -1):
        print(f"{i} секунд осталось...")
        time.sleep(1)

    print("Время вышло!")

def current_time(format="%Y-%m-%d %H:%M:%S"):
    return time.strftime(format, time.localtime())

def inputint(prompt="Введите число: "):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():  # Проверка, что введено целое число
            return int(user_input)
        else:
            print("Ошибка: Пожалуйста, введите целое число.")


def start(name="Your project name", delay=0.25):
    frame = "-" * len(name) + "--"

    lines = [
        f"[{frame}]\n"
        f"[ {name} ]\n"
        f"[{frame}]\n"
    ]

    # Печать начального оформления по одному символу
    for line in lines:
        for char in line:
            if char == " ":
                sys.stdout.write(char)
                sys.stdout.flush()
                continue
            elif char == "-":
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay/3)
            else:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
        print()

def end(end_text="End of code!", delay=0.25):
    end_frame = "-" * len(end_text) + "--"

    sys.stdout.write("\n")
    lines = [
        f"[{end_frame}]\n"
        f"[ {end_text} ]\n"
        f"[{end_frame}]\n"
    ]
    for line in lines:
        for char in line:
            if char == " ":
                sys.stdout.write(char)
                sys.stdout.flush()
                continue
            elif char == "-":
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay/5)
            else:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
        print()