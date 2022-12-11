import time
from plyer import notification,audio

count = 0


def long_break():
    notification.notify(
        title="Congrats you have 20 minutes of rest",
        message="Congrats you have completed 4 cycle in row keep going on.."
    )
    time.sleep(2)
def short_break():
    notification.notify(
        title="5 minutes of rest",
        message=f'Yeah you have completed {count} cycle. you have only {4-count} cycles to complete'
    )
    time.sleep(2)
def start_pomo():
    while True:
        notification.notify(
            title="Timer has started",
            message="Start working for 25 minutes"
        )
        time.sleep(3)
        global count
        count += 1
        if count == 4:
            long_break()
            count = 0
        else:
            short_break()


n = 1
while n:
    s = input("type 's' to start and 'e' to exit the pomodoro : ")
    if s == 's':
        start_pomo()
    else:
        exit()