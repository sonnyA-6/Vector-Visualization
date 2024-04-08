from vectorClass import Vector2D

import math

class UniformField:
    def __init__(self, magnitude, direction):
        self.magnitude = magnitude
        self.direction = direction

    def get_vector_at(self, x, y):
        """Returns a uniform vector despite the x,y position"""
        ux = self.magnitude * math.cos(self.direction)
        uy = self.magnitude * math.sin(self.direction)

        return Vector2D(ux, uy)