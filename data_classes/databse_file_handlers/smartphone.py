
class SmartPhone():
    def __init__(self, brand, model, price, made_in, dealer, imei_code, stores=[]):
        super().__init__()
        self.brand = brand
        self.model = model
        self.price = price
        self.made_in = made_in
        self.dealer = dealer
        self.imei_code = imei_code
        self.stores = stores

    # methods for SmartPhone object comparison
    def __eq__(self, other):
        return self.imei_code == other.imei_code

    def __gt__(self, other):
        return self.imei_code > other.imei_code

    def __ge__(self, other):
        return self.imei_code >= other.imei_code

    def __str__(self):
        return str({"brand": self.brand, "model": self.model, "price": self.price, "made_in": self.made_in, "dealer": self.dealer, "IMEI_CODE": self.imei_code, "stores": self.stores})

    def make_array(self):
        return [self.brand, self.model, self.price, self.made_in, self.dealer, self.imei_code]
