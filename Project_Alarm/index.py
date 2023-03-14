from playsound import playsound
import time 

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elap = 0
    print(CLEAR)
    while time_elap < seconds:
        time.sleep(1)
        time_elap += 1

        time_left = seconds - time_elap
        minute_left = time_left // 60 
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}{minute_left:02d} : {seconds_left:02d}")

    return True

active = False

if __name__ == "__main__":
    hour = int(input(" Enter the Hour set to alarm : "))
    minute = int(input(" Enter the Minute set to alarm : "))
    second = int(input(" Enter the seconds set to alarm : "))
    total_seconds = (((hour * 60) + minute) * 60) + second
    active = alarm(total_seconds)
    if active:
        playsound("sound.mp3")

