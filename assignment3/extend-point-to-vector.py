# python "magic methods":
# "__eq__" for equality
# "__add__" as "+"
# "__sub__" as "-"
# ... https://www.geeksforgeeks.org/python/dunder-magic-methods-python/

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, another_point):
        # print(f"__eq__: {type(self)} == {type(another_point)}")
        return self.x == another_point.x and self.y == another_point.y

    # override system __str__() to print user-readable object values
    def __str__(self):
        return f"Point: x={self.x}, y={self.y}"
    
    def clone(self):
        return Point(self.x, self.y)
    
    # Euclidian distance to another point
    def calculate_distance(self, another_point):
        if isinstance(another_point, Point): # or type(self) istead of= Point
            # print(f"calculate_distance: {type(self)} to {type(another_point)}")
            x1 = self.x
            x2 = another_point.x
            y1 = self.y
            y2 = another_point.y
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class Vector(Point):
    def __str__(self):
        return f"Vector: x={self.x}, y={self.y}"
    
    def __add__(self, another_vector):
        if isinstance(another_vector, Vector): # or type(self) istead of Vector
            return Vector(self.x + another_vector.x, self.y + another_vector.y)

point_1 = Point(5, 10)
print(point_1)

point_2 = Point(15, 100)
print(point_2)

vector_1 = Vector(5, 10)
print(vector_1)

vector_2 = Vector(50, 100)
print(vector_2)

# points equality
print(point_1 == point_2) # False
print(point_1 == point_1.clone()) # True

# vector addition
print(vector_1 + vector_2)

# calculate_distance from point to another point
print(point_1.calculate_distance(point_2))

# calculate_distance from vector to point
print(vector_1.calculate_distance(point_2))

# calculate_distance from point to vector
print(point_2.calculate_distance(vector_1))

# calculate_distance from vector to another vector
print(vector_1.calculate_distance(vector_2))

# vector equality
print(vector_1 == vector_2) # False

# vector to point equality
# (vector_1.clone() generates Point, because the parent method "clone" is not overridden in Vector)
print(vector_1 == vector_1.clone()) # True
