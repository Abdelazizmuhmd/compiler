class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())