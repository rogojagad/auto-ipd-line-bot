class MessageEventHandler:
    def __init__(self):
        pass

    def handle(self, event):
        return event.message.text

    def test(self):
        print("Message event handler loaded")

if __name__ == "__main__":
    pass