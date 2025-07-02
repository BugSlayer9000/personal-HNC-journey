# samod subhasha
# 🔧 Activity 5 (Challenge): Rectangle Geometry

# 🔁 Extend: Ask the user for values, then create a rectangle and print area/perimeter.

class Rectangle:
    def __init__(self):
        self.get_height_and_width()
    
    def get_height_and_width(self):
        try:
            self.height = int(input("Enter the Height : "))
            self.width = int(int(input("Enter the Width : ")))
        except:
            print("Invalid Input ! ")
    
    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        perimeter = 2 * (self.height + self.width)
        return perimeter

def main():
    rectangle = Rectangle()
    try:
        print(f"Area : {rectangle.area()}")
        print(f"Perimeter : {rectangle.perimeter()}")
    except:
        print("Error")

if __name__ == "__main__":
    main()
    

