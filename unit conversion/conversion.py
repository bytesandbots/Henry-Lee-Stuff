class Conversion:

    def __init__(self):
        self.result = None
    def convert(self, unit1, unit2, value):
        # Lengths
        # Kilometers
        if unit1 == "Km":
            if unit2 == "M":
                self.result = value * 0.621371
        # Miles
        elif unit1 == "M":
            if unit2 == "Km":
                self.result = value * 1.60934
        # Weights
        # Pounds
        elif unit1 == "Lbs":
            if unit2 == "Kg":
                self.result = value * 0.45359237
            elif unit2 == "Ounces":
                self.result = value 
        elif unit1 == "Kg":
            if unit2 == "Lbs":
                self.result = value * 2.20462
            elif unit2 == "Ounces":
                self.result = value * 35.274
        # Ounces
        elif unit1 == "Ounces":
            if unit2 == "Lbs":
                self.result = value * 2.20462
            elif unit2 == "Kg":
                self.result = value / 35.274
        # Invalid
        else:
            self.result = "Invalid"
            
        return self.result


