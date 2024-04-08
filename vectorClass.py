"""This class will represent a two-dimensional vector (x,y).
   In this class users will be able to:
    - Magnitude
    - Add/Subtract
    - Dot multiplication
    - Normalizing
    - Scalar Multiplication
    - define the name & return the name
    """

import math


class Vector2D:

    def __init__(self, x, y, vectorname = ''):
        if not isinstance(x,(int, float)) or isinstance(y,(int,float)):
            raise ValueError("Vector coordinates must be integers or floats.")
        self.x = x
        self.y = y
        self._vectorname = vectorname   #Private attribute

    def vectormagnitude(self):
        """Returns the magntitude of the vector"""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def add(self, other):
        
        """This returns the addition of two vectors."""
        if not isinstance(other, Vector2D):
            raise ValueError("The other object must of vector2D.")
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def subtract(self, other):
        """This returns the subtraction of two vectors."""
        if not isinstance(other, Vector2D):
            raise ValueError("The other object must be of vector2D")
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def dotMultiplication(self, other):
        """This returns the dot multiplication of two vectors.
        Dot multiplication is where corresponding elements of the vector are
        multiplied then added. The result is the dot product."""
        if not isinstance(other, Vector2D):
            raise ValueError("The other object must be of vector2D")
        return self.x * other.x + self.y * other.y
    
    def normalize(self):
        """Converts the specified vector into a unit vector. The vector will
        still maintain its property of direction, only now it has a magnitude of
        one."""
        magnitude = self.vectormagnitude()
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector2D(self.x / magnitude, self.y / magnitude )
    
    def scalarMultiplication(self, scalar):
        """Returns the result of a vector multiplied by a scalar (constant)."""
        
        return Vector2D(self.x * scalar, self.y * scalar)
            
    
    def nameofvector(self):
        """Returns the name of the vector"""
        return self._vectorname
    
    def vectorName(self, name):
        """Sets the name of the vectur. Includes validation."""
        if not isinstance(name, str):
            raise ValueError("Vector name must be of type string.")
        self._vectorname = name
    
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y}, '{self._vectorname}')"
