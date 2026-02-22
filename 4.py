# class dog:
#   def bark(self):# self has to be given if the fun is declared inside the class
#         print(self)
#         print("dog barking")
#
# d =dog()
# print(d)
# d.breed = "husky"

class Car:
    def start(self):
        print("car starting")

    def gear(self, gr):
        print("gear shifted to" , gr)
        if gr==0:
            self.stop()

    def stop(self):
        print("car stopping")


class Driver:
    def drive(self):
        self.c=Car()
        print(self.c)
        self.c.start()
        self.c.gear(2)
        self.c.gear(5)
        self.c.stop()

d = Driver()
d.drive()

