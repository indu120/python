class Details:
    def brand(self):
        self.brand_name = input("What brand do you want? ")
        print("Brand of the mobile is:", self.brand_name)

    def price(self):
        self.price_value = input("What price do you want? ")
        print("Price of the mobile is:", self.price_value)

    def color(self):
        self.color_name = input("What color do you want? ")
        print("Color of the mobile is:", self.color_name)

class Mobile:
    def mobiledetails(self):
        print("Mobile details:")
        self.md = Details()
        self.md.brand()
        self.md.price()
        self.md.color()
    def switchon(self):
        print("Switching on...")

    def switchoff(self):
        print("Switching off...")

    def listenmusic(self):
        print("Listening music...")


class Handler:

    def use(self):
        self.m = Mobile()
        print("\nUsing mobile...")
        self.m.switchon()
        self.m.listenmusic()
        print("Stopped listening music...")
        self.m.switchoff()


# Object creation

md=Mobile()
md.mobiledetails()
m = Handler()
m.use()