class Event:
    def __init__(self):
        self.handlers = []
    def subscribe(self, handler):
        self.handlers.append(handler)
    def notify(self, *args):
        for handler in self.handlers:
            handler(*args)

def on_data(data):
    print(f"Received: {data}")

event = Event()
event.subscribe(on_data)
event.notify("Data Stream Connected")
