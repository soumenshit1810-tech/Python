class EmailService:
    def send(self, msg):
        print(f"Email sent: {msg}")

class Notification:
    def __init__(self, service):
        self.service = service

    def notify(self, msg):
        self.service.send(msg)

email_service = EmailService()
notifier = Notification(email_service)
notifier.notify("Advanced Python is awesome!")
