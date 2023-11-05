class Car:



    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year= year
        self.color = color


    def drive(self):
        print("움직이는중")
    
    def stop(self):
        print("멈춤")