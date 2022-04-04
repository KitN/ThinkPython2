# For ThinkPython Chapter 17 Exersize 2

class Kangaroo():
    def __init__(self):
        self.pouch_contents = []

    def __str__(self):
        return "Pouch: " + str(self.pouch_contents)

    def put_in_pouch(self, thing):
        self.pouch_contents += [thing]


def main():
    kanga = Kangaroo()
    roo = Kangaroo()
    roo.put_in_pouch('skittle')
    kanga.put_in_pouch(roo)
    print(kanga)
    print(roo)

if __name__=='__main__':
    main()
