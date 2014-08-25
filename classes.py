import json


class Part:

    def __init__(self, part_number, description, price):
        self.part_number = part_number
        self.description = description
        self._price = price

    def get_price(self, discount):
        return self._price * (discount / 100)

    @staticmethod
    def static_method(one, two, three):
        return one + two + three


myPart = Part("3L5Z 15A35-AA", "Oil filter", 2000)

print(myPart.get_price(10.0))

class FinisPart(Part):
    def __init__(self):
        pass



something = [1, 2, 3, 4, {"This": "Is", "A": ["Dictionary", "!"], 5: 6}]
print(json.JSONEncoder().encode(something))

print(json.JSONEncoder().encode(myPart.__dict__))