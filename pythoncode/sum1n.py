

class sum1n:
    def __init__(self):
        self.a = self.count()


    def count(self, b=0):
        b += 1
        return b

if __name__ == "__main__":
    my = sum1n()
    my = sum1n()

    print(my.a)
