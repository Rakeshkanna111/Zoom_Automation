import webbrowser
import pyautogui
import time


def join_to_meeting(meeting_id, password):

    url = 'https://zoom.us/wc/join/' + meeting_id
    webbrowser.get('firefox').open_new_tab(url)
    time.sleep(10)

    join_button = pyautogui.locateAllOnScreen('join_button.png')
    pyautogui.moveTo(join_button)
    pyautogui.click()
    time.sleep(3)

    password_button = pyautogui.locateCenterOnScreen("password.png")
    pyautogui.moveTo(password_button)
    pyautogui.write(password)
    pyautogui.click()



class_timings = ['09:00:00', '10:00:00', '11:00:00', "14:00:00", "15:00:00"]

while True:

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    for timings in class_timings:
        if current_time == timings:

            if timings == "09:00:00":
                join_to_meeting("8437561852", "2121")

            if timings == "10:00:00":
	        join_to_meeting("8437561852", "2121")

            if timings == "11:32:00":
                join_to_meeting("8437561852", "2121")

            if timings == "14:00:00":
                join_to_meeting("8437561852", "2121")

            if timings == "15:00:00":
                join_to_meeting("8437561852", "2121")
