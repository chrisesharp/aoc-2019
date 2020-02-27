class Keyboard():
    def __init__(self):
        self.buffer = []
    
    def append(self, command):
        for c in reversed(command):
            self.buffer.append(ord(c))

    def pop(self):
        if not self.buffer:
            print("Enter command:")
            command = input() + "\n"
            for c in reversed(command):
                if command:
                    self.buffer.append(ord(c))
        return self.buffer.pop()
