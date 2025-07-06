# samod subhasha
# 🔧 Activity 5 (Challenge): Rectangle Geometry
# Create a Rectangle class with width and height as inputs.
# Add methods:

# area() to return area

# perimeter() to return perimeter

# 🔁 Extend: Ask the user for values, then create a rectangle and print area/perimeter.

class Rectangle:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
    
    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        perimeter = 2 * (self.height + self.width)
        return perimeter

def main():
    rectangle = Rectangle(6,5)
    print(f"Area : {rectangle.area()}")
    print(f"Perimeter : {rectangle.perimeter()}")

if __name__ == "__main__":
    main()
    

