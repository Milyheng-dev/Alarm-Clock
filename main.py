import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "faaah.mp3"
    is_running = True

    while is_running:
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(currentTime)

        if currentTime == alarm_time:
            print("Wake up!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            while pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
                time.sleep(1)

            is_running = False
        time.sleep(1)

if __name__ == '__main__':
    alarm_time = input("Enter the alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)