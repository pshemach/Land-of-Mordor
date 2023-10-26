class Subject:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscribers):
        self.subscribers.append(subscribers)

    def notify(self, obj):
        print(f'Notify observers {obj} has come')
