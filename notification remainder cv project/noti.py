import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
        title="All Day Remainder",
        message="Today I Have To Submit"
                "My assignment And You Have"
                "Not Completed It Till Now",
        timeout=10
    )
        time.sleep(10)