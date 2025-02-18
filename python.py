class Area:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
        self.area = self.calculate_area()
        self.price_per_square_meter = self.calculate_price_per_square_meter()

    def calculate_area(self):
        return self.width * self.width

    def calculate_price_per_square_meter(self):
        if 1<=self.area<=20:
            return 50
        elif 21<=self.area<=49:
            return 45
        else:
            return 40

    def calculate_total_cost(self):
        return self.area*self.price_per_square_meter
    
    def display_cost(self):
        total_cost = self.calculate_total_cost()
        print(f"Price per square metre (euros): {self.price_per_square_meter}\nTotal cost (euros): {total_cost}")

length = int(input("Input the length of the area in meters: "))
width = int(input("Input the width of the area in meters: "))

area_instance = Area(length, width)

area_instance.display_cost()