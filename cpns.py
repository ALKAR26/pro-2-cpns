from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="YourApp"  # Change this to your app's name
    )

if __name__ == "__main__":
    notification_title = "Notification Title"
    notification_message = "This is a pop-up notification."

    send_notification(notification_title, notification_message)
