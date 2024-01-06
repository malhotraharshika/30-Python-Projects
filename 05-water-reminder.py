from win10toast import ToastNotifier
import time

notification = ToastNotifier()

while True:
  time.sleep(2700) # remind you to drink water after every 45 minutes
  notification.show_toast(
    "Remainder",
    "Drink Water! Time to Hydrate",
    duration = 5,
    icon_path = "icon.ico,
    threaded = True,
  )
  
