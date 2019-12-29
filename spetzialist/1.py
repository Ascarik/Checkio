
class Lamp:
    is_on = False

    def on(self):
        print("Лампа включина")
        if not self.is_on:
            self.is_on = True

    def off(self):
        if self.is_on:
            print("Лампа выключина")
            self.is_on = False
        else:
            print("Лампа не включали")

    # def __str__(self):
    #     return "jbbh"

    def __repr__(self):
        print("jbbh")



lamp1 = Lamp()
lamp2 = Lamp()

print(dir(Lamp))

lamp1.on()
lamp1.off()

lamp1