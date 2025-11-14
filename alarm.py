import time
import datetime
import pygame

def alarm(alarm_time):
    print(f"your alarm has been set")
    ring="fire_alarm.mp3"   #add your sound file path here
    is_running=True
    while is_running:
        now=datetime.datetime.now().strftime("%H:%M:%S")
        print(now)
        if now == alarm_time:
            print(f"WAKE UP 🫨")
            pygame.mixer.init()
            pygame.mixer.music.load(ring)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running=False
        time.sleep(1)

        


t = input("enter your alarm time (HH:MM:SS)")
alarm(t)