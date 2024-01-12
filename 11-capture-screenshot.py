import os
import argparse
import pyautogui
import time

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path", help="absolute path to store screenshot.", default=r"./images")

args = parser.parse_args()

time.sleep(2)

os.makedirs(args.path, exist_ok=True)

current_time = time.strftime("%Y-%m-%d_%H_%M_%S")
file = f"screenshot_{current_time}.jpg"

save_path = os.path.join(args.path, file)
image = pyautogui.screenshot(save_path)
print(f"{file} saved successfully at: {save_path}")
